# -*- coding: utf-8 -*-
"""day6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rd6BGzRYFfPA4URLwzvWIZy1UQ48v1UX
"""

!pip install tensorflow

import tensorflow as tf
import matplotlib as mpl
import glob
import cv2
import numpy as np

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from matplotlib.pyplot import imread, imshow, subplots, show
from keras.preprocessing.image import save_img

#sending images with seleceted augmentation here
def gorsellestirme(data_generator, indx, images):
    data_generator.fit(images)
    image_iterator = data_generator.flow(images)
    imgd = image_iterator.next()[0].astype('int')
    save_img("/content/result/image%d.jpg"%(indx), imgd)
    return imgd

#selecting folder of images and augmentation type
i = 0
for img in glob.glob('/content/*.jpg'):
  image = imread('/content/test%d.jpg'%(i))
  images = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
  #data_generator = ImageDataGenerator(channel_shift_range=120.0)
  data_generator = ImageDataGenerator(vertical_flip=True)
  gorsellestirme(data_generator, i, images)
  if(i < 7):
   i += 1

#testing augmentations on images one by one
i = 0
image = imread('/content/test%d.jpg'%(i))
images = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
#data_generator = ImageDataGenerator(channel_shift_range=120.0)
#data_generator = ImageDataGenerator(vertical_flip=True)
data_generator = ImageDataGenerator(brightness_range=(0.1, 0.9))
img_o= gorsellestirme(data_generator, i, images)
save_img('/content/result/image1.jpg', img_o)
imshow(img_o)

