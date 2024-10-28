
class Tablero:
        
    def __init__(self, Matriz, dimX, dimY):
        self.Matriz = Matriz
        self.dimX = dimX
        self.dimY = dimY

    def Iniciar(self):
        for i in range(0, self.dimY):
            R = []
            for j in range (0, self.dimX):
                if i % 2 == 1 and j % 2 == 1:
                    R.append(1)  # (randint(1, 9)) # Asigna valor a la casilla (filas y columnas impres)
                elif i % 2 == 0 and j % 2 == 0:
                    R.append('*') # Imprime asteriscos como puntos en el tablero (filas y columnas pares)
                else:
                    R.append(' ') # Agrega espacio adicional para acciones en el juego (demás casillas)
            self.Matriz.append(R)

    def Obtener_matriz(self):
        ans = []
        for i in range(0, self.dimY):
            R = []
            for j in range(0, self.dimX):
                R.append(self.Matriz[i][j])
            ans.append(R)
        return ans

    def Dibujar_matriz(self):        
        if self.dimX > 9:
            print(" ", end='')
        print("   ", end='')
        for i in range(0, self.dimX):
            print(str(i), end='  ')
        print()

        if self.dimX > 9:
            print(" ", end='')
        print("   ", end='')
        for i in range(0, self.dimX + 1):
            print("___", end='')
        print()
        for j in range(self.dimY):
            if self.dimX > 9 and j < 10:
                print(" ", end='')
            print(str(j) + "| ", end='')
            for z in range(self.dimX):
                print(str(self.Matriz[j][z]), end='  ')
            print()
        print("   _________________________\n")

    def Obtener_estado_actual(self):
        return Tablero(self.Obtener_matriz(), self.dimX, self.dimY) # Duplica la instancia

    def Accion(self, i, j):
        Suma = 0

        if j % 2 == 0 and i % 2 == 1:
            self.Matriz[j][i] = '-'
            if j < self.dimY - 1:
                if self.Matriz[j+2][i] == '-' and self.Matriz[j+1][i+1] == '|' and self.Matriz[j+1][i-1] == '|':
                    Suma += self.Matriz[j+1][i]
            if j > 0:
                if self.Matriz[j-2][i] == '-' and self.Matriz[j-1][i+1] == '|' and self.Matriz[j-1][i-1] == '|':
                    Suma += self.Matriz[j-1][i]

        elif j % 2 == 1 and i % 2 == 0:
            self.Matriz[j][i] = '|'
            if i < self.dimX - 1:
                if self.Matriz[j][i+2] == '|' and self.Matriz[j+1][i+1] == '-' and self.Matriz[j-1][i+1] == '-':
                    Suma += self.Matriz[j][i+1]
            if i > 0:
                if self.Matriz[j][i-2] == '|' and self.Matriz[j+1][i-1] == '-' and self.Matriz[j-1][i-1] == '-':
                    Suma += self.Matriz[j][i-1]
                    
        return Suma
