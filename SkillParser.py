'''
    This script is used to extract skills from the resume
'''

import re

from csv_skills import make_csv

import pandas as pd

#function to compare and match all the skills
import os 

def match_individual_skill(skill_to_match, filetext):

    

    skill_to_check = r"(" + skill_to_match + ")"
    print("skill_to_check", skill_to_match, "-->", len(skill_to_match))

    regex = skill_to_check

    if len(skill_to_match) <= 5:
        regex = r"[\s\,]" + skill_to_match + "[\s\,]"

    #Finditer returns an iterator over all matches in the text

    if skill_to_match == 'C' or skill_to_match == 'R':
        matches = re.finditer(regex, filetext, re.MULTILINE)
    else:
        matches = re.finditer(regex, filetext, re.MULTILINE | re.IGNORECASE)
    
    count = 0


    # Iterates over the "matches" iterator 
    for matchNum, match in enumerate(matches, start=1):
        count = count + 1

        #To print where the match was found in text file and number of matches found in that particular group

        print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                            end=match.end(), match=match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                                                                           start=match.start(groupNum),
                                                                           end=match.end(groupNum),
                                                                           group=match.group(groupNum)))
    print("count", count)
    if count > 0:
        return True
    return False

#function to iterate over all the skills category
def match_skill_category(directory,filetext):

    
    if os.path.isdir(os.path.join(directory,'csv_files')):
        print("csv_files directory exists")
        if os.path.isfile(os.path.join(directory,'csv_files/Skills_list.csv')):
            print("file exists")
        else:
            csv_df=make_csv()

    else:
        os.mkdir(os.path.join(directory,'csv_files'))
        csv_df=make_csv()

    csv_df.to_csv(os.path.join(directory,'csv_files/Skills_list.csv'))


    

    skill_df= pd.read_csv(os.path.join(directory,'csv_files/Skills_list.csv'))

    print(skill_df["Web_Mobile_and_Desktop_Application_Development"])

    skills = dict()

    # print filetext
    Software_Engineering_Lst = list()
    Web_Mobile_and_Desktop_Application_Development_Lst = list()
    Artificial_Intelligence_Lst = list()
    Special_Technologies_and_Expertise_Areas_Lst = list()
    APIs_and_Packages_Lst = list()
    Other_Skills_Lst = list()
    combined_skill_list = list()

    #Comparing the data with the list

    for i in range(0,skill_df["Software_Engineering"].count()):
        
        if (match_individual_skill(skill_df["Software_Engineering"].iloc[i], filetext)):
            combined_skill_list.append(skill_df["Software_Engineering"].iloc[i].replace('\\', ''))
            Software_Engineering_Lst.append(skill_df["Software_Engineering"].iloc[i])            
            skills['Software_Engineering'] = Software_Engineering_Lst

    for j in range(0,skill_df["Web_Mobile_and_Desktop_Application_Development"].count()):
        
        if (match_individual_skill(skill_df["Web_Mobile_and_Desktop_Application_Development"].iloc[j], filetext)):
            combined_skill_list.append(skill_df["Web_Mobile_and_Desktop_Application_Development"].iloc[j].replace('\\', ''))
            Web_Mobile_and_Desktop_Application_Development_Lst.append(skill_df["Web_Mobile_and_Desktop_Application_Development"].iloc[j])            
            skills["Web_Mobile_and_Desktop_Application_Development"] = Web_Mobile_and_Desktop_Application_Development_Lst

    for k in range(0,skill_df["Artificial_Intelligence"].count()):
        
        if (match_individual_skill(skill_df["Artificial_Intelligence"].iloc[k], filetext)):
            combined_skill_list.append(skill_df["Artificial_Intelligence"].iloc[k].replace('\\', ''))
            Artificial_Intelligence_Lst.append(skill_df["Artificial_Intelligence"].iloc[k])            
            skills["Artificial_Intelligence"] = Artificial_Intelligence_Lst


    for l in range(0,skill_df["Special_Technologies_and_Expertise_Areas"].count()):
        
        if (match_individual_skill(skill_df["Special_Technologies_and_Expertise_Areas"].iloc[l], filetext)):
            combined_skill_list.append(skill_df["Special_Technologies_and_Expertise_Areas"].iloc[l].replace('\\', ''))
            Special_Technologies_and_Expertise_Areas_Lst.append(skill_df["Special_Technologies_and_Expertise_Areas"].iloc[l])            
            skills['Special_Technologies_and_Expertise_Areas'] = Special_Technologies_and_Expertise_Areas_Lst


    for m in range(0,skill_df["APIs_and_Packages"].count()):
        
        if (match_individual_skill(skill_df["APIs_and_Packages"].iloc[m], filetext)):
            combined_skill_list.append(skill_df["APIs_and_Packages"].iloc[m].replace('\\', ''))
            APIs_and_Packages_Lst.append(skill_df["APIs_and_Packages"].iloc[m])            
            skills['APIs_and_Packages'] = APIs_and_Packages_Lst

    for n in range(0,skill_df["Other_Skills"].count()):
        
        if (match_individual_skill(skill_df["Other_Skills"].iloc[n], filetext)):
            combined_skill_list.append(skill_df["Other_Skills"].iloc[n].replace('\\', ''))
            Other_Skills_Lst.append(skill_df["Other_Skills"].iloc[n])            
            skills['Other_Skills'] = Other_Skills_Lst       
        
            


    # print("skills ", skills)
    print("combined_skill_list", combined_skill_list)
    return combined_skill_list