import pygame
import sys
import time
from cartas import Carta
import random as r

pygame.init()

ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Las Veintiuna')
manoJugador = []
manoCasa = []

def sumarCartas(mano):
    total = 0
    for carta in mano:
        total += carta.valor
    return total

def verAses(mano):
    total = sumarCartas(mano)
    i = 0
    while total > 21 and i < len(mano):
        if mano[i].valor == 11:
            mano[i].valor = 1
            total = sumarCartas(mano)
        i += 1
    return total

def sacarCartas(mano, baraja, veces):
    for i in range(veces):
        if baraja:
            ultimaCarta = baraja.pop()
            mano.append(ultimaCarta)
    verAses(mano)

def imagenCartas(carta, x, y):
    try:
        ruta = f"img/{carta.nombre}_{carta.palo}.png"
        imagen = pygame.image.load(ruta)
        imagen = pygame.transform.scale(imagen, (100, 150))
        ventana.blit(imagen, (x, y))
    except pygame.error:
        print(f"Error al cargar la imagen: {ruta}")

def mostrarCartas(mano, esJugador=True):
    x = 50
    y = 400 if esJugador else 50
    for carta in mano:
        print(f"Carta {'Jugador' if esJugador else 'Casa'}: {carta}")
        imagenCartas(carta, x, y)
        x += 100

def mostrarTexto(texto, x, y):
    fuente = pygame.font.SysFont('arial', 30)
    superficie = fuente.render(texto, True, (255, 255, 255))
    ventana.blit(superficie, (x, y))

def llamarBaraja():
    baraja = []
    palos = ["espadas", "oros", "copas", "bastos"]
    for i in range(4):
        for j in range(1, 11):
            if j == 1:
                carta = Carta(11, palos[i], "As")
            elif j < 8:
                carta = Carta(j, palos[i], str(j))
            else:
                figuras = ["Sota", "Caballo", "Rey"]
                carta = Carta(10, palos[i], figuras[j-8])
            baraja.append(carta)
    return baraja

baraja = llamarBaraja()
r.shuffle(baraja)

sacarCartas(manoJugador, baraja, 2)
sacarCartas(manoCasa, baraja, 2)

seguir = True
ganar = True
continuar = True
turnoCasa = False

ventana.fill((0, 128, 0))
mostrarCartas(manoJugador, True)
mostrarCartas(manoCasa, False)

totalJugador = sumarCartas(manoJugador)
totalCasa = sumarCartas(manoCasa)

print(f"Valor total Jugador: {totalJugador}")
print(f"Carta Casa: {manoCasa[0]}")

while continuar:
    ventana.fill((0, 128, 0))
    mostrarCartas(manoJugador, True)
    mostrarCartas(manoCasa, False)
    if seguir:
        mostrarTexto("Presiona 'S' para sacar carta, 'N' para plantarse", 50, 550)
    elif turnoCasa:
        mostrarTexto("Turno de la Casa...", 50, 550)
    mostrarTexto(f"Jugador: {totalJugador}", 50, 350)
    mostrarTexto(f"Casa: {'?' if seguir else totalCasa}", 50, 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuar = False
        elif event.type == pygame.KEYDOWN and seguir:
            if event.key == pygame.K_s:  # Sacar carta
                sacarCartas(manoJugador, baraja, 1)
                totalJugador = sumarCartas(manoJugador)
                ventana.fill((0, 128, 0))
                mostrarCartas(manoJugador, True)
                mostrarCartas(manoCasa, False)
                mostrarTexto(f"Jugador: {totalJugador}", 50, 350)
                mostrarTexto("Presiona 'S' para sacar carta, 'N' para plantarse", 50, 550)
                pygame.display.update()
                print(f"Valor total Jugador: {totalJugador}")
                if totalJugador > 21:
                    seguir = False
                    ganar = False
            elif event.key == pygame.K_n:
                print("Turno de la Casa: ")
                seguir = False
                turnoCasa = True

    if turnoCasa:
        totalCasa = sumarCartas(manoCasa)
        if totalCasa < 17:
            sacarCartas(manoCasa, baraja, 1)
            totalCasa = sumarCartas(manoCasa)
            ventana.fill((0, 128, 0))
            mostrarCartas(manoJugador, True)
            mostrarCartas(manoCasa, False)
            mostrarTexto(f"Jugador: {totalJugador}", 50, 350)
            mostrarTexto(f"Casa: {totalCasa}", 50, 20)
            mostrarTexto("Turno de la Casa...", 50, 550)
            pygame.display.update()
            print(f"Valor total Casa: {totalCasa}")
            time.sleep(0.5)
        else:
            print(f"Valor final Casa: {totalCasa}")
            if totalCasa > 21:
                ganar = True
            else:
                totalJugador = sumarCartas(manoJugador)
                ganar = totalJugador > totalCasa and totalJugador <= 21
            turnoCasa = False

    if not seguir and not turnoCasa:
        mensaje = "Has ganado" if ganar else "Has perdido"
        print(mensaje)
        mostrarTexto(mensaje, 50, 300)
        pygame.display.update()
        time.sleep(2)
        continuar = False

    pygame.display.update()

pygame.quit()
sys.exit()