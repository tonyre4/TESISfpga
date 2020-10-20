import cv2 
import numpy as np

ot = cv2.imread("otsu.png",0)
mk = cv2.imread("mask.png",0)
man = cv2.imread("amano.png",0)


ori = cv2.imread("orig.png")

m = ori.copy()
m[:,:,2] = mk

cv2.imwrite("orimk.png",m)

m2 = ori.copy()
m2[:,:,2] = ot
cv2.imwrite("oriot.png",m2)

m3 = ori.copy()
m3[:,:,2] = man
cv2.imwrite("origman.png",m3)


