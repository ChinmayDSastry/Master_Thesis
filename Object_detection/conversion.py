import cv2
import glob
import os
inputFolder = r'D:\msc_thesis\cruise_test'
os.mkdir('jpg_conversion')
# To convert images to JPG from PNG
i=0 #mg = cv2.imread("cruise_test.jpg")
for img in glob.glob(inputFolder + "/*.jpg"):
     image = cv2.imread(img)

     cv2.imwrite("jpg_conversion/sailboat_synth%04i.jpg" %i, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
     i+=1
     #print(image)

