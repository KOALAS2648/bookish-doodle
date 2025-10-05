import pygame as pg

class Box:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.centralx = self.x-self.width//2
        self.centraly = self.y-self.height//2
        self.color = (255, 0, 0)

    def check_collision(self, other):
        check_collision_y = other.y+other.height >= self.y
    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.centralx, self.centraly, self.width, self.height))