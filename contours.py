import cv2
img=cv2.imread('img.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("numbers of contours = "+str(len(contours)))     # displays number of contours
print(contours[0])     # it displays all the contours which are numpy arrays in the image
cv2.drawContours(img,contours,-1,(0,255,0),3)    # to draw all the contours we give -1
cv2.imshow('image',img)
cv2.imshow('image gray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()