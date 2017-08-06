import cv2
import numpy as np
from random import randint
img=np.zeros((1024,1024,3), np.uint8)
imgp=np.zeros((1024,1024,3), np.uint8)
imgq=np.zeros((922,922,3), np.uint8)
colour=[(0,0,0),(255,255,255),(255,255,0),(255,0,255),(0,255,255),(255,0,0),(0,255,0),(0,0,255)]

#this part will create random values that will be used to make a star map
m=[]
for i in range (1, 1000):

    x= randint(10,1010)#x coord of the star
    y= randint(10,1010)#y coord of the star
    r=randint (1, 5)# radius of the star
    c=randint(1,7)
    img1= cv2.circle(imgp,(x,y),r,(colour[c]),-1)
    img2= cv2.circle(imgq,(int(x*0.9),int(y*0.9)),r,(colour[c]),-1)

    m.append([x,y,r,c])
font = cv2.FONT_HERSHEY_COMPLEX
#img1 = cv2.putText(img1,'JUSC PRESENTS TECHKNOW-CRADLE 2017',(10,1010),font,4,(255,255,255),2,cv2.LINE_AA)
#img1 = cv2.putText(img1,'IN THE MAIN SCREEN, USE a,s,d,w TO MOVE',(10,1010),font,4,(255,255,255),2,cv2.LINE_AA)
#TODO the part of adding text is commented out. Check why it's not working
#cv2.namedWindow("BigBang",cv2.WINDOW_NORMAL)
cv2.imshow("BigBang",img1)
cv2.waitKey(0)
cv2.imshow("BigBang",img1)
cv2.waitKey(0)
originx=20
originy=20

while True:

    for j in m:
        img= cv2.circle(img,((j[0]),(j[1])),j[2],(colour[j[3]]),-1)

    for j in m:
        img= cv2.circle(img,(int(j[0]*0.9+originx),int(j[1]*0.9+originy)),j[2],(colour[j[3]]),-1)
    cv2.imshow("BigBang",img)
    k=cv2.waitKey(0)
    if k==ord("a"):
        originx-=1
    if k==ord("w"):
        originy-=1
    if k==ord("d"):
        originx+=1
    if k==ord("s"):
        originy+=1
    if k==ord("q"):
        break
    img= np.zeros((1024,1024,3), np.uint8)
cv2.destroyAllWindows()
