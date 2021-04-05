import cv2 as cv #import the cv library
import sys #import the sys library
img = cv.imread('beeg yoshi.png') #sets img to the png stored on pi
res = cv.resize(img,None,fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC) # resize the img
if img is None: #check if img exists
 sys.exit("The image could not be read.") #exit and display text
cv.imshow("OpenCV Image", img) #names the window and opens img
cv.waitKey(0) #wait for key press 
cv.destroyAllWindows() #close window