import pygame as pg
import random
from fruit import fruit
from rotten_fruit import rotten_fruit
from player import player

class game():
    def __init__(self, w, h):
        self.fruits = []
        self.w = 500
        self.h = 500

    def setCaption(self, string):
        pg.display.set_caption(string)
    
    def addFruit(self, win):
        tf = [True, False]
        x = random.choice(tf)
        f = None
        fruits = ["apple", "orange", "melon"]
        if x == True:
            f = fruit(random.choice(fruits), random.randint(0,self.w), random.randint(0,self.h))
        else:
            f = fruit(random.choice(fruits), random.randint(0, self.w), random.randint(0, self.h))
        self.fruits.append(f)
        f.updateFruit(win)

    def removeFruit(self):
        self.fruits.pop(0)

    def updateWin(self, win, player):
        win.fill((255, 255, 255))
        player.drawChar(win)
        if not self.fruits:
            self.addFruit(win)
        for x in self.fruits:
            x.updateFruit(win)
            if x.fallState == 0:
                removeFruit()
                self.addFruit()
            else:
                x.fall()
