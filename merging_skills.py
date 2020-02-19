import pandas as pd 
import os
import csv

from ast import literal_eval

from skills_count import skill_count

#Merging both the dataframe by using common name
#Note: Dataframe can not be merged because of Name from Resume Parser
def merge_skills(directory_csv, directory_txt,dataframe1,dataframe2):

    #dataframe with record of LD_database skills
    colnames_LD=["LDTALENTS",'EMAIL','SKILLS']
    df_LD=pd.read_csv(os.path.join(directory_csv,dataframe1),names=colnames_LD,header=None)
    df_LD=df_LD.drop_duplicates(subset="LDTALENTS", keep="first")
    df_LD= df_LD[1:]

    #making a copy of df_LD dataframe to later grab the skills using index
    df_LD_2=pd.read_csv(os.path.join(directory_csv,dataframe1),names=colnames_LD,header=None)
    df_LD_2= df_LD_2[1:]
    df_LD_2=df_LD_2.drop_duplicates(subset="LDTALENTS", keep="first")
    df_LD_2=df_LD_2.set_index("LDTALENTS")

    #dataframe with record of resume skills
    colnames=["ENGINEER",'SKILLS']
    df_resume=pd.read_csv(os.path.join(directory_csv,dataframe2),names=colnames,header=None)
    df_resume=df_resume.drop_duplicates(subset="ENGINEER", keep="first")
    df_resume= df_resume[1:]

    #making a copy of df_resume dataframe to later grab the skills using index
    df_resume_2=pd.read_csv(os.path.join(directory_csv,dataframe2),names=colnames,header=None)
    df_resume_2=df_resume_2.drop_duplicates(subset="ENGINEER", keep="first")
    df_resume_2=df_resume_2.set_index("ENGINEER")



    merge_csv="Resume_And_ld_skills.csv"

    #Opening a csv file to add the merged record

    with open(os.path.join(directory_csv,merge_csv), 'w', encoding='utf-8', newline='') as csv_data_file:
        writer = csv.writer(csv_data_file)
        writer.writerow(["Name","Skills_Resume","Skills_ld"])
        
        #To keep the record of names that were not found and those that could not be processed due to common name issue
        Not_Found=0
        Common_name_abort=0

        
        for item_LD in df_LD["LDTALENTS"].tolist():
            
            
                
            for item_resume in df_resume["ENGINEER"].tolist(): 
                if item_LD.upper() in item_resume.upper():
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
                                Common_name_abort+=1
                        
                        elif len(skills_resume) > 15:                           
                            if count > 6:
                                writer.writerow([name_ld,skills_resume,skills_ld])
                            else:                                
                                Common_name_abort+=1

                        elif len(skills_resume) > 8: 
                            if count > 4:
                                writer.writerow([name_ld,skills_resume,skills_ld])
                            else:
                                Common_name_abort+=1
                        elif len(skills_resume) > 5: 
                            if count > 2:
                                writer.writerow([name_ld,skills_resume,skills_ld])
                            else:
                                Common_name_abort+=1
                        else:
                            writer.writerow([name_ld,skills_resume,skills_ld])
                            
                    except:
                        
                        Not_Found+=1                   
                        
                    break


                elif item_LD.split(' ')[0].upper() in item_resume.upper():

                    if len(item_LD.split(' ')[0].upper())<4:
                        
                        Not_Found+=1
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
                                    Common_name_abort+=1
                                    
                            elif len(skills_resume) > 15:                           
                                if count > 7:
                                    writer.writerow([name_ld,skills_resume,skills_ld])
                                else:
                                    Common_name_abort+=1

                            elif len(skills_resume) > 10:
                                if count > 5 :
                                    writer.writerow([name_ld,skills_resume,skills_ld])
                                else:
                                    Common_name_abort+=1
                            else:
                                writer.writerow([name_ld,skills_resume,skills_ld])

                            
                        except:
                            
                            Not_Found+=1                   
                        
                        break
    

    print("Common name abort: {}".format(Common_name_abort))
    print("Not Found : {}".format(Not_Found))

    skill_count(directory_csv, merge_csv)

    
    






