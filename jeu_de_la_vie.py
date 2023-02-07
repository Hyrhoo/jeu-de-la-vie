# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:08:24 2022

@author: jojoj
"""

from random import randint, choice
from time import monotonic
from copy import deepcopy
from interface_graphique import *

tableau_jeu_vie = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

def verif_vie(pos):
    celules = 0
    for i in range (-1, 2):
        for y in range (-1, 2):
            n_pos = [pos[0]+i, pos[1]+y]
            if n_pos[0] > len(tableau_du_jeu_de_la_vie)-1: n_pos[0] = 0
            if n_pos[1] > len(tableau_du_jeu_de_la_vie[0])-1: n_pos[1] = 0
            if tableau_du_jeu_de_la_vie[n_pos[0]][n_pos[1]] == 1 and n_pos != pos: celules += 1
    return celules

def verif_vie_tableau():
    les_vie = []
    les_mort = []
    for hauteur in range(len(tableau_du_jeu_de_la_vie)):
        for largeur,case in enumerate(tableau_du_jeu_de_la_vie[hauteur]):
            position = [hauteur,largeur]
            #print([i-1 for i in position], position)
            celules = verif_vie(position)
            vie = False
            if case == 1:
                if celules in (2,3):
                    vie = True
            elif case == 0:
                if celules == 3:
                    vie = True
            if vie:
                les_vie.append(position)
            else:
                les_mort.append(position)
    return les_vie, les_mort

def random_grille(touche):
    if touche == 1:
        for i in range(len(tableau_du_jeu_de_la_vie)):
            for y in range(len(tableau_du_jeu_de_la_vie[i])):
                tableau_du_jeu_de_la_vie[i][y] = choice([0, 0, 1])
    elif touche == 2:
        for i in range(len(tableau_du_jeu_de_la_vie)):
            for y in range(len(tableau_du_jeu_de_la_vie[1])):
                tableau_du_jeu_de_la_vie[i][y] = choice([0, 0, 1])
        for i in range(len(tableau_du_jeu_de_la_vie)//2):
            for y in range(len(tableau_du_jeu_de_la_vie[1])):
                tableau_du_jeu_de_la_vie[len(tableau_du_jeu_de_la_vie)-i-1][y] = tableau_du_jeu_de_la_vie[i][y]
    elif touche == 3:
        for i in range(len(tableau_du_jeu_de_la_vie)):
            for y in range(len(tableau_du_jeu_de_la_vie[i])):
                tableau_du_jeu_de_la_vie[i][y] = choice([0, 0, 1])
        for y in range(len(tableau_du_jeu_de_la_vie[1])//2):
            for i in range(len(tableau_du_jeu_de_la_vie)):
                tableau_du_jeu_de_la_vie[i][len(tableau_du_jeu_de_la_vie[1])-y-1] = tableau_du_jeu_de_la_vie[i][y]
    elif touche == 4:
        for i in range(len(tableau_du_jeu_de_la_vie)):
            for y in range(len(tableau_du_jeu_de_la_vie[i])):
                tableau_du_jeu_de_la_vie[i][y] = choice([0, 0, 1])
        for i in range(len(tableau_du_jeu_de_la_vie)):
            for y in range(len(tableau_du_jeu_de_la_vie[1])):
                tableau_du_jeu_de_la_vie[len(tableau_du_jeu_de_la_vie)-i-1][y] = tableau_du_jeu_de_la_vie[i][y]
                tableau_du_jeu_de_la_vie[i][len(tableau_du_jeu_de_la_vie[1])-y-1] = tableau_du_jeu_de_la_vie[i][y]

Clock = pygame.time.Clock()
temps_0 = monotonic()
fini = False
generation = 1
commencer = False
attand = 0.25
tableau_du_jeu_de_la_vie = deepcopy(tableau_jeu_vie)
while not fini:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                fini=True
            if event.key == 13:
                commencer = not commencer
            if event.key == 61:
                attand += 0.01
                attand = round(attand, 2)
                if attand > 10:
                    attand = 10.00
                print(attand)
            if event.key == 54:
                attand -= 0.01
                attand = round(attand, 2)
                if attand < 0:
                    attand = 0.00
                print(attand)
            if event.key == 8 and not commencer:
                tableau_du_jeu_de_la_vie = deepcopy(tableau_jeu_vie)
                generation = 0
            elif event.key == 49 and not commencer:
                random_grille(1)
                generation = 0
            elif event.key == 50 and not commencer:
                random_grille(2)
                generation = 0
            elif event.key == 51 and not commencer:
                random_grille(3)
                generation = 0
            elif event.key == 52 and not commencer:
                random_grille(4)
                generation = 0
        if event.type == pygame.MOUSEBUTTONUP and not commencer:
            tableau_du_jeu_de_la_vie[event.pos[1]//20][event.pos[0]//20] = int(not bool(tableau_du_jeu_de_la_vie[event.pos[1]//20][event.pos[0]//20]))
    dessiner_le_tableau(tableau_du_jeu_de_la_vie)
    #for i in tableau_du_jeu_de_la_vie:
        #print(i)
    if commencer:
        if monotonic() > temps_0 + attand:
            temps_0 = monotonic()
            #print("actualisation", ifd)
            les_vie, les_mort = verif_vie_tableau()
            for i in les_vie:
                tableau_du_jeu_de_la_vie[i[0]][i[1]] = 1
            for i in les_mort:
                tableau_du_jeu_de_la_vie[i[0]][i[1]] = 0
            commencer = False
            for i in tableau_du_jeu_de_la_vie:
                for y in i:
                    if y == 1:
                        commencer = True
            generation += 1
            print("nbr generation:", generation)
    Clock.tick(60)
            
    #print("fin de la boucle")
pygame.quit()