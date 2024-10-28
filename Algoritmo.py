
class Algoritmo: # Algoritmos utilizados (minimax y poda alfa-beta)
    
    def miniMax(Nodo, Profundidad):
        for i in range(Nodo.Tablero.dimY):
            for j in range(Nodo.Tablero.dimX):
                # Nodo.Tablero.Matriz[i][j] == ' ' significa jugada disponible
                if Nodo.Tablero.Matriz[i][j] == ' ' and (j, i) not in Nodo.Hijos:
                    Nodo.GenerarHijo(j, i, True)
                    if Profundidad < 2:
                        return (i, j)

        Puntaje_Minimo = 1000
        i = 0
        j = 0
        for k, z in Nodo.Hijos.items():
            Resultado = Algoritmo.Maximo(z, Profundidad - 1, Puntaje_Minimo)
            if Puntaje_Minimo > Resultado:
                Puntaje_Minimo = Resultado
                i = k[0]
                j = k[1]

        return (i, j)
    
    def Maximo(Nodo, Profundidad, Alfa):
        if Profundidad == 0:
            return Nodo.Puntuacion

        for i in range(Nodo.Tablero.dimY):
            for j in range(Nodo.Tablero.dimX):
                if Nodo.Tablero.Matriz[i][j] == ' ' and (j, i) not in Nodo.Hijos:
                    Nodo.GenerarHijo(j, i, Nodo.Punto != 0) # False

        Puntaje_Maximo = -1000
        i = 0
        j = 0
        for k, z in Nodo.Hijos.items():
            if(z.Puntuacion < Nodo.Puntuacion):
                Resultado = Algoritmo.Maximo(z, Profundidad - 1, Puntaje_Maximo)
            else:
                Resultado = Algoritmo.Minimo(z, Profundidad - 1, Puntaje_Maximo)
                
            if Puntaje_Maximo < Resultado:
                Puntaje_Maximo = Resultado
            if Resultado > Alfa:
                return Resultado

        return Puntaje_Maximo

    def Minimo(Nodo, Profundidad, Beta):
        if Profundidad == 0:
            return Nodo.Puntuacion

        for i in range(Nodo.Tablero.dimY):
            for j in range(Nodo.Tablero.dimX):
                if Nodo.Tablero.Matriz[i][j] == ' ' and (j, i) not in Nodo.Hijos:
                    Nodo.GenerarHijo(j, i, Nodo.Punto == 0) # True

        Puntaje_Minimo = 1000
        i = 0
        j = 0
        for k, z in Nodo.Hijos.items():
            if(z.Puntuacion > Nodo.Puntuacion):
                Resultado = Algoritmo.Minimo(z, Profundidad - 1, Puntaje_Minimo)
            else:
                Resultado = Algoritmo.Maximo(z, Profundidad - 1, Puntaje_Minimo)
                
            if Puntaje_Minimo > Resultado:
                Puntaje_Minimo = Resultado
            if Resultado < Beta:
                return Resultado

        return Puntaje_Minimo
