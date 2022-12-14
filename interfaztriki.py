"""
Este módulo contiene 3 funciones para imprimir el juego triqui
"""

def explicarJuego():
    explicacion = """
    ========================================================
    Este es el juego triqui

    Es un juego de dos jugadores, para ganar debe 
    completar 3 caracteres iguales en linea ("X o "O")

    Para ingresar la posicion en el juego, guiese
    con los siguientes numeros


    0    |     1     |    2
    ------------------------
    3    |     4     |    5
    ------------------------
    6    |     7     |    8 
    ========================================================
    """
    print(explicacion)
    input("Ingrese enter para empezar el juego... ")

def dibujarTablero(tableroLogico:list):
    tableroVisual= """

    {}  |  {}  |  {}
    -------------------
    {}  |  {}  |  {}
    -------------------
    {}  |  {}  |  {} 
    
    """.format(tableroLogico[0], tableroLogico[1],
               tableroLogico[2], tableroLogico[3],
               tableroLogico[4], tableroLogico[5],
               tableroLogico[6], tableroLogico[7],
               tableroLogico[8])
    tableroVisual = tableroVisual.replace("None", " ")
    print(tableroVisual)


if __name__ == "__main__":
    explicarJuego()
    tablero1 = [None]*9
    tablero2 = ["X"]*9
    dibujarTablero(tablero1)
    dibujarTablero(tablero2)
