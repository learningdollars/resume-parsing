import csv
import json
import os
import sys
from datetime import datetime
import requests
import shutil  


import argparse

#used only for google drive pdfs
import imagetotext as im2text

from FileUtils import convert_pdf_to_txt, extract_text_from_pdf, pdf_2_pil_images, concat_and_save_images, \
    extract_text_from_json, TARGET_DIRECTORY, extract_developer_name, download_gdrive_files

from SkillParser import match_skill_category

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-D", "--directory", required=True,
                help="Directory/folder having resumes")
ap.add_argument("-O", "--ocr", required=False, default=False,
                help="Want to use Google Vision API?")
ap.add_argument("-G", "--google", required=False, default=False,
                help="google-resume-file-text file name")


args = vars(ap.parse_args())

fmt = "%Y_%m_%d_%I_%M_%S_%p"
now = datetime.now()
new_skill_list_filename = 'engineerlist_' + now.strftime(fmt) + '.csv'

LEARNING = 0
BEGINNER = 1
MODERATE = 2
ADVANCED = 3
EXPERIENCE = (
    (LEARNING, 'LEARNING'),
    (BEGINNER, 'BEGINNER'),
    (MODERATE, 'MODERATE'),
    (ADVANCED, 'ADVANCED')
)


class FreelancerSkill(object):

    def __init__(self,  name_ld, skill, years_of_experience, experience_level):
        self.freelancer_name_ld = name_ld
        self.skill = skill
        self.years_of_experience = years_of_experience
        self.experience_level = experience_level

    def __str__(self):
        return 'Freelancer ' + self.freelancer_name_ld + \
               ' has skill ' + json.dumps(self.skill) + \
               ' with ' + str(self.years_of_experience) + ' years of experience;' + \
               ' at ' + str(EXPERIENCE[self.experience_level]) + ' level'


# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.


def main( fileSavingDirectory ,directory , filetype='pdf', ocr=False):

    print("Current working directory in main()", "=>", os.getcwd())
    engineer = ''
    print("Current working directory after os.getcwd()", "=>", os.getcwd())

    conversion_candidates = dict()
    count = 0
    other_filetype_counter = 0   
        
    #Creates csv file in csv folder with the name of Engineer and skill set
    with open(os.path.join(fileSavingDirectory,new_skill_list_filename), 'a', encoding='utf-8', newline='') as csv_data_file:
        writer = csv.writer(csv_data_file)

        writer.writerow(["ENGINEER","SKILLS"])

        #To iterate over all the files in the directory
        for filename in os.listdir(directory):
            
            # Parsing the resume with .pdf extension 
            if filename.lower().endswith(".pdf") and filetype == 'pdf':

                count = count + 1

                print("processing file", "=>", filename)

                filename = "" + filename + ""
                skills_retrieved = []

                try:
                    #fist converting pdf into txt 

                    engineer, text = convert_pdf_to_txt(filename)

                    #passes the text file to compare and search for the skills

                    skills_retrieved = match_skill_category(text)

                    #Another method for extracting skills using textract
                    if len(skills_retrieved) == 0:
                        print("No Skills Found.Trying PYPDF for", filename)
                        engineer, text = extract_text_from_pdf(filename)
                        skills_retrieved = match_skill_category(text)

                    if len(skills_retrieved) == 0:
                        print("No Skills Found.Trying Textract Explicitly for ", filename)
                        engineer, text = extract_text_from_pdf(filename, 1)
                        skills_retrieved = match_skill_category(text)

                    print(engineer)                 
             


                except TypeError as e:
                    print(e, "While processing file:- ", filename)
                except Exception as oth:
                    print(oth, "While processing file:- ", filename)

                #When OCR is true converting pdf to image
                if len(skills_retrieved) == 0 and ocr:
                    print("Converting to images since no skills were found")
                    conversion_candidates[extract_developer_name(filename)] = filename
                    
            #for json file returned from google vision API
            elif filename.lower().endswith('.json'):
                print("JSON file.")
                engineer = extract_developer_name(filename)
                text = extract_text_from_json(filename)
                skills_retrieved = match_skill_category(text)
            else:
            # If resume are of other format
                print("File name with other extension", filename)
                other_filetype_counter = other_filetype_counter + 1
                continue

            
            writer.writerow([engineer,  skills_retrieved])
        

            #Note: This code returns advanced level for all and returns 30 years of experience
            fs = FreelancerSkill(engineer,  skills_retrieved, 30., ADVANCED)
            print(fs)

    #When using OCR
    if len(conversion_candidates) > 0:
        print("List of files to be converted", conversion_candidates)
        tmp_path = os.path.join(os.getcwd(), "converted_resumes")
        try:
            os.mkdir("converted_resumes")
        except FileExistsError:
            print("converted_resumes directory already exists!")
        #Converting to image
        for devname, fname in conversion_candidates.items():
            pil_images = pdf_2_pil_images(fname, tmp_path)
            concat_and_save_images(pil_images, devname)
        im2text.process_directory(os.getcwd())
        main(os.getcwd(), 'json')

    if os.path.isdir(os.path.join(fileSavingDirectory,'csv_files')):
        print("csv_files directory exists")
    else:
        os.mkdir(os.path.join(fileSavingDirectory,'csv_files'))
    #Changing the directory of csv
    shutil.move(os.path.join(fileSavingDirectory,new_skill_list_filename), os.path.join(fileSavingDirectory,'csv_files'))

    #number of resume that were parsed    
    print("Resumes processed:-", count)
    #number of files that could not be parsed 
    print("Other Format Files:-", other_filetype_counter)






if __name__ == '__main__':

    TARGET_DIRECTORY = args["directory"]
    
    TARGET_DIRECTORY_MAIN=os.getcwd()
    
    os.chdir(TARGET_DIRECTORY)

    TARGET_DIRECTORY = os.getcwd()  # Setting  target directory value to new current working directory

    if args["google"]:
        download_gdrive_files(args["google"])

    if args["ocr"]:
        main(TARGET_DIRECTORY_MAIN,TARGET_DIRECTORY, True)
    else:
        main(TARGET_DIRECTORY_MAIN,TARGET_DIRECTORY)
