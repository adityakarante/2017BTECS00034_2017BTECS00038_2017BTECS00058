import cv2
import numpy as np
img = cv2.imread('lines.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,200)
minLineLength = 0
maxLineGap = 0
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for i in range(len(lines)):
	for j in range(len(lines[i])):
		cv2.line(img,(lines[i][j][0],lines[i][j][1]),(lines[i][j][2],lines[i][j][3]),(0,0,255),2)
cv2.imwrite('output.jpg',img)