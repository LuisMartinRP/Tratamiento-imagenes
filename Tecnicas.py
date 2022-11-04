#Luis Martin Rojas Palacios
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("kurumiDB.jpg",0)
#Esta funcion sirve
def hist(im):
	hist = cv2.calcHist([im],[0], None, [256], [0,256])
	plt.figure(1)
	plt.subplot(221)
	plt.plot( hist)
	plt.title("Histograma")
	plt.show()
	pass
#Esta funcion sirve
def brillo(im):
	resultado=np.zeros(im.shape,dtype=np.uint8)
	brillo = 50  #El valor va desde -255 hasta 255
	for a in range(im.shape[0]):
		for b in range(im.shape[1]):
			if (im.item(a,b)+brillo)>255:
				resultado[a][b]=255
			elif (im.item(a,b)+brillo)<0:
				resultado[a][b]=0
			else:
				resultado[a][b]=im.item(a,b)+brillo
	return resultado
#Esta funcion sirve
def contraste(im):
	resultado=np.zeros(im.shape,dtype=np.uint8)
	contraste = 10 #El valor va desde -100 hasta 100
	c=(100 + contraste)/100
	c*=c
	for a in range(im.shape[0]):
		for b in range(im.shape[1]):
			r=((im.item(a,b)/255)*c)*255
			if r>255:
				resultado[a][b]=255
			elif r<0:
				resultado[a][b]=0
			else:
				resultado[a][b]=r
	return resultado
#Esta funcion no sirve
def rotacion(im):
	resultado=np.zeros(im.shape,dtype=np.uint8)
	return resultado
#Esta funcion sirve
def desplazamiento(im):
	resultado=np.zeros(im.shape,dtype=np.uint8)
	desplazamientoX=50
	desplazamientoY=50
	for a in range(im.shape[0]):
		for b in range(im.shape[1]):
			if a<desplazamientoX or b<desplazamientoY:
				resultado[a][b]=0
			else:
				resultado[a][b]=im.item(a-desplazamientoX,b-desplazamientoY)
	return resultado
#Esta funcion sirve
def espejo(im):
	resultado=np.zeros(im.shape,dtype=np.uint8)
	for a in range(im.shape[0]):
		for b in range(im.shape[1]):
			resultado[a][b]=im.item(a,im.shape[1]-b-1)
	return resultado
#Esta funcion no sirve
def ampliarreducir(im):
	resultado=np.zeros(im.shape,dtype=np.uint8)
	return resultado

cv2.imshow("Prueba de imagen", image)
hist(image)
#print("Imagen Original",image[0])
imgB=brillo(image)
cv2.imshow("Brillo",imgB)
hist(imgB)
#print("Brillo",imgB[0])
imgC=contraste(image)
cv2.imshow("Contraste",imgC)
hist(imgC)
#print("Contraste",imgC[0])
imgR=rotacion(image)
cv2.imshow("Rotacion",imgR)
#print("Rotacion",imgR[0])
imgD=desplazamiento(image)
cv2.imshow("Desplazamiento",imgD)
#print("Desplazamiento",imgD[0])
imgE=espejo(image)
cv2.imshow("Espejo",imgE)
#print("Espejo",imgE[0])
imgA=ampliarreducir(image)
cv2.imshow("Escala",imgA)
#print("Escala",imgA[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
