import numpy as np
import random

def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, "_")

barcos_no_validos=[]

barcos_validos=[]

casilla_o= "B"

fila_a = random.randint(0,9)
columna_a = random.randint(0,9)
orientacion = random.choice(["S","O","E","N"])

barco = [(fila_a, columna_a)]


tablero=crear_tablero()
print(tablero)



def colocar_barco(barco, tablero):
    for casilla in barco:
        if tablero[casilla]=="B" :
            barco=[]
        else:
            tablero[casilla] = "B"
    return tablero



def crear_barco_random(eslora,tablero):


    fila_a = random.randint(0,9)
    columna_a = random.randint(0,9)
    orientacion = random.choice(["S","O","E","N"])
    barco = [(fila_a, columna_a)]

    while len(barco) < eslora:

    
        match orientacion:
            case "O":
                columna_a -= 1 # columna_a = columna_a - 1
            case "E":
                columna_a += 1
            case "S":
                fila_a += 1
            case "N":
                fila_a -= 1
        barco.append((fila_a, columna_a))
    
    colocar_barco(barco,tablero)



    return tablero        
        

barco=(crear_barco_random(5,tablero))
print(barco)