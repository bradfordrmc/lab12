import numpy as np
import cv2 as cv
import sys
img1 = cv.imread('bezos.jpg')
img2 = cv.imread('turtle.jpeg')
alpha = 0.5
dst = cv.addWeighted(img1,1-alpha,img2,alpha,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()