import pandas as pd
import os

from csv_skills import make_csv


def skill_count(directory, csv_file):

    colnames=["ENGINEER",'SKILLS IN RESUME', 'SKILLS IN LD']
    df_merge= pd.read_csv(os.path.join(directory,csv_file),names=colnames,header=None)
    df_merge= df_merge[1:]

    Skill_Count= "Skills_Count.csv"
    
    Skill_Count_df= first_skill(directory,df_merge)

    return Skill_Count


#To check and count all the skills

def first_skill(directory,dataframe):

    if os.path.isdir(directory):
        print("csv_files directory exists")
        if os.path.isfile(os.path.join(directory,'Skills_list.csv')):
            print("file exists")
        else:
            make_csv()
    else:
        os.mkdir(directory)
        make_csv()


    skill_df= pd.read_csv(os.path.join(directory,'Skills_list.csv'))


    New_Dataframe_dict={

        "Engineer_name":[],
        "Skill in Both Resume and List":[],
        "Skills only on Resume":[],
        "Skills only on LDTalent":[],
        "Skills Neither on LDTalent and on Resume":[],
        "Skill Count in Both Resume and List":[],
        "Skills Count only on Resume":[],
        "Skills Count only on LDTalent":[],
        "Skills Count Neither on LDTalent and on Resume":[]

    }
    
    #Comparing the data with all the skills list of Skills_list.csv

    for engineer in range(0,len(dataframe)):
        New_Dataframe_dict['Engineer_name'].append(dataframe["ENGINEER"].iloc[engineer]) 
        print("Processing for {}".format(dataframe["ENGINEER"].iloc[engineer]))  
        Skill_Both_Lst = list()
        Skills_LD_Lst = list()
        Skills_RESUME_Lst = list()
        Skills_Not_Both_Lst = list()         
        
        for i in range(0,skill_df["Software_Engineering"].count()):                
            if skill_df["Software_Engineering"].iloc[i].upper() in dataframe["SKILLS IN RESUME"].iloc[engineer].upper() and skill_df["Software_Engineering"].iloc[i].upper() in dataframe['SKILLS IN LD'].iloc[engineer].upper():
                Skill_Both_Lst.append(skill_df["Software_Engineering"].iloc[i].replace('\\', ''))
            elif skill_df["Software_Engineering"].iloc[i].upper() in dataframe["SKILLS IN RESUME"].iloc[engineer].upper():
                Skills_RESUME_Lst.append(skill_df["Software_Engineering"].iloc[i].replace('\\', ''))
            elif skill_df["Software_Engineering"].iloc[i].upper() in dataframe['SKILLS IN LD'].iloc[engineer].upper():
                Skills_LD_Lst.append(skill_df["Software_Engineering"].iloc[i].replace('\\', ''))
            else:
                Skills_Not_Both_Lst.append(skill_df["Software_Engineering"].iloc[i].replace('\\', ''))

        for j in range(0,skill_df["Web_Mobile_and_Desktop_Application_Development"].count()):                
            if skill_df["Web_Mobile_and_Desktop_Application_Development"].iloc[j].upper() in dataframe["SKILLS IN RESUME"].iloc[engineer].upper() and skill_df["Web_Mobile_and_Desktop_Application_Development"].iloc[j].upper() in dataframe['SKILLS IN LD'].iloc[engineer].upper():
                Skill_Both_Lst.append(skill_df["Web_Mobile_and_Desktop_Application_Development"].iloc[j].replace('\\', ''))
            elif skill_df["Web_Mobile_and_Desktop_Application_Development"].iloc[j].upper() in dataframe["SKILLS IN RESUME"].iloc[engineer].upper():
                Skills_RESUME_Lst.append(skill_df["Web_Mobile_and_Desktop_Application_Development"].iloc[j].replace('\\', ''))
            elif skill_df["Web_Mobile_and_Desktop_Application_Development"].iloc[j].upper() in dataframe['SKILLS IN LD'].iloc[engineer].upper():
                Skills_LD_Lst.append(skill_df["Web_Mobile_and_Desktop_Application_Development"].iloc[j].replace('\\', ''))
            else:
                Skills_Not_Both_Lst.append(skill_df["Web_Mobile_and_Desktop_Application_Development"].iloc[j].replace('\\', ''))

        for k in range(0,skill_df["Artificial_Intelligence"].count()):                
            if skill_df["Artificial_Intelligence"].iloc[k].upper() in dataframe["SKILLS IN RESUME"].iloc[engineer].upper() and skill_df["Artificial_Intelligence"].iloc[k].upper() in dataframe['SKILLS IN LD'].iloc[engineer].upper():
                Skill_Both_Lst.append(skill_df["Artificial_Intelligence"].iloc[k].replace('\\', ''))
            elif skill_df["Artificial_Intelligence"].iloc[k].upper() in dataframe["SKILLS IN RESUME"].iloc[engineer].upper():
                Skills_RESUME_Lst.append(skill_df["Artificial_Intelligence"].iloc[k].replace('\\', ''))
            elif skill_df["Artificial_Intelligence"].iloc[k].upper() in dataframe['SKILLS IN LD'].iloc[engineer].upper():
                Skills_LD_Lst.append(skill_df["Artificial_Intelligence"].iloc[k].replace('\\', ''))
            else:
                Skills_Not_Both_Lst.append(skill_df["Artificial_Intelligence"].iloc[k].replace('\\', ''))

        for l in range(0,skill_df["Special_Technologies_and_Expertise_Areas"].count()):                
            if skill_df["Special_Technologies_and_Expertise_Areas"].iloc[l].upper() in dataframe["SKILLS IN RESUME"].iloc[engineer].upper() and skill_df["Special_Technologies_and_Expertise_Areas"].iloc[l].upper() in dataframe['SKILLS IN LD'].iloc[engineer].upper():
                Skill_Both_Lst.append(skill_df["Special_Technologies_and_Expertise_Areas"].iloc[l].replace('\\', ''))
            elif skill_df["Special_Technologies_and_Expertise_Areas"].iloc[l].upper() in dataframe["SKILLS IN RESUME"].iloc[engineer].upper():
                Skills_RESUME_Lst.append(skill_df["Special_Technologies_and_Expertise_Areas"].iloc[l].replace('\\', ''))
            elif skill_df["Special_Technologies_and_Expertise_Areas"].iloc[l].upper() in dataframe['SKILLS IN LD'].iloc[engineer].upper():
                Skills_LD_Lst.append(skill_df["Special_Technologies_and_Expertise_Areas"].iloc[l].replace('\\', ''))
            else:
                Skills_Not_Both_Lst.append(skill_df["Special_Technologies_and_Expertise_Areas"].iloc[l].replace('\\', ''))

        for m in range(0,skill_df["APIs_and_Packages"].count()):                
            if skill_df["APIs_and_Packages"].iloc[m].upper() in dataframe["SKILLS IN RESUME"].iloc[engineer].upper() and skill_df["APIs_and_Packages"].iloc[m].upper() in dataframe['SKILLS IN LD'].iloc[engineer].upper():
                Skill_Both_Lst.append(skill_df["APIs_and_Packages"].iloc[m].replace('\\', ''))
            elif skill_df["APIs_and_Packages"].iloc[m].upper() in dataframe["SKILLS IN RESUME"].iloc[engineer].upper():
                Skills_RESUME_Lst.append(skill_df["APIs_and_Packages"].iloc[m].replace('\\', ''))
            elif skill_df["APIs_and_Packages"].iloc[m].upper() in dataframe['SKILLS IN LD'].iloc[engineer].upper():
                Skills_LD_Lst.append(skill_df["APIs_and_Packages"].iloc[m].replace('\\', ''))
            else:
                Skills_Not_Both_Lst.append(skill_df["APIs_and_Packages"].iloc[m].replace('\\', ''))

        for n in range(0,skill_df["Other_Skills"].count()):                
            if skill_df["Other_Skills"].iloc[n].upper() in dataframe["SKILLS IN RESUME"].iloc[engineer].upper() and skill_df["Other_Skills"].iloc[n].upper() in dataframe['SKILLS IN LD'].iloc[engineer].upper():
                Skill_Both_Lst.append(skill_df["Other_Skills"].iloc[n].replace('\\', ''))
            elif skill_df["Other_Skills"].iloc[n].upper() in dataframe["SKILLS IN RESUME"].iloc[engineer].upper():
                Skills_RESUME_Lst.append(skill_df["Other_Skills"].iloc[n].replace('\\', ''))
            elif skill_df["Other_Skills"].iloc[n].upper() in dataframe['SKILLS IN LD'].iloc[engineer].upper():
                Skills_LD_Lst.append(skill_df["Other_Skills"].iloc[n].replace('\\', ''))
            else:
                Skills_Not_Both_Lst.append(skill_df["Other_Skills"].iloc[n].replace('\\', ''))

        New_Dataframe_dict["Skill in Both Resume and List"].append(Skill_Both_Lst)
        New_Dataframe_dict["Skills only on Resume"].append(Skills_RESUME_Lst)
        New_Dataframe_dict["Skills only on LDTalent"].append(Skills_LD_Lst)
        New_Dataframe_dict["Skills Neither on LDTalent and on Resume"].append(Skills_Not_Both_Lst)
        New_Dataframe_dict["Skill Count in Both Resume and List"].append(len(Skill_Both_Lst))
        New_Dataframe_dict["Skills Count only on Resume"].append(len(Skills_RESUME_Lst))
        New_Dataframe_dict["Skills Count only on LDTalent"].append(len(Skills_LD_Lst))
        New_Dataframe_dict["Skills Count Neither on LDTalent and on Resume"].append(len(Skills_Not_Both_Lst))

    #Creating a dataframe with the dictionary

    df=pd.DataFrame.from_dict(
        New_Dataframe_dict,
        orient='index'
    )
        
    df=df.transpose()


    df.to_csv(os.path.join(directory,"Skill_count.csv"))



