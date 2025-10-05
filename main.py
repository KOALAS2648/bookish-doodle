import pygame as pg
from box import *
def main():
    screen = pg.display.set_mode((800,800))
    run = True
    box1 = Box(400, 400, 100, 100)
    box2 = Box(50,50, 10, 10)
    clock = pg.time.Clock()
    FPS = 60
    boxes = [box1, box2]
    while run:
        for box in boxes:
             box.update_pos()
        if box1.check_collision(box2):
            box1.color = (0, 255, 0)
        else:
            box1.color = (255,0,0)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        mousex, mousey =  pg.mouse.get_pos()
        box2.x, box2.y =mousex, mousey
        pg.display.set_caption(f"{box2.x=}, {box2.y=}")
        box1.draw(screen)
        box2.draw(screen)
        #clock.tick(FPS)

        pg.display.flip()
        pg.display.update()
        screen.fill((0,0,0))

if __name__ == "__main__":
    main()
    pg.quit()