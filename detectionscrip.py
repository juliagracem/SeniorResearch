# -*- coding: utf-8 -*-
"""
Created on Fri May 1 13:19:10 2020

@author: Julia
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 6 17:13:35 2020

@author: Julia
"""

import cv2


def runtest(imageName,windowName):
    numFacesDetected=0
    cascadetest=cv2.CascadeClassifier('cascade.xml') #Read in the cascade file
    testImage=cv2.imread(imageName) # Read in the testing image
    gray=cv2.cvtColor(testImage,cv2.COLOR_BGR2GRAY)
    face=cascadetest.detectMultiScale(gray, 1.01,7) #use the cascade to detect faces
    for(x,y,w,h) in face:
        testImage=cv2.rectangle(testImage,(x,y),(x+w,y+h),(0,0,255),2) #draw a red rectangle around any detected face in the test image
        numFacesDetected=numFacesDetected+1
    print(f"There were {numFacesDetected} faces detected in {imageName}")
    cv2.namedWindow(windowName) #name the window so multiple windows can be opened in succession
    testImage=cv2.resize(testImage, (800,700)) #change the image size. This isn't necessary but the images were openeing too big for my screen. this can be changed or deleted based on screen size
    cv2.imshow(windowName,testImage) #open the image with the rectangle
    cv2.waitKey()
    

for i in range(1,46): # This lets us iterate through all 45 testfiles. Because the loop structure doesn't include the last number it should be the last number file plus 1 so that it will reed the last file
    imageName='_ ({}).jpg'.format(i)
    windowName="Window{}".format(i)
    runtest(imageName, windowName)