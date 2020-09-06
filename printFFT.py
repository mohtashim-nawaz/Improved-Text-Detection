# importing the libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
from randList import getRandomList


def getFFT(pth):
	""" Finds and plots the Fourier Transform of the image """
	image = cv2.imread(pth, cv2.IMREAD_GRAYSCALE)
	f = np.fft.fft2(image)
	shifted = np.fft.fftshift(f)
	mag_spctrm = 20*np.log(np.abs(shifted))
	plt.figure(figsize=(20,6))
	plt.subplot(121), plt.imshow(image, cmap='gray')
	plt.title("Image")
	plt.subplot(122), plt.imshow(mag_spctrm)
	plt.title("Fourier Transform")


def getFFTUtil(num, pth ,mx):
	"""For finding the FFT of a number of images selected randomly out of some given images, path to directory,
	total number of images in directory and number of images to be selected randomly should be passed as parameters."""
	if(num>mx):
		print("Maximum number of images available is "+ str(mx))
		return
	lst = getRandomList(num, 1, mx, 1)
	for i in lst:
		pth = pth+'img'+str(i)+'.jpg'
		getFFT(pth)

