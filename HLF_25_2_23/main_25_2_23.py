import numpy as np
import random

import funciones_25_2_23 as f

class Barco:

    def __init__(self,eslora,posiciones):

        self.posiciones = posiciones
        self.eslora = eslora



tablero_maquina= f.crear_tablero_relleno()
print("tablero máquina \n",tablero_maquina)
tablero_jugador_1= f.crear_tablero_relleno()
print('tablero jugador \n',tablero_jugador_1)

tablero_disparos_maquina= f.crear_tablero()

tablero_disparos_jugador_1= f.crear_tablero()





###   INSTRUCCIONES DEL JUEGO
print("\t\t\t\t\t\t\t EMPIEZA EL JUEGO\n ", "~~"*70)
print("Instrucciones: \n\n\t El juego consiste en disparar a los barcos de tu oponente y hundirlos antes de que tu oponente destruya los tuyos.\n")

print("\t Empieza jugando el Jugador 1, si acierta sigue disparando hasta que tenga un fallo, entonces será el turno de la máquina.\n")

print("\t\t\t\t\t\t\t¡¡¡BUENA SUERTE!!!\n")


print(f'\n Jugador 1, este es tu mar con tus barcos:\n\n {tablero_jugador_1}\n')
print(f'\n Y aqui esta el mar de tu adversario: \n\n {tablero_disparos_jugador_1}\n')



marcador = {            ###diccionario para establecer un marcador de máquina y un marcador de jugador
    'jugador': 0,
    'maquina': 0}

PUNTUACION_MAXIMA = 1


###  EMPIEZA EL JUEGO


while marcador["jugador"] < PUNTUACION_MAXIMA and marcador["maquina"] < PUNTUACION_MAXIMA:

    
    #  EMPIEZAN LOS TURNOS DENTRO DEL JUEGO
    while marcador["jugador"] < PUNTUACION_MAXIMA:
        disparo_jugador = f.pedir_coordenadas()
        comprobar_jugador = f.comprobar_disparo(disparo_jugador, tablero_maquina)
        if comprobar_jugador==True:
            tablero_disparos_jugador_1[disparo_jugador] = "X"
            marcador["jugador"] += 1
            print("Tocado por Jugador 1")
            print('disparos jugador\n', tablero_disparos_jugador_1)
            continue
        else:
            tablero_disparos_jugador_1[disparo_jugador] = "A"
            print("Agua")
            print('disparos jugador\n', tablero_disparos_jugador_1)
            break

    while marcador["maquina"] < PUNTUACION_MAXIMA:
        disparo_maquina = (random.randint(0, 9), random.randint(0, 9))
        print('disparo maquina', disparo_maquina)
        comprobar_maquina = f.comprobar_disparo(disparo_maquina, tablero_maquina)
        if comprobar_maquina== True:
            tablero_disparos_maquina[disparo_maquina] = "X"
            marcador["maquina"] += 1
            print("Tocado por maquina")
            print('disparos maquina\n', tablero_disparos_maquina)
            continue
        else:
            tablero_disparos_maquina[disparo_maquina] = "A"
            print("Agua maquina")
            print('disparos maquina\n', tablero_disparos_maquina,"\n")
            break


#### FINAL
print('\t El juego ha terminado\n')

if marcador["maquina"] == 20:
    print("\t Ohhhhh! Has perdido contra la máquina \n\t\tQue no te hunda la moral, vuelve a intentarlo de nuevo!")
else:
    print("\t¡¡ENHORABUENA, HAS GANADO!!")