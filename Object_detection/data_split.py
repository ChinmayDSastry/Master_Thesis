import cv2
import os
# import glob
import numpy as np
# from random import shuffle
from math import floor
import shutil
inputFolder = r'E:\New folder\TUGS_STYLEGAN2\tugs'
#

os.mkdir('Training_real_tugs') #create directory for training
os.mkdir('Validation_real_tugs') #create directory for validation/test


import os
import sys
from random import shuffle

#arg = sys.argv[1]

cnt = os.listdir(r'E:\sailboat')

random_number = [i for i in range(len(cnt))]
shuffle(random_number)

idx = 0

for filename in os.listdir(r'E:\New folder\TUGS_STYLEGAN2\tugs'):
	new_str = os.path.realpath(r'E:\New folder\TUGS_STYLEGAN2\tugs')+'/'+str(random_number[idx])+'-'+filename
	os.rename(os.path.realpath(r'E:\New folder\TUGS_STYLEGAN2\tugs')+'/'+filename, os.path.realpath(r'E:\New folder\TUGS_STYLEGAN2\tugs')+'/'+str(random_number[idx]+1)+'-'+filename)
	idx+=1


def get_training_and_testing_sets(file_list):
    split = 0.7 #specify the split ratio can be 0.6,0.7,0.8,0.9 depending on the user
    split_index = floor(len(file_list) * split)
    training = file_list[:split_index]
    testing = file_list[split_index:]
    return training, testing

file_list = []
for path, dirs, files in os.walk(r'E:\New folder\TUGS_STYLEGAN2\tugs'):
    for f in files:
        file_list.append(f)

training,testing=get_training_and_testing_sets(file_list)

#print("Training",len(training))
#print("Testing",len(testing))
#print(training)
i =0
for img in training:
    try:
        image =cv2.imread(os.path.join(r'E:\New folder\TUGS_STYLEGAN2\tugs',img))
        image = np.uint8(image)
    except Exception as e:
        print(img)  #checks for corrupt images
    finally:
        cv2.imwrite("Training_real_tugs/realtugtrain-image%04i.jpg" %i, image) #naming the image accordingly
        print(i)
        i=i+1
     #cv2.waitKey(30)
cv2.destroyAllWindows()
j= 0
for img in testing:
    try:
        image = cv2.imread(os.path.join(r'E:\New folder\TUGS_STYLEGAN2\tugs', img))
        image = np.uint8(image)
    except Exception as e:
        print("file not found")
        print(img)
    finally:
        cv2.imwrite("Validation_real_tugs/realtugvalidate-image%04i.jpg" % j, image)#naming the images accordingly
        print(j)
        j= j+1
cv2.destroyAllWindows()