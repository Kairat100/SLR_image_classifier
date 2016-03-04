import numpy as np
import cv2
import cv2.cv as cv

hog = cv2.HOGDescriptor("hog.xml")
im = cv2.imread("./frames/a1111.png")
h = hog.compute(im)

print h

cv2.imshow("hog", im)
cv2.waitKey(0)