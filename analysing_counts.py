import pandas as pd

from merging_skills import merge_skills

import argparse

import os


#Setting the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-L", "--LDdirectory", required=True,
                help="Directory/folder having the LD-data text file")
ap.add_argument("-R", "--Rdirectory", required=True,
                help="Directory/folder having the resume csv file")
args = vars(ap.parse_args())




def main(directory_ld_txt, directory_resume_csv, filetype="txt"):

    #checking for text file containing data of ld-talents database
    while True:
        file_name= input("Please enter the text file name : ")
        list_with_all_text_file=[]
        for filename in os.listdir(directory_ld_txt):            
                # Parsing the resume with .pdf extension 
                if filename.endswith(".txt") and filetype == 'txt':
                    list_with_all_text_file.append(filename)
        if file_name in list_with_all_text_file:
            ld_data=file_name
            break
        else:
            print("No such file found!! Please try again")

                
    
    # writing data to a new file changing the first delimiter only

    new_csv="ld_skills_data.csv"
    
    
    new_temp = open(os.path.join(directory_ld_txt,'temp-bos-resume-data.txt'), 'w') 
    with open(os.path.join(directory_ld_txt,ld_data)) as f:
        for line in f:
            # only replace first two instance of ,(comma) to use this as delimiter for pandas
            line = line.replace(',', '|', 1)        
            line = line.replace(',', '|', 1)
            new_temp.write(line)
            
    new_temp.close()

    #changing txt file to csv file

    df = pd.read_csv(directory_ld_txt+'/temp-box-resume-data.txt', delimiter='|', header=None, names= ["LDTalent","Email","Skills"])
    df=df[2:]
    df.to_csv(directory_resume_csv+ "//" + new_csv, index=False)

        #checking for csv file containing data of ld-talents database
    while True:
        file_name_csv= input("Please enter the name of csv file from resume parser : ")
        list_with_all_csv_file=[]
        for filename in os.listdir(directory_resume_csv):
                            
                # Parsing the resume with .pdf extension 
                if filename.endswith(".csv"):
                    list_with_all_csv_file.append(filename)
        
        if file_name_csv in list_with_all_csv_file:
            resume_data=file_name_csv
            break
        else:
            print("No such file found!! Please try again")

    resume_csv= resume_data
    
    #To merge both the data from ldTalent and 
    merge_skills( directory_resume_csv,directory_ld_txt,new_csv,resume_csv)


if __name__ == '__main__':

    TARGET_DIRECTORY = args["LDdirectory"] 
    TARGET_DIRECTORY_1 = args["Rdirectory"]  

    main(TARGET_DIRECTORY, TARGET_DIRECTORY_1)