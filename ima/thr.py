import numpy as np
import cv2

img = cv2.imread("lena.jpg",0)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

cv2.imwrite("th.png",thresh1)
cv2.imwrite("thinv.png",thresh2)
