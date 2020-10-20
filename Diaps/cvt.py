import cv2
import numpy

img = cv2.imread("15.png")
g = cv2.imread("15.png",0)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h,s,v = cv2.split(hsv)

cv2.imwrite("h.png",h)
cv2.imwrite("s.png",s)
cv2.imwrite("v.png",v)
cv2.imwrite("g.png",g)
