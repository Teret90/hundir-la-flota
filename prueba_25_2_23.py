import numpy as np
import random

class Barco:

    def __init__(self,eslora,posiciones):

        self.posiciones = posiciones
        self.eslora = eslora


jugador_1 = "jugador 1"

maquina = "maquina"

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
    #fila_inicio=fila_a
    #columna_inicio = columna_a
    orientacion = random.choice(["S","O","E","N"])
    barco.posiciones = [(fila_a, columna_a)]

    

    while len(barco.posiciones) < barco.eslora:

    
        match orientacion:
            case "O":
                
                if columna_a - (barco.eslora-1)>=0:
                     columna_a -= 1   
                else:
                    orientacion = "E"
                    print(orientacion)
                    continue
                        
                     
            case "E":
                
                if columna_a + (barco.eslora-1)<=9:
                    columna_a += 1
                else:
                    orientacion="O"
                    print(orientacion)
                    continue
            case "S":
                    
                if fila_a + (barco.eslora-1)<=9:
                    fila_a += 1
                else:
                    orientacion="N"
                    print(orientacion)
                    continue

            case "N":
                    
                if fila_a - (barco.eslora-1)>=0:
                    fila_a -= 1 
                else:
                    orientacion="S"
                    print(orientacion)
                    continue
                    
                    
        barco.posiciones.append((fila_a, columna_a))
       

    return barco


def comprobar_barco(barco,tablero):
    for i in barco.posiciones:
        if tablero[i] == "B":

            print("hay barco en esa posicion")
            return False
            
            
            
        else:
            
            print("barco ok")
            
    return True

def comprobar_disparo(disparo,tablero):
    if tablero[disparo] == "B":

        print("hay barco en esa posicion")
        return True
        
        
        
    else:
        
        print("barco ok")
        
    return False

            
           
def crear_y_colocar_barco_valido(eslora, tablero):
    barco= crear_barco_random(eslora)
    es_barco_valido = comprobar_barco(barco,tablero)

    while es_barco_valido == False:   #### Aquí estoy diciendo que mientras barco_es_válido sea False siga haciendo el bucle hasta que se convierta en True
        barco= crear_barco_random(eslora)
        es_barco_valido = comprobar_barco(barco,tablero)
    colocar_barco(barco,tablero)
    
# 4 - 1x
# 3 - 2x
# 2 - 3x
# 1 - 4x
    
### hacemos una lista de tuplas donde la 0ª posicion de la tupla es la eslora y la 1ª posición cantidad de barcos a crear



def crear_tablero_relleno():
    barcos_a_insertar = [(4,1), (3,2),(2,3), (1,4)] 
    tablero = crear_tablero()
    for i in barcos_a_insertar:       
        for x in range(i[1]):
            crear_y_colocar_barco_valido(i[0], tablero)

    return tablero

"""Recorremos la lista "barcos_a_insertar"; Creamos otro bucle anidado que haga un rango de la posición [1],que nos dice la cantidad de barcos a crear de cada eslora,
    para que llame a la función "crear_y_colocar_barco_válido" el numero de veces que necesitamos y
    en el argumento metemos la posición [0] de la tupla de nuestra lista, que es la eslora. 
    Así nos va a ir generando los barcos necesarios de la eslora que queremos y nos los va a ir comprobando y colocando en el tablero.

"""

    
#tablero_máquina= 
tablero_maquina= crear_tablero_relleno()
print(tablero_maquina)
tablero_jugador_1= crear_tablero_relleno()
print('jugador',tablero_jugador_1)

marcador = {            ###diccionario para establecer un marcador de máquina y un marcador de jugador
    'jugador': 0,
    'maquina': 0
}
PUNTUACION_MAXIMA = 2

tablero_disparos_maquina= crear_tablero()
tablero_disparos_jugador_1= crear_tablero()

## marcador["jugador"]= marcador["jugador"]+1 cuando acierte

def pedir_coordenadas():
    disparo_jugador_x= int(input("Por favorintroduce tu coordenada x: "))
    disparo_jugador_y= int(input("Por favorintroduce tu coordenada y: "))
    return (disparo_jugador_x,disparo_jugador_y)




##### Una vez creados y colocados los barcos comienza el bucle del juego
print("Empieza el juego")

while marcador["jugador"] < PUNTUACION_MAXIMA and marcador["maquina"] < PUNTUACION_MAXIMA:
    print(f'Jugador 1, este es tu mar con tus barcos,\n {tablero_jugador_1}')

    print(f'Y aqui esta el mar de tu adversario \n{tablero_disparos_jugador_1}')
    #ha_acertado = False

    while marcador["jugador"] < PUNTUACION_MAXIMA:
        disparo_jugador = pedir_coordenadas()
        comprobar_jugador = comprobar_disparo(disparo_jugador, tablero_maquina)
        if comprobar_jugador:
            tablero_disparos_jugador_1[disparo_jugador] = "X"
            marcador["jugador"] += 1
            print("Tocado")
        else:
            tablero_disparos_jugador_1[disparo_jugador] = "A"
            print("Agua")
        break

    while marcador["maquina"] < PUNTUACION_MAXIMA:
        disparo_maquina = (random.randint(0, 9), random.randint(0, 9))
        print('disparo maquina', disparo_maquina)
        comprobar_maquina = comprobar_disparo(disparo_maquina, tablero_maquina)
        if comprobar_maquina:
            tablero_disparos_maquina[disparo_maquina] = "X"
            marcador["maquina"] += 1
            print("Tocado por maquina")
            print('disparos maquina', tablero_disparos_maquina)
        else:
            tablero_disparos_maquina[disparo_maquina] = "A"
            print("Agua maquina")
        break

print('ha terminado el juego')

if marcador["maquina"] == 20:
    print("Ohhhhh! Has perdido contra la máquina \n Que no te hunda la moral, vuelve a intentarlo de nuevo!")
    





#if tablero[disparo] == "_":
#    print("Agua")
#    tablero[disparo] = "A"
#elif tablero[disparo] == "O":
#    print("Tocado")
#    tablero[disparo] = "X"
#else:
#    print("Ya has disparado aquí")
#
#print(tablero)