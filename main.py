from Algoritmo import *
from Tablero import *
from Juego import *
from Nodo import *

def main():
    print("¡ Bienvenido al juego de Lineas y Cajas !")
            
    x = int(input("\nPor favor ingresa el número de filas para el tablero: \n")) * 2 + 1
    if x < 5:
        print("\nEl número de filas debe ser al menos 2\n")
        exit()

    y = int(input("\nPor favor ingresa el número de columnas para el tablero: \n")) * 2 + 1
    if y < 5:
        print("\nEl número de columnas debe ser al menos 2\n")
        exit()

    # Profundidad = int(input("\nIngrese la dificultad/profundidad de la IA (mayor que 1): \n"))

    # if Profundidad < 2:
    #     print("\nLa profundidad debe ser mayor que 1\n")
    #     exit()

    juego = Juego(x, y, 4)
    juego.Empezar()
            
if __name__ == "__main__":
    main()
