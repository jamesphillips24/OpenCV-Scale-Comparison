import numpy
import cv2
import random
import numpy as np

#Program I made that shows a comparison between two images
#One uses regular opencv scaling and the other uses interpolation
#Mostly made this to get the basics of opencv

#Variable to make scale x scale images
scale = 500

#Declare initial image, numpy array of zeroes, and scalars for interpolation
dog = cv2.imread("test.jpg", 0)
comparison = np.zeros((scale, scale*2), dtype=np.uint8)
dogfx = scale/dog.shape[0]
dogfy = scale/dog.shape[1]

#scale the images
dogInterp = cv2.resize(dog, (0, 0), fx=dogfx, fy=dogfy, interpolation=cv2.INTER_AREA)
dogResize = cv2.resize(dog, (scale, scale))

#Fill each side of zero array
comparison[:, :scale] = dogInterp
comparison[:, scale:] = dogResize

cv2.imshow("comparison.jpg",comparison)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Conclusion is that as you scale the image down more,
#the normal scale gets grainier than the interpolation