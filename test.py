import pandas as pd
import os
import shutil

files = pd.read_csv('/users/anshikageanra/desktop/lab/data/log_sample.csv')
new_path = '/Users/anshikageanra/PycharmProjects/ML-projects/sample/'

file_path = files.iloc[:, 4]
# file = file_path[0].split('/')
# new = os.path.join(new_path,file[-1])
# print(new)
# print(file[-1])
for i in file_path:
    file = i.split('/')
    new = os.path.join(new_path, file[-1])
    shutil.copyfile(i, new)
