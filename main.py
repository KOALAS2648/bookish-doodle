import pygame as pg
from box import *
def main():
    screen = pg.display.set_mode((800,800))
    run = True
    box1 = Box(400, 400, 100, 100)
    box2 = Box(0,0, 10, 10)
    clock = pg.time.Clock()
    FPS = 60
    while run:
        #mousex, mousey = 
        box2.x, box2.y = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        box1.draw(screen)
        box2.draw(screen)
        clock.tick(FPS)

        pg.display.update()
        screen.fill((0,0,0))

if __name__ == "__main__":
    main()
    pg.quit()