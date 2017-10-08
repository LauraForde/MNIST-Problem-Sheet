import gzip
import PIL.Image as pil

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