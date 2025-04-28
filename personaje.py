import pygame

class Personaje():

    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, 20, 20)
        self.forma.center = (x,y)

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, (255, 255, 0) self.forma)
