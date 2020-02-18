import pandas as pd

#changing txt file to csv file

# writing data to a new file changing the first delimiter only
new_temp = open('new-box-resume-data.txt', 'w') 
with open('box-resume-data.txt') as f:
    for line in f:
        # only replace first two instance of ,(comma) to use this as delimiter for pandas
        line = line.replace(',', '|', 1)
        line = line.replace(',', '|', 1) 
        new_temp.write(line)
new_temp.close()

df = pd.read_csv('new-box-resume-data.txt', delimiter='|', header=None, names= ["LDTalent","Email","Skills"])
df=df[2:]
if os.path.isdir(os.path.join('./','csv_files')):
    print("csv_files directory exists")
else:
    os.mkdir(os.path.join('./','csv_files'))

df.to_csv('./csv_files/new_resume_data.csv', index=False)
