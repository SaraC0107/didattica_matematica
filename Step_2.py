import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
import pygame
import pgzrun
from pgzero.builtins import Actor
from pygame import Rect
import time
import Step_1 as step_1

# ========================================================================================================================
# STEP 2: DEFINITE LE DIMENSIONI DEL PENTAGRAMMA (STAFF_WIDTH = LARGHEZZA PENTAGRAMMA, STAFF_HEIGHT = ALTEZZA PENTAGRAMMA)
# ========================================================================================================================
STAFF_WIDTH = 
STAFF_HEIGHT = 

WIDTH = step_1.WIDTH
HEIGHT = step_1.HEIGHT

background = pygame.image.load("images/background.jpg")
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

STAFF_TOP, STAFF_LEFT = 0, 0
staff_rect = Rect((STAFF_LEFT, STAFF_TOP), (STAFF_WIDTH, STAFF_HEIGHT))

def draw():
    screen.blit(background, (0, 0))
    line1_y = STAFF_TOP + (STAFF_HEIGHT // 3)
    line2_y = STAFF_TOP + 2 * (STAFF_HEIGHT // 3)

    # Draw white band between the two lines
    band_top = line1_y
    band_height = line2_y - line1_y
    screen.draw.filled_rect(Rect((STAFF_LEFT, band_top), (STAFF_WIDTH, band_height)), (255, 255, 255))

    # Draw the two staff lines
    screen.draw.line((STAFF_LEFT, line1_y), (STAFF_LEFT + STAFF_WIDTH, line1_y), (0, 0, 0))
    screen.draw.line((STAFF_LEFT, line2_y), (STAFF_LEFT + STAFF_WIDTH, line2_y), (0, 0, 0))

if __name__ == '__main__':
    pgzrun.go()