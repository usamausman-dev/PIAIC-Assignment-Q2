from PIL import Image
import os
import matplotlib.pylab as plt
import numpy as np

rootDir = '.'
imageList=[]
for dirName,subDirList,fileList in os.walk(rootDir):
    print('found directory %s' %dirName)
    imageList=imageList+fileList
counter=1

for i in imageList:
    if i.endswith('.jpg') or i.endswith('.jpeg'):
        im=plt.imread(i)
        image= Image.open(i)
        newImage=image.resize((300,300))
        newImage.save('new{}.jpg'.format(counter))
        counter+=1