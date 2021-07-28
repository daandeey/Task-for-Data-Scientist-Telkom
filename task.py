# Assessment Kandidat Data Scientist Telkom
# Author: Dandy Arif Rahman
# Date: 28 Juli 2021

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

NEW_SIZE = (100, 100)

def file_to_array(file, image_size=NEW_SIZE):
    # read image as numeric array representation
    image = Image.open(file)
    image = image.resize(NEW_SIZE)
    image = np.asarray(image)
    image = image.reshape(-1)
    
    return list(image)

def folder_to_csv(path='Data/', filename='images.csv'):
    folder = ['drum/', 'guitar/']
    
    # init a data frame
    df = pd.DataFrame(columns=['label', 'array'])
    index = 0
    
    for i in range(2):
        for file in listdir(join(path, folder[i])):
            # inserting label
            df.loc[index, 'label'] = i
            
            img_arr = file_to_array(join(path, folder[i], file)) # read image as numeric array
            img_arr = [str(binary) for binary in img_arr] # convert numeric array to array of string
            img_arr = ','.join(img_arr) # convert array of string to string
            
            # inserting array representation of image
            df.loc[index, 'array'] = img_arr
            
            # increment index
            index += 1
    
    # writing to csv file
    df.to_csv(filename, index=False)

def str_to_array(s):
    return np.asarray([int(binary) for binary in s.split(',')])

def show_img(array, size=NEW_SIZE):
    img_arr = str_to_array(array).reshape((*size, -1))
    plt.imshow(img_arr)
    plt.show()

def main():
    # Task 1: write images numeric representation into csv file
    # output file will be 'images.csv'
    folder_to_csv(path='Data/', filename='images.csv')
    
    # Task 2: display images from csv files
    df = pd.read_csv('images.csv')
    for i in range(2):
        array = df.loc[i, 'array']
        show_img(array)

if __name__ == "__main__":
    main()

