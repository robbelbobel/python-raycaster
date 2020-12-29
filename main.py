import pygame
import sys
import math
from player import Player
from gameMap import GameMap
from camera import Camera

pygame.init()

width = 1000
height = 500

win = pygame.display.set_mode((width, height))

mapLayout = [
        1,1,1,1,1,1,1,1,
        1,0,1,0,0,0,0,1,
        1,0,0,0,0,0,0,1,
        1,0,0,2,0,0,1,1,
        1,0,0,0,0,0,0,1,
        1,0,0,0,1,0,0,1,
        1,0,0,0,1,0,0,1,
        1,1,1,1,1,1,1,1
        ]

player = Player(100, 100, 5, 5, 0)
gameMap = GameMap(8, 8, mapLayout)
camera = Camera(width, height)

while True:
    win.fill((224, 224, 224)) #Fill background with gray
    player.draw(win)
    camera.draw(win, gameMap, player.posX,  player.posY)
    gameMap.draw(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                camera.angle += 0.1
            if event.key == pygame.K_q:
                camera.angle -= 0.1
            if event.key == pygame.K_z:
                player.posX += math.cos(camera.angle) * 5
                player.posY -= math.sin(camera.angle) * 5
            if event.key == pygame.K_s:
                player.posX -= math.cos(camera.angle) * 5
                player.posY += math.sin(camera.angle) * 5

    pygame.display.flip()
    