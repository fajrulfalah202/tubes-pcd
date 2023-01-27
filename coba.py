
import cv2
import numpy as np

 
img = cv2.imread('target1.png')
blur = cv2.medianBlur(img,5)
 
cv2.imshow('mas', blur)

cv2.imwrite('simpan.png', blur)
cv2.waitKey(0)
        