import funciones as f


tablero = f.crear_tablero()

barcos = [f.crear_barco_random(2), 
          f.crear_barco_random(4), 
          f.crear_barco_random(3), 
          f.crear_barco_random(4)]


tablero = f.colocar_barcos(barcos, tablero)

tablero = f.disparar((3,5), tablero)
tablero = f.disparar((1,7), tablero)
tablero = f.disparar((1,5), tablero)

print(tablero)