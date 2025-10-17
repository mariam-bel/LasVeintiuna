from veintiuna.cartas import Carta
import random as r

manoJugador = []
manoCasa = []

def sacarCartas(mano,baraja,veces):
    for i in range(veces):
        ultimaCarta = baraja.pop()
        mano.append(ultimaCarta)
        print(f"Carta {i+1}: {ultimaCarta}")


def llamarBaraja():
    baraja = []
    palos = ["espadas", "oros", "copas", "bastos"]
    for i in range(4):
        for j in range(1,11):
            if j==1:
                carta = Carta(1,palos[i],"As")
            elif j<8:
                carta = Carta(j,palos[i],j)
            else:
                figuras = ["Sota", "Caballo", "Rey"]
                carta = Carta(10,palos[i],figuras[j-8])
            baraja.append(carta)
    return baraja

baraja = llamarBaraja()
r.shuffle(baraja)
for carta in baraja:
    print(carta)
    print(f"El valor de la carta es {carta.valor}")
sacarCartas(manoJugador,baraja,2)