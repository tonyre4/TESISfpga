import cv2
import numpy as np

g = cv2.imread("amano.png",0)
ot = cv2.imread("otsu.png",0)
mk = cv2.imread("mask.png",0)

r1 = g-ot
r2 = g-mk

px = g.shape[0]*g.shape[1]
nz1 = np.count_nonzero(r1)
nz2 = np.count_nonzero(r2)

p1 = (px-nz1)*100/px
p2 = (px-nz2)*100/px

print("otsu percent: %f" % p1 )
cv2.imshow("a",r1)
cv2.waitKey(0)
print("mask percent: %f" % p2 )
cv2.imshow("a",r2)
cv2.waitKey(0)
