import pygame
from personaje import Personaje
import constantes 

player = Personaje(50, 50)

pygame.init()

ancho = constantes.ANCHO_VENTANA
alto = constantes.ALTO_VENTANA

ventana = pygame.display.set_mode((ancho, alto))

pygame.display.set_caption("mi primer juego")

"""variables de movimiento"""
mover_arriba = False 
mover_abajo = False
mover_izquierda = False
mover_derecha = False

reloj = pygame.time.clock()

run = True

while run:

    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG)

    """calcular el movimiento"""
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    player.movimiento(delta_x, delta_y)



    player.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.k_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.k_s:
                mover_abajo = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.k_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.k_s:
                mover_abajo = False

    pygame.display.uptade() 

pygame.quit()