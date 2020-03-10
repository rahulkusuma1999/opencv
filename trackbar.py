import cv2
import numpy as np
def nothing(x):
    print(x)

img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')   #to name the window

cv2.createTrackbar('B','image',0,255,nothing)  #to create trackabr
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)


switch = '0:off\n 1:on'
cv2.createTrackbar(switch,'image',0,1,nothing)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break


    b=cv2.getTrackbarPos('B','image')  #to get the pos of trackbar
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')


    img[:]=[b,g,r] #to apply current values to the trackbar
cv2.destroyAllWindows()
