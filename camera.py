import math
import pygame

class Camera:
    fov = math.radians(60)
    angle = math.radians(45)
    resolution = 0
    maxWallHeight = 0
    wallMiddle = 0

    def __init__(self, windowWidth, windowHeight):
        self.resolution = windowWidth
        self.wallMiddle = windowHeight/2
        self.maxWallHeight = windowHeight * (3/4)

    def drawWall(self, surface, dist, width, color):

        height = self.maxWallHeight/(dist/50)

        pygame.draw.line(surface, color, [width, self.wallMiddle], [width, self.wallMiddle - height/2])
        pygame.draw.line(surface, color, [width, self.wallMiddle], [width, self.wallMiddle + height/2])

    def vectorLength(self, p1, p2):
        dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        return dist

    def draw(self, surface, gameMap, pX, pY):

        for i in range(self.resolution):

            renderAngle = self.angle - (self.fov / 2) + i*(self.fov/self.resolution)

            while renderAngle > math.pi*2:
                renderAngle -= math.pi*2
            while renderAngle < 0:
                renderAngle += math.pi*2

            # ---Check Horizontal---
            rX = 0
            rY = 0
            xo = 0
            yo = 0
            dof = 0
            color = (255, 0, 0)

            if renderAngle < math.pi and renderAngle > 0: #facing up
                coTan = 1/math.tan(renderAngle)

                rY = math.floor(pY / gameMap.tileSize) * (gameMap.tileSize) - 0.00001
                rX = pX + coTan * (pY - rY)

                yo = -gameMap.tileSize
                xo = -coTan * yo
            
            elif renderAngle > math.pi and renderAngle < 2*math.pi: #facing down
                coTan = 1/math.tan(renderAngle)

                rY = math.floor(pY / gameMap.tileSize) * gameMap.tileSize  + gameMap.tileSize
                rX = pX + coTan * (pY - rY)

                yo = gameMap.tileSize
                xo = -coTan * yo

            else:
                dof = 8
                rX = pX
                rY = pY

            while dof < 8:
                mapIndex = math.floor((rY/gameMap.tileSize)) * gameMap.sizeX + math.floor(rX/gameMap.tileSize)
                if mapIndex > 0 and mapIndex < (gameMap.sizeX * gameMap.sizeY) and not gameMap.layout[mapIndex] == 0:
                    if gameMap.layout[mapIndex] == 2:
                        color = (0, 0, 255)
                    dof = 8

                else:
                    rX += xo
                    rY += yo
                    dof += 1

            horDestination = [rX, rY]

            #---Check Vertical---
            if renderAngle > (math.pi/2) and renderAngle < ((3/2) * math.pi): #facing left
                rX = math.floor(pX/gameMap.tileSize) * gameMap.tileSize - 0.00001
                rY = pY + math.tan(renderAngle) * (pX - rX)

                xo = -gameMap.tileSize
                yo = -math.tan(renderAngle) * xo
                
            elif renderAngle < (math.pi/2) or renderAngle > ((3/2) * math.pi): #facing right
                rX = math.floor(pX/gameMap.tileSize) * gameMap.tileSize + gameMap.tileSize
                rY = pY + math.tan(renderAngle) * (pX - rX)

                xo = gameMap.tileSize
                yo = -math.tan(renderAngle) * xo

            else:
                dof = 8
                rX = pX
                rY = pY
            
            dof = 0
            while dof < 8:
                mapIndex = math.floor((rY/gameMap.tileSize)) * gameMap.sizeX + math.floor(rX/gameMap.tileSize)
                if mapIndex > 0 and mapIndex < (gameMap.sizeX * gameMap.sizeY) and not gameMap.layout[mapIndex] == 0:
                    if gameMap.layout[mapIndex] == 2:
                        color = (0, 0, 255)
                    dof = 8
                else:
                    rX += xo
                    rY += yo
                    dof += 1
            
            verDestination = [rX, rY]

            horDist= self.vectorLength([pX, pY], horDestination)
            verDist = self.vectorLength([pX, pY], verDestination)

            if horDist > verDist:
                pygame.draw.line(surface, [255, 0, 0], [pX, pY], verDestination)
                self.drawWall(surface, verDist * math.cos(renderAngle - self.angle), i, color)

            else:
                pygame.draw.line(surface, [255, 0, 0], [pX, pY], horDestination)
                self.drawWall(surface, horDist * math.cos(renderAngle - self.angle), i, (color[0]/2, color[1]/2, color[2]/2))

            

            
