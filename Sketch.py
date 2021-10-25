import cv2
import matplotlib.pyplot as plt
from tkinter.filedialog import *

photo = askopenfilename()
img = cv2.imread(photo)
grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#plt.imshow(img)
#plt.axis(False)
#plt.show()

#plt.imshow(img[:,:,::-1])
#plt.axis(False)
#plt.show()

print(img.shape)
#cv2.imshow('example',img)
#cv2.imshow('Grey',grey_img)
invert_img=cv2.bitwise_not(grey_img)
#cv2.imshow('Invert',invert_img)
blurr_img=cv2.GaussianBlur(img, (41,41),0)
#cv2.imshow('BLURIMG',blurr_img)
blur_img=cv2.GaussianBlur(invert_img, (31,31),0)
#cv2.imshow('Blur',blur_img)
invblur_img=cv2.bitwise_not(blur_img)
#cv2.imshow('INVBLUR',invblur_img)
sketch_img=cv2.divide(grey_img,invblur_img, scale=200.0)
cv2.imshow('Sketch',sketch_img)

width = 400
height = 420
dim = (width, height)

# resize image
resized = cv2.resize(sketch_img, dim, interpolation = cv2.INTER_AREA)
#cv2.imshow('sketch',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

status = cv2.imwrite('C:/Users/aryan/Downloads/workforce/resised1.png',sketch_img)
 
print("Image written to file-system : ",status)

print(resized.shape)
cv2.waitKey(0)