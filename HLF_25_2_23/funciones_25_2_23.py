import numpy as np

import random

class Barco:

    def __init__(self,eslora,posiciones):

        self.posiciones = posiciones
        self.eslora = eslora


def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, "_")


def colocar_barco(barco, tablero):
    for casilla in barco.posiciones:
        tablero[casilla]="B"
    return tablero


def crear_barco_random(eslora):

    barco = Barco(eslora, [])
    
    fila_a = random.randint(0,9)
    columna_a = random.randint(0,9)
    orientacion = random.choice(["S","O","E","N"])
    barco.posiciones = [(fila_a, columna_a)]

    while len(barco.posiciones) < barco.eslora:

    
        match orientacion:
            case "O":
                
                if columna_a - (barco.eslora-1)>=0:
                     
                     columna_a -= 1   
                else:
                    orientacion = "E"
                    
                    continue
                        
                     
            case "E":
                
                if columna_a + (barco.eslora-1)<=9:
                    
                    columna_a += 1
                else:
                    orientacion="O"
                    
                    continue
            case "S":
                    
                if fila_a + (barco.eslora-1)<=9:
                    fila_a += 1
                else:
                    orientacion="N"
                    
                    continue

            case "N":
                    
                if fila_a - (barco.eslora-1)>=0:
                    
                    fila_a -= 1 
                else:
                    orientacion="S"
                    
                    continue
                    
                    
        barco.posiciones.append((fila_a, columna_a))
       

    return barco

def comprobar_barco(barco,tablero):
    for i in barco.posiciones:
        if tablero[i] == "B":
            print("hay barco en esa posicion")
            return False                  
    return True


def comprobar_disparo(disparo,tablero):
    if tablero[disparo] == "B":

        print("hay barco en esa posicion")
        return True
    
    else:
        
        print("fallo")
        
    return False

def crear_y_colocar_barco_valido(eslora, tablero):
    barco= crear_barco_random(eslora)
    es_barco_valido = comprobar_barco(barco,tablero)

    while es_barco_valido == False:   #### Aquí estoy diciendo que mientras barco_es_válido sea False siga haciendo el bucle hasta que se convierta en True
        barco= crear_barco_random(eslora)
        es_barco_valido = comprobar_barco(barco,tablero)
    colocar_barco(barco,tablero)

def crear_tablero_relleno():
    barcos_a_insertar = [(4,1), (3,2),(2,3), (1,4)] 
    tablero = crear_tablero()
    for i in barcos_a_insertar:       
        for x in range(i[1]):
            crear_y_colocar_barco_valido(i[0], tablero)

    return tablero

def pedir_coordenadas():
    disparo_jugador_x= int(input("Por favorintroduce tu coordenada de fila: "))
    disparo_jugador_y= int(input("Por favorintroduce tu coordenada de columna: "))
    return (disparo_jugador_x,disparo_jugador_y)



