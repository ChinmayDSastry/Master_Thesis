import cv2
import os
import glob
import numpy as np
from os import listdir
from PIL import Image
i=0
for filename in listdir('./sailboat/'):
    if filename.endswith('.jpg'):
        try:
            img = Image.open('./sailboat/' + filename)  # open the image file
            img.verify()  # verify that it is, in fact an image
            #print(filename)
            i=i+1
            #print(i)

        except (IOError, SyntaxError) as e:
            print('Bad file:', filename)  # print out the names of corrupt files
            i=i+1
            print(i)
