import numpy as np
import cv2


def modifiedPowerLaw(img):
  img=np.uint8(cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX))
  a,b = img.shape
  img = img.flatten()
  mask1 = (img<128)
  mask2 = (img>=128)
  img[mask1] = ((img[mask1]/127)**(5))*img[mask1]
  img[mask2] = (((img[mask2]-128)/127)**0.2)*img[mask2]
  img = img.reshape(a,b)
  return img 

def histEqual(img):
  img=np.uint8(cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX))
  return cv2.equalizeHist(img)

def histEqualAdaptive(img):
  img=np.uint8(cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX))
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
  return clahe.apply(img)