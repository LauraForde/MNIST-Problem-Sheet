import gzip
import numpy as np
import PIL.Image as pil
import os, errno
import shutil

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
        for i in range(20): #numImg
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

#Looping through the amount of rows in the train images set and extracting the third element
for rows in train_images[2]:
    #For the amount of columns in the row print different symbols depeneding on the value
    for cols in rows:
        print('. ' if cols < 127 else '# ', end = '')
    #Move to the next line to show each row on seperate lines on the console
    print()

############## EXERCISE 3 ##############
''' What was done in class
img = pil.fromarray(np.array(train_images[5]))
img = img.convert('RGB')
img.save('2.png') '''

# Making dir adapted from https://stackoverflow.com/questions/1274405/how-to-create-new-folder
path = "PNG/"
dir = os.path.dirname(path)

# If the directory does not exist, make the directory
if not os.path.exists(dir):
    os.makedirs(dir)

def save_as_png(imgToSave, label, folder):

    saveTo = 'PNG/' + folder + '/'
    # Making the sub folder to seperate train and test images files
    dir = os.path.dirname(saveTo)
    if not os.path.exists(dir):
        os.makedirs(dir)

    for i, image in enumerate(imgToSave):
        # Getting the label num for each byte for the name
        labelNo = label[i]
        # Setting the name for the png'
        name = folder + '-' + str(i).zfill(5) + '-' + str(labelNo) + '.png'
        saveFold = saveTo + name

        # Converting the numpy array into png files
        img = pil.fromarray(np.array(image).astype('uint8'))
        img = img.convert('RGB')
        img.save(saveFold, 'PNG')
    # Printing that the PNG files have been saved into whichever folder
    print('Saved as PNG files to the', folder,'folder')

# Calling the method and passing each image set and label set in for converting and saving with the name of the data set
save_as_png(train_images, train_labels, 'train')
save_as_png(test_images, test_labels, 'test')

# Zipping the PNG directory
# Adapted from https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
print("Zipping the PNG folder, this will take a while....")
shutil.make_archive(dir, 'zip', dir)