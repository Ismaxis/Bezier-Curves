import pygame as pg


class Dot:
    radius = 5

    def __init__(self, pos):  # pos - 2d tuple with start coords
        self.coords = pos
        self.set_rect()
        self.moving = False
        self.color = ((255, 255, 255), (255, 0, 0))

    def set_rect(self):
        self.rect = [self.coords[0] - self.radius, self.coords[1] - self.radius,
                     self.coords[0] + self.radius, self.coords[1] + self.radius]

    def draw(self, win):
        pg.draw.circle(
            win, self.color[int(self.moving)], self.coords, self.radius, self.radius)

    def check(self, pos):  # pos - 2d tuple with mouse coords
        if pos[0] >= self.rect[0] and pos[0] <= self.rect[2]:
            if pos[1] >= self.rect[1] and pos[1] <= self.rect[3]:
                return True

        else:
            return False

    def move(self, offset):
        if (offset[0] > 3):
            offset = (3, offset[1])
        if (offset[0] < -3):
            offset = (-3, offset[1])
        if (offset[1] > 3):
            offset = (offset[0], 3)
        if (offset[1] < -3):
            offset = (offset[0], -3)

        self.coords = (self.coords[0] + offset[0], self.coords[1] + offset[1])
        self.set_rect()
