import pygame as pg
class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.v = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkFrame = 0
        self.score = 0

    def drawChar(self, win):
        still = [pg.image.load("player_sprite/1.png")]
        walkRight = [pg.image.load("player_sprite/2.png"), pg.image.load("player_sprite/3.png")]
        walkLeft = [pg.image.load("player_sprite/8.png"), pg.image.load("player_sprite/9.png")]
        walkUp = [pg.image.load("player_sprite/4.png"), pg.image.load("player_sprite/5.png")]
        walkDown = [pg.image.load("player_sprite/6.png"), pg.image.load("player_sprite/7.png")]
        if (not self.walkFrame % 2 == 0) and (self.left == True):
            win.blit(walkLeft[0], (self.x, self.y))
            pg.display.update()
        elif (self.walkFrame % 2 == 0) and (self.left == True):
            win.blit(walkLeft[1], (self.x, self.y))
            pg.display.update()
        elif (not self.walkFrame % 2 == 0) and (self.right == True):
            win.blit(walkRight[0], (self.x, self.y))
            pg.display.update()
        elif (self.walkFrame % 2 == 0) and (self.right == True):
            win.blit(walkRight[1], (self.x, self.y))
            pg.display.update()
        elif (not self.walkFrame % 2 == 0) and (self.up == True):
            win.blit(walkUp[0], (self.x, self.y))
            pg.display.update()
        elif (self.walkFrame % 2 == 0) and (self.up == True):
            win.blit(walkUp[1], (self.x, self.y))
            pg.display.update()
        elif (not self.walkFrame % 2 == 0) and (self.down == True):
            win.blit(walkDown[0], (self.x, self.y))
            pg.display.update()
        elif (self.walkFrame % 2 == 0) and (self.down == True):
            win.blit(walkDown[1], (self.x, self.y))
            pg.display.update()
        else:
            win.blit(still[0], (self.x, self.y))
            pg.display.update()
        self.walkFrame +=1
            
    def updateChar(self, x, y):
        self.x += x
        self.y += y
    
    def addPoints(self, points):
        self.score += points
    
    def setLeft(self, val):
        self.left = val
        self.right = False
        self.up = False
        self.down = False

    def setRight(self, val):
        self.right = val
        self.up = False
        self.down = False
        self.left = False

    def setUp(self, val):
        self.up = val
        self.left = False
        self.down = False
        self.right = False

    def setDown(self, val):
        self.down = val
        self.up = False
        self.left = False
        self.right = False

    def setAll(self, val):
        self.down = val
        self.up = val
        self.left = val
        self.right = val

