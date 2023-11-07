import random
def inicio(modo):
    print("Elija el modo de juego:")
    print("1. Contra la máquina")
    print("2. Dos jugadores")
   
    if modo == "1":
        return modo
    elif modo == "2":
        return modo 
    else:
        print("Ingrese un modo de juego válido")
    
def jugadores(modo):
    if modo == "1":
        jugador = input("Ingrese su apodo: ")
        return jugador
    else:
        jugador = input("Jugador 1 - Ingrese su apodo: ")
        jugador2 = input("Jugador 2 - Ingrese su apodo: ")
        return jugador, jugador2
       




def main():
    modo = input()
    inicio(modo)
    jugadores(modo)
    



if __name__ == "__main__":
    main() 