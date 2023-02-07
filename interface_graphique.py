# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:22:15 2022

@author: jojoj
"""

import pygame
pygame.init()

resolution = (1000, 700)
noir = (54, 57, 63)

pygame.display.set_caption("jeu de la vie")
fenetre_de_jeu = pygame.display.set_mode(resolution)
fenetre_de_jeu.fill(noir)

def dessiner_le_tableau(tableau):
    fenetre_de_jeu.fill(noir)
    for i in range(len(tableau)):
        for y,z in enumerate(tableau[i]):
            if z == 1:
                rectangle = pygame.Rect(y*20, i*20, 20, 20)
                pygame.draw.rect(fenetre_de_jeu, (100,100,100), rectangle)
    pygame.display.flip()
