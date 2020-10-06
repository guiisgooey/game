from fruit import fruit
import pygame as pg


class rotten_fruit(fruit):
    def __init__(self, name, x, y):
        super().__init__(name, x, y, v)
        self.debuff = self.getDebuff()
        self.points = self.getPoints()

    def getPoints(self):
        x = 0
        if self.name == "apple":
            x = -5
        elif self.name == "orange":
            x = -10
        elif self.name == "melon":
            x = -15
        return x

    def getDebuff(self):
        x = 0
        if self.name == "apple":
            x = -2
        elif self.name == "orange":
            x = -4
        elif self.name == "melon":
            x = -6
        return x

    def updateFruit(self, win):
        fruit = [pg.image.load("bad/a.png"), pg.image.load("bad/o.png"), pg.image.load("bad/m.png")]
        if self.name == "apple":
            win.blit(fruit[0], (self.x, self.y))
        elif self.name == "orange":
            win.blit(fruit[1], (self.x, self.y))
        elif self.name == "melon":
            win.blit(fruit[2], (self.x, self.y))
            
