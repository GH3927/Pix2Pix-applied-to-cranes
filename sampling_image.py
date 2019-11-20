import shutil
import os
import random

folders = os.listdir('C:/Users/gyuha/OneDrive - 충남대학교/메카트로닉스 (대학원)/인공지능응용/Project/crane2')

for folder in folders:
    directory = os.listdir('C:/Users/gyuha/OneDrive - 충남대학교/메카트로닉스 (대학원)/인공지능응용/Project/crane2/%s'%folder)
    if folder == 'train':
        directory = random.sample(directory, 1600)
    else:
        directory = random.sample(directory, 400)
    for file in directory:
        src = 'C:/Users/gyuha/OneDrive - 충남대학교/메카트로닉스 (대학원)/인공지능응용/Project/crane2/{}/{}'.format(folder,file)
        dst = 'C:/Users/gyuha/OneDrive - 충남대학교/메카트로닉스 (대학원)/인공지능응용/Project/sample_1600/%s'%folder
        shutil.copy(src, dst)