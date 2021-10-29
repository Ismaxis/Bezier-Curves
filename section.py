import pygame as pg
from dot import Dot


class Broken_line:
    def __init__(self, sections):  # sections - tuple of Section objs
        self.sections = sections

    def get_point(self, t):
        if len(self.sections) > 1:
            return self.get_sub_line(t).get_point(t)
        else:
            return self.sections[0].get_point(t)

    def get_sub_line(self, t):
        prev_point = (-1, -1)
        sections = []
        for section in self.sections:
            cur_point = section.get_point(t)
            if prev_point[0] != -1:
                sections.append(Section((prev_point, cur_point)))

            prev_point = cur_point

        return Broken_line(sections)


class Section:
    def __init__(self, dots):  # dots - 2d (x,y) tuple
        self.dots = dots

    def get_point(self, t):
        point = ((1-t) * self.dots[0][0] + t * self.dots[1][0],
                 (1-t) * self.dots[0][1] + t * self.dots[1][1])

        return point


def dots_to_line(dots):  # dots - 2d (x,y) tuple
    sections = []
    for i in range(0, len(dots) - 1):
        sections.append(Section((dots[i].coords, dots[i+1].coords)))

    return Broken_line(sections)


def draw_broken_line(win, dots):  # dots - tuple of Dot objects
    for i in range(0, len(dots) - 1):
        dot1 = dots[i].coords
        dot2 = dots[i + 1].coords

        draw_section(win, dot1, dot2)


def draw_section(win, dot1, dot2):  # dot1, dot2 - (x,y) tuples
    pg.draw.line(win, (255, 255, 255), dot1, dot2, 1)
