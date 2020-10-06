import pygame as pg
from game import game
from player import player

pg.init()

sWidth = 500
sHeight = 500

g = game(sWidth, sHeight)
g.setCaption("fruit basket")

x = 50
y = 440
width = 42
height = 36
v = 10
run = True
win = pg.display.set_mode((sWidth, sHeight))
p1 = player(x,y,width,height)
g.updateWin(win, p1)
while run:
    pg.time.delay(50)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    if (keys[pg.K_LEFT] or keys[pg.K_a]) and (x > v):
        x -= v
        p1.updateChar(-v, 0)
        p1.setLeft(True)
        g.updateWin(win, p1)
    elif (keys[pg.K_RIGHT] or keys[pg.K_d]) and (x < sWidth - width - v):
        x += v
        p1.updateChar(v, 0)
        p1.setRight(True)
        g.updateWin(win, p1)
    elif (keys[pg.K_UP] or keys[pg.K_w]) and (y > v):
        y -= v
        p1.updateChar(0, -v)
        p1.setUp(True)
        g.updateWin(win, p1)
    elif (keys[pg.K_DOWN] or keys[pg.K_s]) and (y < sHeight - height - v):
        y += v
        p1.updateChar(0, v)
        p1.setDown(True)
        g.updateWin(win, p1)
    else:
        p1.setAll(False)
        g.updateWin(win,p1)
pg.quit()
