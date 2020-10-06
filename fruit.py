import pygame as pg

class fruit():
    def __init__(self, name, x, y):
        self.name = name
        self.points = self.getPoints()
        self.x = x
        self.y = y
        self.v = 5
        self.fallState = 30
    
    def getPoints(self):
        x = 0
        if self.name == "apple":
            x = 5
        elif self.name == "orange":
            x = 10
        elif self.name == "melon":
            x = 15
        return x

    def updateFruit(self, win):
        fruit = [pg.image.load("good/a.png"), pg.image.load("good/o.png"), pg.image.load("good/m.png")]
        if self.name == "apple":
            win.blit(fruit[0], (self.x,self.y))
        elif self.name == "orange":
            win.blit(fruit[1], (self.x, self.y))
        elif self.name == "melon":
            win.blit(fruit[2], (self.x, self.y))

    def fall(self):
        self.y -= 1