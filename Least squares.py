import numpy as np
import cv2 as cv2
import imutils
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(r"C:\Users\chand\Downloads\ball_video2.mp4")
if cap.isOpened() == False:
    print('Error in opening the file')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('The number of frames in the video is ' + str(length))
x = []
y = []
count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray_image, 200, 255,cv2.THRESH_BINARY_INV)
    #moments of this binary image
    M = cv2.moments(thresh)
       
    #calculate the coordinates of the center
    cX = int(M["m10"]/M["m00"])
    cY = -int(M["m01"]/M["m00"])
       
    x.append(cX)
    y.append(cY)
    print(x)
    ret, frame =cap.read()
    print("success", ret)
    count+1
       
x2 = np.power(x,2)
X = np.column_stack([x2,x,np.ones(len(x))])
Y = np.row_stack(y)
E = np.matmul(X.T,X)
F = np.linalg.inv(E)
G = np.matmul(F,X.T)
B = np.matmul(G,Y)

print(B)

line = np.matmul(X,B)

print(x)
print(y)
plt.scatter(x,y)
plt.plot(x, line, 'g')
plt.show()