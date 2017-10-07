import gzip

#f = gzip.open('data/t10k-labels-idx1-ubyte.gz', 'rb')
# changing to add method so you can use more than one file, to read both label files

def read_labels_from_file(filename):
    # new way of dealing with files in python
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is:", magic)

        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("Number of labels:", nolab)

        '''labels = []

        # reading byte and converting in label
        for i in range(nolab):
        labels.append(f.read(1))'''

        # short hand of doing the above code
        # adding labels from file to array
        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big') for label in labels]

    return labels

train_labels = read_labels_from_file('data/train-labels-idx1-ubyte.gz')
test_labels = read_labels_from_file('data/t10k-labels-idx1-ubyte.gz')

def read_images_from_file(filename):
    # new way of dealing with files in python
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is:", magic)

        noimg = f.read(4)
        noimg = int.from_bytes(noimg, 'big')
        print("Number of images:", noimg)

        norow = f.read(4)
        norow = int.from_bytes(norow, 'big')
        print("Number of rows:", norow)

        nocol = f.read(4)
        nocol = int.from_bytes(nocol, 'big')
        print("Number of columns:", nocol)

        images = []

        for i in range(noimg):
            rows = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                rows.append(cols)
            images.append(rows)
    return images

train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')
test_images = read_images_from_file('data/t10k-images-idx3-ubyte.gz')

#import numpy & pil

for row in train_images:
    for col in row:
        print('.' if col <= 127 else '#', end = '.')
    print()

import PIL.Image as pil
img = pil.fromarray(np.array(train_images[4999]))
img = img.convert('RGB')
img.show()
img.save('2.png')