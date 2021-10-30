import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import glob
inputFolder='training_sailboat_stylegan2_resized'
os.mkdir('training_sailboat_stylegan2_flipped')
# Load .png image
#image = cv2.imread('cruise_stylegan2/seed0000.png')
i=0
#to flip the image horizontally
for img in glob.glob(inputFolder + "/*.jpg"):
    print(img)
    image = cv2.imread(img)
    flip = cv2.flip(image,1) # change the value from 1 to 0 if vertical flipping is desired
    cv2.imwrite('training_sailboat_stylegan2_flipped/tugs_test_stylegan2flipped%04i.jpg' % i, flip)
    i+=1

