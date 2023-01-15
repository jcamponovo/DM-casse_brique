import pyxel

pyxel.init(128, 128, title="Nuit du c0de")

vaisseau_x = 60
vaisseau_y = 124

# initialisation des tirs
tirs_liste = []


def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 2
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 2
    return x, y
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y

    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
def draw():
    """création des objets (30 fois par seconde)"""
    
    pyxel.cls(0)

    pyxel.rect(vaisseau_x, vaisseau_y, 25, 10, 1)

def tirs_creation(x, y, tirs_liste):
    """création d'un tir avec la barre d'espace"""

    # btnr pour eviter les tirs multiples
    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs_liste.append([x+4, y-4])
    return tirs_liste

def tirs_deplacement(tirs_liste):
    """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""

    for tir in tirs_liste:
        tir[1] -= 0.8
        if  tir[1]<-8:
            tirs_liste.remove(tir)
    return tirs_liste


# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, tirs_liste

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)

    # creation des tirs en fonction de la position du vaisseau
    tirs_liste = tirs_creation(vaisseau_x, vaisseau_y, tirs_liste)

    # mise a jour des positions des tirs
    tirs_liste = tirs_deplacement(tirs_liste)


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 25, 10, 1)

    # tirs
    for tir in tirs_liste:
        pyxel.rect(tir[0], tir[1], 5, 3, 6)    
    
pyxel.run(update, draw)
