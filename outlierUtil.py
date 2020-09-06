import numpy as np
import cv2
import math

def get_iqr_outlier(data):
  """Get number of outliers in array using IQR outlier removal"""
  sort_data=np.sort(data)
  Q1 = np.percentile(data, 25, interpolation = 'midpoint')  
  Q2 = np.percentile(data, 50, interpolation = 'midpoint')  
  Q3 = np.percentile(data, 75, interpolation = 'midpoint') 
  IQR = Q3 - Q1   
  low_lim = Q1 - 1.5 * IQR 
  up_lim = Q3 + 1.5 * IQR 
  cons=3
  low_lim=low_lim*cons
  up_lim=up_lim*cons
  
  outlier=0 
  mask = ((data>up_lim) | (data<low_lim))
  outlier = np.sum(mask) 
  
  return outlier


def num_outliers(image, k=40):
  """Get numberof outliers for an image"""
  img_fft = np.fft.fftn(image)
  img_fft_shift = np.fft.fftshift(img_fft)
  
  img_shape=img_fft_shift.shape
  
  rows=(math.floor(img_shape[0]/k))*k
  cols=(math.floor(img_shape[1]/k))*k
  
  
  d1=math.floor(math.floor(rows/k)*math.floor(cols/k))
  d2=k*k
  
  
  finalarr=np.zeros([d1,d2])
  
  
  num_of_outliers=0;
  
  for i in range(rows):
    for j in range(cols):
      ind=(math.floor(i/k)*math.floor(cols/k))+math.floor(j/k);
      ind=math.floor(ind)
      finalarr[ind,((i%k)*k+j%k)]=img_fft_shift[i,j]
  for i in range(d1):
     num_of_outliers=num_of_outliers+get_iqr_outlier(finalarr[i])

  return num_of_outliers


def get_outliers_list(pth,num):
  """Get outliers for a number of recaptured/dist images as a list"""
  input=pth+'/img'
  i=1
  count_outliers=[]
  while (i<=num):
    pth=input+str(i)+'.jpg'
    image = cv2.imread(pth, cv2.IMREAD_GRAYSCALE)
    k=num_outliers(image)
    count_outliers.append(k)
    i=i+1
  return count_outliers


def check_moire(image):
  count=0
  is_noise = False
  count = num_outliers(image)
  thresh=150
  if(count>=thresh):
    is_noise=True
  return is_noise