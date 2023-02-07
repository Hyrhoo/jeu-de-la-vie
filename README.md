
# jeu-de-la-vie

il s'agie du jeu de la vie imaginé par John Horton Conway en 1970. <br>
les regles sont simple:
- une cellule vivante reste en vie si elle est entourer de 2 ou 3 autres cellules vivantes
- une cellule morte naît si elle est entourer d'exactement 3 cellules vivantes <br>

![alt text](https://github.com/Hyrhoo/jeu-de-la-vie/blob/main/img/Capture%20d’écran%202023-02-07%20191706.png)

pour lancer el programme, il faut lancer le programme `jeu_de_la_vie.py` <br>
une fois lancer rien ne ce passe. il est possible de placer des cellules en cliquant avec la souris. <br>
il est aussi possible de faire de la génération aléatoir de grille. <br>
- la touche `1` génère une grille totalement aléatoir
- la touche `2` génère une grille aléatoir symétrique horizontalement
- la touche `3` génère une grille aléatoir symétrique verticalement
- et la touche `4` génère une grille aléatoir symétrrique horizontalement et verticalement <br>

les touches `+` et `-` (ou `=` et `6`) permetent d'augmenter ou de diminuer la vitesse de la simulation <br>
la touche `entrer` permet de lancer ou d'arrêter la simulation et la touche `effacer` permet d'effacer l'entièreté de la grille

ce programme utilise l'interface graphique pygame qu'il faut installer
