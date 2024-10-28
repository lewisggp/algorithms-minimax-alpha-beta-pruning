
class Nodo: # Nodo del arbol del algoritmo
   
    def __init__(self, Tablero):
        self.Tablero = Tablero
        self.Puntuacion = 0
        self.Hijos = {}
        self.Punto = 0

    def GenerarHijo(self, i, j, jugador):
        self.Hijos[(i, j)] = Nodo(self.Tablero.Obtener_estado_actual())
        mul = 1
        if jugador:
            mul *= -1
        self.Hijos[(i, j)].Punto = self.Hijos[(i, j)].Tablero.Accion(i, j)
        self.Hijos[(i, j)].Puntuacion = (self.Hijos[(i, j)].Punto * mul) + self.Puntuacion

    def Agregar(self, i, j, hijo):
        self.Hijos[(i,j)] = hijo

    def Dibujar(self):
        self.Tablero.Dibujar_matriz()
