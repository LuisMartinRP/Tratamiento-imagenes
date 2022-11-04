#Luis Martin Rojas Palacios
import cv2
import numpy as np
xf=0#coordenada en x mas a la derecha
yf=0#coordenada en y mas a la derecha
con=0#contador para encontrar la yi
img = cv2.imread("patos.png",0)#cargamos en grises la imagen
xi=857#coordenada en y mas  ala izquierda
umbralizada = np.zeros( img.shape, dtype=np.uint8)#creamos matriz para imagen 
for f in range( img.shape[0] ):#for para umbralizar
    for c in range( img.shape[1] ):
        if img[f,c]<10:#si es menor al umbral
        	umbralizada[f,c]=255#se vuelve blanco
        	if con==0:#para encontrar y inicial
        		yi=f#solo entra con el primer pixel blanco mas arriba de la imagen  se lo asigna
        		con+=1#para que no cambie el valor de yi
        	if f>yf:#para encontrar la y mas abajo
        		yf=f
        	if c>xf:#para encontrar la x mas a la derecha
        		xf=c
        	if c<xi:#para encontarr la x mas a la izquierda
        		xi=c
        if img[f,c]>=10:#si es mayor al umbarl
        	umbralizada[f,c]=0#se vuelve negro
img2=cv2.imread("patos.png")#imagen a color
'''cv2.line(img2,(xi,yi),(xf,yi),(255,0,0),1)
cv2.line(img2,(xi,yi),(xi,yf),(255,0,0),1)
cv2.line(img2,(xf,yi),(xf,yf),(255,0,0),1)
cv2.line(img2,(xi,yf),(xf,yf),(255,0,0),1)'''
for f in range( img2.shape[0] ):#para trazar la linea de arriba
    for c in range( img2.shape[1] ):
    	if f==yi:
    		if c>=xi:
    			if c<=xf:
	    			img2.itemset((f, c, 0), 255)
	    			img2.itemset((f, c, 1), 0)
	    			img2.itemset((f, c, 2), 0)
for f in range( img2.shape[0] ):#para trazar la linea de la izquierda
    for c in range( img2.shape[1] ):
	    if c==xi:
	    	if f>=yi:
	    		if f<=yf:
	    			img2.itemset((f, c, 0), 255)
	    			img2.itemset((f, c, 1), 0)
	    			img2.itemset((f, c, 2), 0)
for f in range( img2.shape[0] ):#para trazar la linea de la derecha
    for c in range( img2.shape[1] ):
	    if c==xf:
	    	if f>=yi:
	    		if f<=yf:
	    			img2.itemset((f, c, 0), 255)
	    			img2.itemset((f, c, 1), 0)
	    			img2.itemset((f, c, 2), 0)
for f in range( img2.shape[0] ):#para trazar la linea de abajo
    for c in range( img2.shape[1] ):
	    if f==yf:
    		if c>=xi:
    			if c<=xf:
	    			img2.itemset((f, c, 0), 255)
	    			img2.itemset((f, c, 1), 0)
	    			img2.itemset((f, c, 2), 0)
print("",xi,"" ,yi,"", xf,"" ,yf) #muestra las coordenadas encontradas
cv2.imshow("Imagen umbralizada", umbralizada)#muestra la imagen umbralizada
cv2.imshow("Imagen con lineas", img2)#muetra la imagen con lineas
cv2.waitKey(0)
cv2.destroyAllWindows()