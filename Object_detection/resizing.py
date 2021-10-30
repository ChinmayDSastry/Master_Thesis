import cv2
import glob
import os
import numpy as np
inputFolder = r'E:\New folder\tugs-stylegan2'
os.mkdir('resized_512_tugs_stylegan2_original')

#This method resizes with aspect ratio maintained but is not square, which is not suitable for Stylegan2
def resize(image,window_height = 512):
    aspect_ratio = float(image.shape[1])/float(image.shape[0])
    window_width = window_height/aspect_ratio
    image = cv2.resize(image, (int(window_height),int(window_width)))
    return image


# This method crops from the center and keeps the aspect ratio Caution,(Important features might get lost for training StyleGAN 2 ada)
def crop_square(img, size, interpolation=cv2.INTER_AREA):
    h, w = img.shape[:2]
    min_size = np.amin([h,w])

    # Centralize and crop
    crop_img = img[int(h/2-min_size/2):int(h/2+min_size/2), int(w/2-min_size/2):int(w/2+min_size/2)]
    resized = cv2.resize(crop_img, (size, size), interpolation=interpolation)
    return resized

i=0
for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)
    new_img = image.resize(image,512) #can be changed
    #resized = cv2.resize(image,(512,512)) Resizing without aspect ratio maintained, another augmentation method
    cv2.imwrite("resized_512_tugs_stylegan2_original/stylegan2tug_original%04i.jpg" % i, new_img)
    i += 1

cv2.destroyAllWindows()