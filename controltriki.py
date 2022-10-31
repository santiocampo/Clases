import interfaztriki
import logicatriki

interfaztriki.explicarJuego()
tableroJuego = logicatriki.obtenerTableroLogico()

for turno in ["X", "O", "X", "O", "X", "O", "X", "O", "X"]:
    print("\nTurno jugador", turno)
    while True:
        try:
            posicion = int(input("Ingrese posicion de juego: "))
        except ValueError:
            continue
        if (tableroJuego[posicion] == "X") or (tableroJuego[posicion] == "O") or (posicion >= 9):
            print("Ingrese otra posicion")
        else:
            break
    tableroJuego = logicatriki.actualizarTableroLogico(tableroJuego, posicion, turno)
    interfaztriki.dibujarTablero(tableroJuego)
    posibleGanador = logicatriki.determinarGanador(tableroJuego)
    if posibleGanador in ["X", "O"]:
        print("Felicidades, ha ganado el juego jugador", turno)
        break