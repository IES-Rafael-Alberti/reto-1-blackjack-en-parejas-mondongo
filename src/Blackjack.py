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

def DarCarta(carta , a , jugador , b ):
    carta=str(random.randint(0, 12))
    
    match (carta):
        case ("0"):
            a="0"
            b=0
        case ("1"):
            a="A"
            b=10
        case ("2"):
            a="2"
            b=2
        case ("3"):
            a="3"
            b=3
        case ("4"):
            a="4"
            b=4
        case ("5"):
            a="5"
            b=5
        case ("6"):
            a="6"
            b=6
        case ("7"):
            a="7"
            b=7
        case ("8"):
            a="8"
            b=8
        case ("9"):
            a="9"
            b=9
        case ("10"):
            a="J"
            b=10  
        case ("11"):
            a="Q"
            b=10    
        case ("12"):
            a="K"
            b=10
    print(f"{jugador} : Tus cartas son => {a} = {b}")

def PedirCarta( pedircarta):
    pedir = input("Quieres otra carta ? s/n : ")
    pedir = pedir.lower()
    if pedir == "s":
        pedircarta=True
        return pedircarta
    elif pedir == "n":
        pedircarta=False
        return pedircarta


def main():
    modo = input("""Elija el modo de juego:
    1. Contra la máquina
    2. Dos jugadores
    => """)
    carta=0
    a=str()
    b=0
    inicio(modo)
    if modo == "1":
        jugador=jugadores()
    pedircarta = True
    while pedircarta == True :
        DarCarta(carta , a , jugador , b)
        (PedirCarta(pedircarta))
    
        

    
    
def prueba(jugador1, jugador2):
    print(jugador1 , jugador2)


if __name__ == "__main__":
    main() 