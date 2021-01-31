import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGl.GLU import *

#Vértices
Vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

#Arestas
Arestas = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

def Cubo():
    glBegin(GL_LINES)
    
    for Vertice in Vertices:
        for verticeX in Arestas:
            glVertex3fv(Vertices[verticeX])
    
    glEnd()