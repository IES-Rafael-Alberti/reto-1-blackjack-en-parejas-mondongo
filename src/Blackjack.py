import random
def inicio(modo):
    if modo == "1":
        return modo
    elif modo == "2":
        return modo 
    else:
        print("Ingrese un modo de juego válido")
    
def jugadores():
    jugador = input("Ingrese su apodo: ")
    return jugador

def DarCarta(carta , a , jugador):
    carta=str(random.randint(0, 12))
    match (carta):
        case ("0"):
            a="0"
        case ("1"):
            a="A"
        case ("2"):
            a="2"
        case ("3"):
            a="3"
        case ("4"):
            a="4"
        case ("5"):
            a="5"
        case ("6"):
            a="6"
        case ("7"):
            a="7"
        case ("8"):
            a="8"
           
        case ("9"):
            a="9"
            
        case ("10"):
            a="J"
           
        case ("11"):
            a="Q"
            
        case ("12"):
            a="K"
    print(f"{jugador} : Tus cartas son => {a}")

def main():
    modo = input("""Elija el modo de juego:
    1. Contra la máquina
    2. Dos jugadores
    => """)
    carta=0
    a=str()
    inicio(modo)
    if modo == "1":
        jugador=jugadores()
    elif modo == "2":
        jugador=jugadores()

        

    DarCarta(carta , a , jugador  )
    
def prueba(jugador1, jugador2):
    print(jugador1 , jugador2)


if __name__ == "__main__":
    main() 