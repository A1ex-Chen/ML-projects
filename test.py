import pandas as pd
import os
import shutil

files = pd.read_csv('/users/anshikageanra/desktop/lab/data/withoutTest/log_vespa_withoutTest.csv')
new_path = '/Users/anshikageanra/PycharmProjects/ML-projects/sample/'

file_path = files.iloc[:, 2]
print(file_path)
# file = file_path[0].split('vcs/')
# filename = file[-1].split('/')
# dir = file[-1].split('/'+'{filename1}'.format(filename1=filename[-1]))
# # print(dir)
# newdir = os.path.join(new_path, dir[0])
# print(newdir)
# if not os.path.isdir(newdir):
#     os.makedirs(newdir)
# new = os.path.join(new_path,file[-1])
# # print(new)
# print(file[-1])

for i in file_path:
    file = i.split('vcs/')
    filename = file[-1].split('/')
    dir = file[-1].split('/'+'{filename1}'.format(filename1=filename[-1]))
    newdir = os.path.join(new_path, dir[0])
    if not os.path.isdir(newdir):
        os.makedirs(newdir)
    new = os.path.join(new_path, file[-1])
    shutil.copyfile(i, new)
