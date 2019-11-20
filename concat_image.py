import numpy as np
import cv2
import os

folders = os.listdir('C:/Users/gyuha/OneDrive - 충남대학교/메카트로닉스 (대학원)/인공지능응용/Project/crane')

for folder in folders:
    directory = os.listdir('C:/Users/gyuha/OneDrive - 충남대학교/메카트로닉스 (대학원)/인공지능응용/Project/crane/%s/rendering'%folder)
    for file in directory:
        os.chdir('C:/Users/gyuha/OneDrive - 충남대학교/메카트로닉스 (대학원)/인공지능응용/Project/crane/%s/rendering'%folder)
        img1 = cv2.imread(file) #image file 불러옴
        os.chdir('C:/Users/gyuha/OneDrive - 충남대학교/메카트로닉스 (대학원)/인공지능응용/Project/crane/%s/labeling'%folder)
        img2 = cv2.imread(file)
        img3 = np.hstack((img1, img2[1:,1:,:]))
        cv2.imwrite('../../../crane2/{}/{}.jpg'.format(folder, file[6:11]), img3)
        
print('End')