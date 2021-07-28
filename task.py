# Assessment Kandidat Data Scientist Telkom
# Author: Dandy Arif Rahman
# Date: 28 Juli 2021

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import listdir
from os.path import join

# Global Variables
NEW_SIZE = (100, 100)
DEFAULT_DATA_PATH = 'Data/'
DEFAULT_CSV_FILENAME = 'images.csv'

# Functions
def file_to_array(file, image_size=NEW_SIZE):
    # read image as numeric array representation
    image = Image.open(file)
    image = image.resize(NEW_SIZE)
    image = np.asarray(image)
    image = image.reshape(-1)
    
    return list(image)

def folder_to_csv(path=DEFAULT_DATA_PATH, filename=DEFAULT_CSV_FILENAME, image_size=NEW_SIZE):
    # write csv file given folder path with drum and guitar images
    folder = ['drum/', 'guitar/']
    
    # init a data frame
    df = pd.DataFrame(columns=['label', 'array'])
    index = 0
    
    for i in range(2):
        for file in listdir(join(path, folder[i])):
            # inserting label
            df.loc[index, 'label'] = i
            
            img_arr = file_to_array(join(path, folder[i], file), image_size=image_size) # read image as numeric array
            img_arr = [str(binary) for binary in img_arr] # convert numeric array to array of string
            img_arr = ','.join(img_arr) # convert array of string to string
            
            # inserting array representation of image
            df.loc[index, 'array'] = img_arr
            
            # increment index
            index += 1
    
    # writing to csv file
    df.to_csv(filename, index=False, header=None)

def str_to_array(s):
    # convert str to numeric array
    return np.asarray([int(binary) for binary in s.split(',')])

def show_img(array, image_size=NEW_SIZE):
    # show image of the given string representation of array
    img_arr = str_to_array(array).reshape((*image_size, -1))
    plt.imshow(img_arr)
    plt.show()

def main():
    # Task 1: write images numeric representation into csv file
    # output file will be DEFAULT_CSV_FILENAME
    folder_to_csv(path=DEFAULT_DATA_PATH, filename=DEFAULT_CSV_FILENAME, image_size=NEW_SIZE)
    
    # Task 2: display images from csv files
    df = pd.read_csv(DEFAULT_CSV_FILENAME, names=['label', 'array'])
    for i in range(len(df)):
        array = df.loc[i, 'array']
        show_img(array, image_size=NEW_SIZE)

if __name__ == "__main__":
    main()