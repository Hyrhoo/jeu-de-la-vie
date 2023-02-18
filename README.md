
# jeu-de-la-vie

> Ce programme utilise la bibliothèque graphique **pygame** qu'il faut installer préalablement.

Il s'agit du jeu de la vie imaginé par John Horton Conway en 1970. <br>
Les regles sont simple:
- une cellule vivante reste en vie si elle est entourer de 2 ou 3 autres cellules vivantes
- une cellule morte naît si elle est entourée d'exactement 3 cellules vivantes <br>

![alt text](https://github.com/Hyrhoo/jeu-de-la-vie/blob/main/img/Capture%20d’écran%202023-02-07%20191706.png)

Pour lancer le programme, il faut lancer `jeu_de_la_vie.py`. <br>
Une fois lancé une nouvelle fenêtre s'ouvre: il est possible de placer des cellules en cliquant avec la souris. <br>
Il est aussi possible de faire de la génération aléatoir de grille avec les touches numériques du haut du clavier. <br>
- la touche `1` génère une grille totalement aléatoire
- la touche `2` génère une grille aléatoire symétrique horizontalement
- la touche `3` génère une grille aléatoire symétrique verticalement
- et la touche `4` génère une grille aléatoire symétrique horizontalement et verticalement <br>

Les touches `+` et `-` (ou `=` et `6`) permettent d'augmenter ou de diminuer la vitesse de la simulation. <br>
La touche `entrer` permet de lancer ou d'arrêter la simulation et la touche `effacer` permet d'effacer l'entièreté de la grille.  
La touche `esc` permet de quitter le programme.
