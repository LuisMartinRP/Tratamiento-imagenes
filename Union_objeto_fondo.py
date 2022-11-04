#Jorge Alfredo de la Cruz de la Cruz
#Luis Martin Rojas Palacios
import cv2
import numpy as np
img1 = cv2.imread("IMG03a.png")#lee imagen de las flores
img2 = cv2.imread("IMG03b.png")#lee imagen de el fondo
img3 = cv2.imread("IMG03a.png",0)#lee imagen a grises de las flores
umbralizada = np.zeros( img1.shape, dtype=np.uint8)#matriz para guardar la imagen umbralizada
aux = np.zeros( img1.shape, dtype=np.int64)#matriz para guardar la imagen "final"
for f in range( img1.shape[0] ):#for anidados para crear la umbralizada
    for c in range( img1.shape[1] ):
        if img3[f,c]<=30:#si el menor a el umbral
        	umbralizada[f,c]=255#se vuelve blanco
        if img3[f,c]>30:#si es mayor al umbral 
        	umbralizada[f,c]=0#se vuelve negro
for f in range( img1.shape[0] ):#for anidado para sacar obtener la imagen final 
    for c in range( img1.shape[1] ):#.all() develve true o false
    	if (umbralizada[f,c]==255).all():#si es 255 es parte del fondo de las flores
    	    aux[f,c]=img2[f,c]#ponemos el fondo de IMG03b 
    	if (umbralizada[f,c]==0).all():#si es 0 es parte de la flor
    		aux[f,c]=img1[f,c]#ponemos la flor
fin=np.asarray(aux,dtype=np.int64)#conversion para poder mostrar la imagen con imshow
final=np.asarray(fin,np.uint8)#imagen final
cv2.imshow("Imagen umbralizada", umbralizada)#mostrar la umbralizada
cv2.imshow("Imagen final", final)#mostrar la final
img2=cv2.resize(img2, (400,400))
img1=cv2.resize(img1, (400,400))
cv2.imshow('Fondo - Objeto',np.hstack([img2,img1]))#mostrar originales
cv2.waitKey(0)
cv2.destroyAllWindows()
        	