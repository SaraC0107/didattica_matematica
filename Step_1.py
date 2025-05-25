import pygame
import pgzrun
from pgzero.builtins import Actor
from pygame import Rect
import time

# ============================================================================================
# STEP 1: DEFINITE LE DIMENSIONI DELLA FINESTRA DI GIOCO (WIDTH = LARGHEZZA, HEIGHT = ALTEZZA)
# ============================================================================================
WIDTH = 
HEIGHT = 

background = pygame.image.load("images/background.jpg")
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

def draw():
    screen.blit(background, (0, 0))

if __name__ == '__main__':
    pgzrun.go()