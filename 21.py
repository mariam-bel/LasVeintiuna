import time

from cartas import Carta
import random as r

manoJugador = []
manoCasa = []

def sumarCartas(mano):
    total = 0
    for carta in mano:
        total +=  carta.valor
    return total

def verAses(mano):
    for carta in mano:
        if sumarCartas(mano)>21 and carta.valor==11:
            carta.valor=1

def sacarCartas(mano,baraja,veces):
    for i in range(veces):
        ultimaCarta=baraja.pop()
        mano.append(ultimaCarta)
    verAses(mano)

def mostrarCartas(mano, esJugador = True):
    for carta in mano:
        print(f"Carta {'Jugador' if esJugador else 'Casa'}: {carta}")
        time.sleep(0.3)

def llamarBaraja():
    baraja = []
    palos = ["espadas", "oros", "copas", "bastos"]
    for i in range(4):
        for j in range(1,11):
            if j==1:
                carta = Carta(11,palos[i],"As")
            elif j<8:
                carta = Carta(j,palos[i],j)
            else:
                figuras = ["Sota", "Caballo", "Rey"]
                carta = Carta(10,palos[i],figuras[j-8])
            baraja.append(carta)
    return baraja
baraja = llamarBaraja()
r.shuffle(baraja)

sacarCartas(manoJugador,baraja,2)

sacarCartas(manoCasa,baraja,2)

mostrarCartas(manoJugador, "Jugador")

print(f"Valor total Jugador: {sumarCartas(manoJugador)}")
print(f"Carta Casa: {manoCasa[0]}")
totalJugador = 0
totalCasa = 0

seguir = True
ganar = True
while seguir:
    sacar = input("¿Quieres seguir sacando cartas? (s/n)").lower()
    if sacar == "n":
        print("Turno de la Casa: ")
        totalCasa = sumarCartas(manoCasa)
        while totalCasa < 17:
            sacarCartas(manoCasa,baraja,1)
            totalCasa = sumarCartas(manoCasa)
            mostrarCartas(manoCasa, "Casa")
            print(f"Valor total Casa: {totalCasa}")
        if totalCasa > 21:
            seguir = False
            ganar = True
        else:
            seguir = False
            ganar = totalJugador > totalCasa
    else:
        sacarCartas(manoJugador, baraja, 1)
        totalJugador = sumarCartas(manoJugador)
        mostrarCartas(manoJugador, "Jugador")
        print(f"Valor total Jugador: {totalJugador}")
        if totalJugador > 21 or totalJugador < totalCasa:
            seguir = False
            ganar = False


if ganar == True:
    print("Has ganado")
else:
    print("Has perdido")


