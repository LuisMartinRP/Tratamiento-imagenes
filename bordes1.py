import cv2
import numpy as np
img1 = cv2.imread("Bordes.png",0)
bordesh = np.zeros( img1.shape, dtype=np.int64)
bordesv = np.zeros( img1.shape, dtype=np.int64)
fil=img1.shape[0]
col=img1.shape[1]
for f in range( fil ):
    for c in range( col-1 ):
        if img1[f,c]==0:
            if (img1[f,c]!=img1[f,c+1]).all():
                bordesv[f,c]=img1[f,c]
        if img1[f,c]==255:
            if (img1[f,c]!=img1[f,c+1]).all():
                bordesv[f,c]=img1[f,c+1]
        if (img1[f,c]==img1[f,c+1]).all():
            bordesv[f,c]=255                
for f in range( fil-1 ):
    for c in range( col ):
        if img1[f,c]==0:
            if (img1[f,c]!=img1[f+1,c]).all():
                bordesh[f,c]=img1[f,c]
        if img1[f,c]==255:
            if (img1[f,c]!=img1[f+1,c]).all():
                bordesh[f,c]=img1[f+1,c]
        if (img1[f,c]==img1[f+1,c]).all():
            bordesh[f,c]=255

borhori=np.asarray(bordesh,dtype=np.int64)
bordehorizontal=np.asarray(borhori,np.uint8)

borvert=np.asarray(bordesv,dtype=np.int64)
bordevertical=np.asarray(borvert,np.uint8)

cv2.imshow("Bordes horizontales", bordehorizontal)
cv2.imshow("Bordes verticales", bordevertical)
cv2.imshow('Imagen original',img1)
cv2.waitKey(0)
cv2.destroyAllWindows() 