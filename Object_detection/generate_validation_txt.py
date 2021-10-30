
import os

full_path_to_images = r'E:\MSC-THESIS\expt2_withAUG_SailboatJetty\synth'


os.chdir(full_path_to_images)


p = []


for current_dir, dirs, files in os.walk('.'):
    # Going through all files
    for f in files:
        # Checking if filename ends with '.jpeg'
        # Change it to .png if the images are in .png format
        if f.endswith('.png'):
            # Preparing path to save into train.txt file
            # If you're using Windows, it might need to change
            # this: + '/' +
            # to this: + '\' +
            # or to this: + '\\' +
            path_to_save_into_txt_files = '/content/drive/MyDrive/yolo_custom_model_Training/darknet/data/sailboat_fake' + '/' + f

            # Appending the line into the list
            # when writing lines into txt files
            p.append(path_to_save_into_txt_files + '\n')



"""
End of:
Getting list of full paths to labelled images
"""


"""
Start of:
Creating validation.txt
"""

# Creating file validation.txt
with open('validation.txt', 'w') as validation_txt:
    # Going through all elements of the list
    for e in p:
        # Writing current path at the end of the file
        validation_txt.write(e)

