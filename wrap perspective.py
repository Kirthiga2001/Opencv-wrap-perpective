import cv2
import  numpy as np

i=cv2.imread("cards.jpg")
w,h=250,350
#p1=np.float32([[760,160],[901,473],[901]])
p1=np.float32([[111,219],[287,188],[154,482],[352,440]])
p11=np.float32([[219,68],[19,150],[372,369],[162,461]])

p2=np.float32([[0,0],[w,0],[0,h],[w,h]])
ma=cv2.getPerspectiveTransform(p1,p2)
io=cv2.warpPerspective(i,ma,(w,h))
cv2.imshow("Kingspade",io)
cv2.imshow("Original",i)
cv2.waitKey(0)