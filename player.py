import pygame

class Player:
    posX = 0
    posY = 0
    sizeX = 20
    sizeY = 20

    def __init__(self, pX, pY, sX, sY, pA):
        self.posX = pX
        self.posY = pY

        self.sizeX = sX
        self.sizeY = sY

        self.angle = pA

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 255), (self.posX, self.posY, self.sizeX, self.sizeY))
