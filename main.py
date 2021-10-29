import sys
import pygame as pg
from dot import Dot
from section import dots_to_line, draw_broken_line

WIN_SIZE = (800, 800)
win = pg.display.set_mode(WIN_SIZE)

N = 100

start_points = ((200, 450), (230, 230), (520, 230), (550, 450))

dots = [Dot(start_points[0]), Dot(start_points[1]),
        Dot(start_points[2]), Dot(start_points[3])]

clock = pg.time.Clock()
LMB_pressed = False
draw_sub_lines = True
draw_dots = True

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        # CLICK
        if event.type == pg.MOUSEBUTTONDOWN:
            m_pos = pg.mouse.get_pos()
            buttons = pg.mouse.get_pressed(3)
            if buttons[0]:
                LMB_pressed = True

                for dot in dots:
                    if dot.check(m_pos):
                        dot.moving = True
                        break

            if buttons[2]:
                removed = False
                for dot in dots:
                    if dot.check(m_pos) and len(dots) > 2:
                        dots.remove(dot)
                        removed = True
                        break

                if not removed:
                    dots.append(Dot(m_pos))

        # KEYBOARD
        if event.type == pg.KEYDOWN:
            if event.key == 32:
                draw_sub_lines = not draw_sub_lines

            if event.key == 100:
                draw_dots = not draw_dots

            if event.key == 114:
                dots = [Dot(start_points[0]), Dot(start_points[1]),
                        Dot(start_points[2]), Dot(start_points[3])]

        # PRESSED
        if LMB_pressed:
            for dot in dots:
                if dot.moving:
                    dot.move(pg.mouse.get_rel())

        # RELEASE
        if event.type == pg.MOUSEBUTTONUP:
            LMB_pressed = False

            for dot in dots:
                dot.moving = False

    # UPDATE
    line = dots_to_line(dots)

    # DRAW
    win.fill((0, 0, 0))

    prev_point = line.get_point(0)
    for i in range(1, N+1):
        cur_point = line.get_point(i/N)
        pg.draw.line(win, (255*i/N, 135 + 120*i/N, 140),
                     prev_point, cur_point, 5)
        prev_point = cur_point

    if draw_dots:
        for dot in dots:
            dot.draw(win)

    if draw_sub_lines:
        draw_broken_line(win, dots)

    pg.display.update()
