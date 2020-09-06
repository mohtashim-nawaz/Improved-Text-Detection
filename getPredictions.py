import numpy as np 
import cv2
from outlierUtil import check_moire
from noises import bandstop, median
from intensityTransforms import histEqualAdaptive
import matplotlib.pyplot as plt
import os
from pathlib import Path

def utilPrePro1(image):
	"""If periodic noise is present, we apply this set of preprocessing steps"""
	image = bandstop(image)
	image = histEqualAdaptive(image)
	return image

def utilPrePro2(image):
	"""If periodic noise is not present, we apply this set of preprocessing steps"""
	image = median(image)
	image = histEqualAdaptive(image)
	return image

def transformImage(image, count):
	is_noise = check_moire(image)
	if (is_noise):
		image = utilPrePro1(image)
	else:
		image = utilPrePro2(image)

	if(os.path.exists('TransformedImages')):
		cv2.imwrite('TransformedImages/img'+str(count)+'.jpg', image)
	
	else:
		print('Missing directory-"TransformedImages"')

def transformImageUtil(pth, num=1):
	"""Pass the path of directory and number of images to read from it"""
	for i in range(1, num+1):
		img_pth = pth+'/img'+str(i)+'.jpg'
		image = cv2.imread(img_pth, cv2.IMREAD_GRAYSCALE)
		if image is None:
			print('Image could not be loaded...Skipping this image number...')
			continue
		transformImage(image, i)
		
	print("Images saved to 'TransformedImages' directory and are ready to be fetched to PSENet!")