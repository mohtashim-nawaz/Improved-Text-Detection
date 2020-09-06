import numpy as np
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
from randList import getRandomList

def getHistImage(pth):
	""" This function print the histogram of Grayscale image and the grayscale image itself """
	image = cv2.imread(pth, cv2.IMREAD_GRAYSCALE)
	plt.figure(figsize=(20,6))
	ax1 = plt.subplot(1,2,1)
	ax2 = plt.subplot(1,2,2)
	sns.distplot(image, hist=True, ax=ax1)
	plt.imshow(image, cmap='gray')



def histUtil(num, pth, mx):
	""" This function randomly selects 'num' images randomly to be fed to getHistImage(), assuming images are named as .../img1.jpg, img2.jpg"""
	if(num>mx):
		print("Maximum number of images available is "+str(mx))
		return
	lst = getRandomList(num, 1, mx, 1)
	for i in lst:
		pth = pth+'img'+str(i)+'.jpg'
		getHistImage(pth)

