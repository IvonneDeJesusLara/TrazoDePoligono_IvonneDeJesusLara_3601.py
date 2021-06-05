import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt


def puntos():
    n= int(input("INTRODUCE EL NUMERO DE LADOS "))
    x1= 10
    y1=10
    Bresenhams(n)

def Bresenhams(n):
    rad = 10
    centroX = 10
    centroY = 10
    x1=0
    lados= n
    k=lados
    angulo = np.linspace(0, 2 *np.pi, lados+1)
    i=0
    p=0
    x = rad * np.cos(angulo) + centroX
    y = rad * np.sin(angulo) + centroY
    for i in range(k):
        for p in range(x.size):  
            #plt.plot(x[i] ,y[i+1], "sm")  
            plt.plot(x,y, "sb")   
            p =p + 1 
        
        i = i + 1
    print("\n Coordenadas X \n")
    print(x)
    print("\n Coordenadas Y \n")
    print(y)
    #TITULO DE LA PANTALLA 
    plt.title("POLIGONOS REGULARES")
   
    #print(x)
    #MUESTRA EN LA GRAFICA LA LEYENDA EJE X
    plt.xlabel("EJE X")
    
    #print("Coordenadas Y ")
    #print(y)
    #MUESTRA EN LA GRAFICA LA LEYENDA EJE Y
    plt.ylabel("EJE Y")
    #PERMITE DAR UNA VISION DEL PLANO IGUAL
    plt.gca().set_aspect('equal')
    #EL PLANO LO MUESTRA CON CUADROS
    plt.grid()

    plt.show()

if __name__=='__main__':
    puntos()
    
    
    
