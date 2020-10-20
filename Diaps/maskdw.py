import cv2
import numpy

img = cv2.imread("15.png")
g = cv2.imread("15_m.png",0)


for i in range(img.shape[0]):
    for k in range(img.shape[1]):
        if g[i,k]==255:
            img[i,k] = 255,255,0

cv2.imwrite("mkdw.png",img)

