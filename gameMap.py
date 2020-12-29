import pygame

class GameMap:
    layout = [None]
    sizeX = 8
    sizeY = 8

    tileSize = 20

    def __init__(self, sX, sY,mLayout):
        self.sizeX = sX
        self.sizeY = sY
        self.layout = mLayout
        

    def draw(self, surface):
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                color = (0, 0, 0)
                if not self.layout[y*self.sizeX + x] == 0:
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)

                pygame.draw.rect(surface, color, [x * self.tileSize, y * self.tileSize, self.tileSize - 1, self.tileSize - 1])