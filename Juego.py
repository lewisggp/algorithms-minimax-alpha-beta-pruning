from random import *
from Algoritmo import *
from Tablero import *
from Nodo import *

class Juego: # Una clase para gestionar los movimientos realizados por el humano y la computadora
    
    def __init__(self, dimX, dimY, Profundidad):
        tablero = Tablero([], dimX, dimY)
        tablero.Iniciar()
        self.NodoTablero = Nodo(tablero)
        self.Profundidad = Profundidad
        self.Puntuacion = 0

    def Humano(self):
        self.Puntuacion = self.NodoTablero.Puntuacion
        self.NodoTablero = Nodo(self.NodoTablero.Tablero)
        self.NodoTablero.Puntuacion = self.Puntuacion
        self.NodoTablero.Dibujar()

        puntuacionAntes = self.NodoTablero.Puntuacion
        
        x = int(input("Por favor ingresa la coordenada 'X' de tu elección (un entero como 4): "))
        y = int(input("Por favor ingresa la coordenada 'Y' de tu elección (un entero como 4): "))
        
        if (x, y) not in self.NodoTablero.Hijos:
            self.NodoTablero.GenerarHijo(x, y, False)
        self.NodoTablero = self.NodoTablero.Hijos[(x, y)]

        puntuacionDespues = self.NodoTablero.Puntuacion
        
        print("Puntuación Actual => Tu Puntuación - Puntuación de la IA = " + str(self.NodoTablero.Puntuacion))
                
        if puntuacionDespues > puntuacionAntes:
            self.Humano()
        else:
            self.Computadora()

    def Computadora(self):
        self.NodoTablero.Dibujar()
        
        puntuacionAntes = self.NodoTablero.Puntuacion

        movimiento = Algoritmo.miniMax(self.NodoTablero, self.Profundidad)        
        if (movimiento[0], movimiento[1]) not in self.NodoTablero.Hijos:
            self.NodoTablero.GenerarHijo(movimiento[0], movimiento[1], True)
        self.NodoTablero = self.NodoTablero.Hijos[(movimiento[0], movimiento[1])]
        
        puntuacionDespues = self.NodoTablero.Puntuacion

        print("La IA seleccionó las siguientes coordenadas para jugar:\n" + "(" ,str(movimiento[0]), ", " + str(movimiento[1]), ")", end = "\n\n")
        print("Puntuación Actual => Tu Puntuación - Puntuación de la IA = " + str(self.NodoTablero.Puntuacion), end = "\n\n\n")
        
        if len(self.NodoTablero.Hijos) == 0:
            self.NodoTablero.Dibujar()
            self.Evaluación()
            return

        if puntuacionDespues < puntuacionAntes:
            self.Computadora()
        else:
            self.Humano()

    def Evaluación(self): # Función de evaluación para manejar las puntuaciones finales

        if self.NodoTablero.Puntuacion > 0:
            print("¡Ganaste!")
            exit()
        elif self.NodoTablero.Puntuacion < 0:
            print("¡Perdiste!")
            exit()
        else:
            print("¡Empate!")
            exit()

    def Empezar(self):
        self.Humano()
