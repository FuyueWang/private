import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def read_file_lines(filename):
    #输入文件名，输出每行为一个元素的list
    line=[line.rstrip() for line in open(filename)]
    return line 

# file1 = read_file_lines('1.txt')

def lines_to_image(file_lines):
    #输入没行为一个元素的list，输出一个0~1之间的图像矩阵
    #将原格式list中的string分开并转化成int，然后再转化成array，再reshape
    image_list=list(map(lambda x: list(map(int,x.split())),file_lines[1:]))
    image_array=np.array(image_list).reshape(int(file_lines[0].split()[0]),int(file_lines[0].split()[1]),3)
    # Make sure to call astype like this on the 3-dimensional array
    # you produce, before returning it.
    return image_array.astype(np.uint8)


def show_images(images, ncols=2, figsize=(10, 7), **kwargs):
    """
    Shows one or more color images.
    
    images: Image or list of images.  Each image is a 3-dimensional
            array, where dimension 1 indexes height and dimension 2
            the width.  Dimension 3 indexes the 3 color values red,
            blue, and green (so it always has length 3).
    """
    def show_image(image, axis=plt):
        plt.imshow(image, **kwargs)
        
    if not (isinstance(images, list) or isinstance(images, tuple)):
        images = [images]
    images = [image.astype(np.uint8) for image in images]
    
    nrows = math.ceil(len(images) / ncols)
    ncols = min(len(images), ncols)
    
    plt.figure(figsize=figsize)
    for i, image in enumerate(images):
        axis = plt.subplot2grid(
            (nrows, ncols),
            (i // ncols,  i % ncols),
        )
        axis.tick_params(bottom='off', left='off', top='off', right='off',
                         labelleft='off', labelbottom='off')
        axis.grid(False)
        show_image(image, axis)


transformed = np.array([12, 37, 65, 89, 114, 137, 162, 187, 214, 240, 250])

def expand_image_range(image):
    for i in range(len(transformed)):
        image[image==i]=transformed[i]
    return image

    filenames = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt','6.txt', '7.txt', '8.txt', '9.txt', '10.txt']


def reveal_file(filename):
    line=read_file_lines(filename)
    image_arr=lines_to_image(line)
    image=expand_image_range(image_arr)
    return image


expanded_images = ...

show_images(expanded_images, ncols=5)
per=np.array([prin(reveal_file(i)) for i in filenames])
expanded_images=[reveal_file(i) for i in filenames]
def prin(image):
    image1=image.reshape(image.shape[0]*image.shape[1],3)
    row=np.argmax(image1,1)
    image1.sort(1)
    per=np.bincount(row[np.argmax(image1,1)==2])/image1.shape[0]
    return per
