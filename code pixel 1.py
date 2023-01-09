import pyxel

# Largeur et hauteur de la fenêtre de jeu
WIDTH = 240
HEIGHT = 160

# Constantes pour la taille de la balle et de la raquette
BALL_SIZE = 4
PADDLE_WIDTH = 48
PADDLE_HEIGHT = 8

# Constantes pour la vitesse de la balle et de la raquette
BALL_SPEED = 2
PADDLE_SPEED = 4

# Variables pour la position de la balle et de la raquette
ball_x = 0
ball_y = 0
paddle_x = 0
paddle_y = 150

# Variable pour la direction de la balle (1 = vers la droite, -1 = vers la gauche)
ball_dir = 1

# Initialise le jeu
def init():
    # Initialise l'écran de jeu
    pyxel.init(WIDTH, HEIGHT)
    
    # Place la balle et la raquette au milieu de l'écran
    global ball_x, ball_y, paddle_x
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2

# Met à jour l'état du jeu
def update():
    global ball_x, ball_y, paddle_x, ball_dir
    
    # Déplace la raquette si les flèches gauche et droite sont enfoncées
    if pyxel.btn(pyxel.KEY_LEFT) and paddle_x > 0:
        paddle_x -= PADDLE_SPEED
    if pyxel.btn(pyxel.KEY_RIGHT) and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += PADDLE_SPEED
    
    # Déplace la balle
    ball_x += BALL_SPEED * ball_dir
    ball_y += BALL_SPEED
    
    # Inverse la direction de la balle si elle touche un bord
    if ball_x <= 0 or ball_x >= WIDTH - BALL_SIZE:
        ball_dir = -ball_dir
    if ball_y <= 0:
        ball_y = 0
    
    # Si la balle touche la raquette, renvoie la balle dans l'autre sens
    if (
        ball_x >= paddle_x and ball_x <= paddle_x + PADDLE_WIDTH
        and ball_y + BALL_SIZE >= paddle_y
    ):
        ball_y = paddle_y - BALL_SIZE
        ball_dir = (ball_x - paddle_x) // PADDLE_WIDTH - 1

# Dessine l'écran de jeu
def draw():
    # Efface l'écran
    pyxel.cls(0)
    
    # Dessine la balle et la raquette
    pyx el.rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT, 9)
    pyxel.rect(ball_x, ball_y, BALL_SIZE, BALL_SIZE, 11)
  
init()
pyxel.run(update, draw

 

