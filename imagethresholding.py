import cv2
import numpy as np

img=cv2.imread('C:\Users\Keshav Goswami\Desktop\Softwares\opencv\IRONman\IRONMAN.jpg')
retval, threshold=cv2.threshold(img, 12, 255,cv2.THRESH_BINARY)
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval1, threshold1=cv2.threshold(grayscaled, 12, 255,cv2.THRESH_BINARY)
gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
retval2, outsu=cv2.threshold(grayscaled, 12, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold1',threshold1)
cv2.imshow('gaus',gaus)
cv2.imshow('outsu',outsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
