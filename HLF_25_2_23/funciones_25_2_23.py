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
    disparo_jugador_x= int(input("Por favorintroduce tu coordenada x: "))
    disparo_jugador_y= int(input("Por favorintroduce tu coordenada y: "))
    return (disparo_jugador_x,disparo_jugador_y)

PUNTUACION_MAXIMA = 2
marcador = {            ###diccionario para establecer un marcador de máquina y un marcador de jugador
    'jugador': 0,
    'maquina': 0}

#def disparar_jugador(tablero_maquina,tablero_disparos_jugador_1):
#
#    while marcador["jugador"] < PUNTUACION_MAXIMA:
#            disparo_jugador = pedir_coordenadas()
#            comprobar_jugador = comprobar_disparo(disparo_jugador, tablero_maquina)
#            if comprobar_jugador == True:
#                tablero_disparos_jugador_1[disparo_jugador] = "X"
#                marcador["jugador"] += 1
#                print("Tocado")
#            else:
#                tablero_disparos_jugador_1[disparo_jugador] = "A"
#                print("Agua")
#            break
#    
#def disparar_maquina(tablero_maquina,tablero_disparos_maquina):
#    while marcador["maquina"] < PUNTUACION_MAXIMA:
#        disparo_maquina = (random.randint(0, 9), random.randint(0, 9))
#        print('disparo maquina', disparo_maquina)
#        comprobar_maquina = comprobar_disparo(disparo_maquina, tablero_maquina)
#        if comprobar_maquina:
#            tablero_disparos_maquina[disparo_maquina] = "X"
#            marcador["maquina"] += 1
#            print("Tocado por maquina")
#            print('disparos maquina', tablero_disparos_maquina)
#        else:
#            tablero_disparos_maquina[disparo_maquina] = "A"
#            print("Agua maquina")
#        break