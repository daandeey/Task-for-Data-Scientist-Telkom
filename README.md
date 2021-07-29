# Task-for-Data-Scientist-Telkom
This repository is a mandatory task for assessment of Data Scientist Role at Telkom. It consists of 2 tasks.

## Task 1
Given images of drums and guitars. Write a program to convert those images into array representation and write it to csv file.

## Task 2
From the csv file that has been created, extract the array and show the image.

## How to Run
Make sure your drum and guitar folder is in right path (in this case: Data folder). Install all the dependencies. Then, run the python file and a csv file will be built and images will be shown. 
```
pip install -r requirements.txt
python task.py
```

To change the image size, data folder path, and csv files. Please change the value of these global variables in task.py.
```
# Global Variables
NEW_SIZE = (100, 100)
DEFAULT_DATA_PATH = 'Data/'
DEFAULT_CSV_FILENAME = 'images.csv'
```
