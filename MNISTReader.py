import gzip
from PIL import Image
import numpy as np
############## EXERCISE 1 ##############

#Method to read the label files
def read_labels(filename):
    #Opening file
    with gzip.open(filename, 'rb') as f:
        #Finding the magic number and printing it
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("The magic number is:", magic)

        #Reading in the number of labels in the file
        numLabels = f.read(4)
        numLabels = int.from_bytes(numLabels, 'big')
        print("Number of labels: ", numLabels)

        labels = [f.read(1) for i in range(numLabels)]
        labels = [int.from_bytes(label, 'big') for label in labels]

    return labels

#Getting the label files from the data folder
train_labels = read_labels('data/train-labels-idx1-ubyte.gz')
test_labels = read_labels('data/t10k-labels-idx1-ubyte.gz')


#Reading images files
def read_images(filename):
    #Opening the files and getting the magic number
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("The magic number is:", magic)

        #Getting the number of images in the file
        numImg = f.read(4)
        numImg = int.from_bytes(numImg, 'big')
        print("Number of images:", numImg)

        #Getting the number of rows in the file
        numRow = f.read(4)
        numRow = int.from_bytes(numRow, 'big')
        print("Number of rows:", numRow)

        #Getting the number of columns in the file
        numCol = f.read(4)
        numCol = int.from_bytes(numCol, 'big')
        print("Number of columns:", numCol)

        images = []

        #Looping through the amount of rows and columns and adding them to the images array
        for i in range(numImg):
            rows = []
            for r in range(numRow):
                cols = []
                for c in range(numCol):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                rows.append(cols)
            images.append(rows)
    return images

#Getting the image files from the data folder
train_images = read_images('data/train-images-idx3-ubyte.gz')
test_images = read_images('data/t10k-images-idx3-ubyte.gz')


############## EXERCISE 2 ##############

for rows in train_images[2]:
    for cols in rows:
        print('. ' if cols<= 127 else '# ', end = '')
    print()