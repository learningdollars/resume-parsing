
import pandas as pd 
import os
import csv

from ast import literal_eval

#dataframe with record of resume skills
colnames=["ENGINEER",'SKILLS']
df_resume=pd.read_csv("./csv_files/engineerlist_2020_02_15_03_49_17_PM.csv",names=colnames,header=None)
df_resume=df_resume.drop_duplicates(subset="ENGINEER", keep="first")
df_resume= df_resume[1:]

#making a copy of df_resume dataframe to later grab the skills using index
df_resume_2=pd.read_csv("./csv_files/engineerlist_2020_02_15_03_49_17_PM.csv",names=colnames,header=None)
df_resume_2=df_resume_2.drop_duplicates(subset="ENGINEER", keep="first")
df_resume_2=df_resume_2.set_index("ENGINEER")

#dataframe with record of LD_database skills
colnames_LD=["LDTALENTS",'EMAIL','SKILLS']
df_LD=pd.read_csv("./csv_files/new_resume_data.csv",names=colnames_LD,header=None)
df_LD=df_LD.drop_duplicates(subset="LDTalents", keep="first")
df_LD= df_LD[1:]

#making a copy of df_LD dataframe to later grab the skills using index
df_LD_2=pd.read_csv("./csv_files/new_resume_data.csv",names=colnames_LD,header=None)
df_LD_2= df_LD_2[1:]
df_LD_2=df_LD_2.drop_duplicates(subset="LDTalents", keep="first")
df_LD_2=df_LD_2.set_index("LDTalents")




#Merging both the dataframe by using common name
#Note: Dataframe can not be merged because of Name from Resume Parser

with open(os.path.join("./csv_files","Resume_ld_skills.csv"), 'w', encoding='utf-8', newline='') as csv_data_file:
    writer = csv.writer(csv_data_file)
    writer.writerow(["Name","Skills_Resume","Skills_ld"])

    for item_LD in df_LD["LDTALENTS"].tolist():
            
        for item_resume in df_resume["ENGINEER"].tolist(): 
            if item_LD.upper() in item_resume.upper():
                try:
                    name_ld=item_LD
                    skills_resume=df_resume_2.loc[item_resume]["SKILLS"]
                    skills_ld=df_LD_2.loc[item_LD]["SKILLS"]

                    count=0
                        for i in range(0,len(skills_resume)):
                                
                            if skills_resume[i].upper() in skills_ld.upper():
                                count=count+1
                        if len(skills_resume) > 20:
                            if count > 8:
                                writer.writerow([name_ld,skills_resume,skills_ld])
                            else:
                                print("Common name abort")

                        elif len(skills_resume) > 15:                           
                            if count > 6:
                                writer.writerow([name_ld,skills_resume,skills_ld])
                            else:
                                print("Common name abort")
                        else:
                            if count > 4:
                                writer.writerow([name_ld,skills_resume,skills_ld])
                            else:
                                print("Common name abort")
                except:
                        print("Not Found")                                              
                    
                break

            elif item_LD.split(' ')[0].upper() in item_resume.upper():

                if len(item_LD.split(' ')[0].upper())<4:
                    print("Not Found")
                    break             
                else:
                    try:
                            
                        name_ld=item_LD
                        skills_resume=df_resume_2.loc[item_resume]["SKILLS"]
                        skills_ld=df_LD_2.loc[item_LD]["SKILLS"]
                        skills_resume=literal_eval(skills_resume)
                            #To minimize the error in merging duw to common name
                        count=0
                        for i in range(0,len(skills_resume)):
                                
                            if skills_resume[i].upper() in skills_ld.upper():
                                count=count+1
                        if len(skills_resume) > 20:
                            if count > 8:
                                writer.writerow([name_ld,skills_resume,skills_ld])
                            else:
                                print("Common name abort")

                        elif len(skills_resume) > 15:                           
                            if count > 6:
                                writer.writerow([name_ld,skills_resume,skills_ld])
                            else:
                                print("Common name abort")
                        else:
                            if count > 4:
                                writer.writerow([name_ld,skills_resume,skills_ld])
                            else:
                                print("Common name abort")
                            
                    except:
                        print("Not Found")                   
                        
                    break






