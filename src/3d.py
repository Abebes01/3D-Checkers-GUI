import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from checkers import CheckerBoard
from pywavefront import Wavefront
import numpy as np
from OpenGL.GL import *
import math
import glm

def draw_cube():

    board = CheckerBoard(4)
    grid = board.get_grid()
    x = 2
    y = -3
    glEnable(GL_DEPTH_TEST)
    color = (1, 1, 1) 
    for x in range(0-int(len(grid)/2), int(len(grid)/2)):
        for a in range (3+len(grid[0])):
            glBegin(GL_QUADS)

            color = (0.1725, 0.1922, 0.2588) if (x+a) % 2 == 0 else (0.3294, 0.3569, 0.4471)
            glColor3f(color[0], color[1], color[2])
            glVertex3f(x+0, y + 0, a + 1)
            glVertex3f(x+1, y + 0, a + 1)
            glVertex3f(x+1, y + 0.25, a + 1)
            glVertex3f(x+0, y + 0.25, a + 1)

            glNormal3f(x+3, y + 3, a + 1) 
            glVertex3f(x+0, y + 0, a + 0)
            glVertex3f(x+0, y + 0, a + 1)
            glVertex3f(x+1, y + 0, a + 1)
            glVertex3f(x+1, y + 0, a + 0)

            glVertex3f(x+0, y + 0.25, a + 0)
            glVertex3f(x+0, y + 0.25, a + 1)
            glVertex3f(x+1, y + 0.25, a + 1)
            glVertex3f(x+1, y + 0.25, a + 0)

            glVertex3f(x+0, y + 0, a + 0)
            glVertex3f(x+1, y + 0, a + 0)
            glVertex3f(x+1, y + 0.25, a + 0)
            glVertex3f(x+0, y + 0.25, a + 0)


            glVertex3f(x+1, y + 0, a + 0)
            glVertex3f(x+1, y + 0, a + 1)
            glVertex3f(x+1, y + 0.25, a + 1)
            glVertex3f(x+1, y + 0.25, a + 0)

            glVertex3f(x+0, y + 0, a + 0)
            glVertex3f(x+1, y + 0, a + 0)
            glVertex3f(x+1, y + 0.25, a + 0)
            glVertex3f(x+0, y + 0.25, a + 0)
            glEnd()
            if board.get_piece((x+int(len(grid)/2), a-3)) != None:
                glBegin(GL_QUADS)
                color = (0.0, 0.0, 0.0) if board.get_piece((x+int(len(grid)/2), a-3)).get_color() == "red" else (1.0, 1.0, 1.0)
                glColor3f(color[0], color[1], color[2])
                glVertex3f(x+0, y + 3, a + 1.5)
                glVertex3f(x+0.5, y + 3, a + 1.5)
                glVertex3f(x+1, y , a + 1.5)
                glVertex3f(x+0, y, a + 1.5)

                glNormal3f(x+3, y + 4, a + 0.5) 
                glVertex3f(x+0, y + 1, a + 0)
                glVertex3f(x+0, y + 1, a + 0.5)
                glVertex3f(x+0.5, y + 1, a + 0.5)
                glVertex3f(x+1, y + 1, a + 0)

                glVertex3f(x+0, y + 1.25, a + 0)
                glVertex3f(x+0, y + 1.25, a + 0.5)
                glVertex3f(x+1, y + 1.25, a + 0.5)
                glVertex3f(x+1, y + 1.25, a + 0.5)

                glVertex3f(x+0, y + 1, a + 0)
                glVertex3f(x+1, y + 1, a + 0)
                glVertex3f(x+1, y + 1.25, a + 0)
                glVertex3f(x+0, y + 1.25, a + 0)

                glVertex3f(x+1, y + 0, a + 0)
                glVertex3f(x+1, y + 0, a + 1)
                glVertex3f(x+1, y + 0.25, a + 1)
                glVertex3f(x+1, y + 0.25, a + 0)

                glVertex3f(x+0, y + 0, a + 0)
                glVertex3f(x+1, y + 0, a + 0)
                glVertex3f(x+1, y + 0.25, a + 0)
                glVertex3f(x+0, y + 0.25, a + 0)
                glEnd()
                




pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
camera_pos = [0, 0, -5, 0, 0, 0, 0, 1, 0]

glTranslatef(0.0,0.0,-5)
glRotatef(180, 0, 1, 0)
dragging = False
last_pos = None

move_left = False
move_right = False
move_front = False
move_back = False
move_down = False
move_up = False
rotate_right = False
rotate_left = False
x = 0
y = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            dragging = True
            last_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            mouse_pos = pygame.mouse.get_pos()
            dx = mouse_pos[0] - last_pos[0]
            dy = mouse_pos[1] - last_pos[1]
            glRotatef(dx * 0.05, 0, 0.1, 0)
            glRotatef(dy * 0.05, 0.1, 0, 0)
            last_pos = mouse_pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_UP:
                move_front = True
            elif event.key == pygame.K_DOWN:
                move_back = True
            elif event.key == pygame.K_w:
                move_up = True
            elif event.key == pygame.K_s:
                move_down = True
            elif event.key == pygame.K_a:
                rotate_left = True
            elif event.key == pygame.K_d:
                rotate_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_UP:
                move_front = False
            elif event.key == pygame.K_DOWN:
                move_back = False
            elif event.key == pygame.K_w:
                move_up = False
            elif event.key == pygame.K_s:
                move_down = False
            elif event.key == pygame.K_a:
                rotate_left = False
            elif event.key == pygame.K_d:
                rotate_right = False
    if move_left: 
        glTranslatef(-0.1, 0, 0)
    if move_right:
        glTranslatef(0.1, 0, 0)
    if move_front:
        glTranslatef(0, 0, -0.1)
    if move_back:
        glTranslatef(0, 0, 0.1)
    if move_up:
        glTranslatef(0, -0.1, 0)
    if move_down:
        glTranslatef(0, 0.1, 0)
    if rotate_right:
        glRotate(1, 0, 1, 0)
    if rotate_left:
        glRotate(-1, 0, 1, 0)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_cube()

    pygame.display.flip()

    pygame.time.wait(5)

