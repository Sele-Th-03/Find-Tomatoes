#Importing libraries
import cv2 
import numpy as np
from time import sleep

n=0
img=cv2.imread("salad.jpg")

#Blurring
blur = cv2.bilateralFilter(img,9,75,75)

#Converting to HSV
hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

#Applying the mask, for the red color range, to the original image
lower=np.array([0,200,200])
upper=np.array([9,255,255])
mask=cv2.inRange(hsv,lower,upper)
result=cv2.bitwise_and(img,img,mask=mask)

#Converting to grayscale
gray=cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)

#Blurring
blur=cv2.GaussianBlur(gray,(7,7),3)

#Detecting and drawing contours
canny=cv2.Canny(blur,50,50)
cnt,h=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for c in cnt:
	area=cv2.contourArea(c)
	if area>20:
		cv2.drawContours(img,c,-1,(255,0,0),3)
		n+=1

#Printing the number of contours found
print("n:"+str(n))

#Displaying the final image with contours
cv2.imshow("img",img)
cv2.waitKey(0)