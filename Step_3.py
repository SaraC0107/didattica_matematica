import pygame
import pgzrun
from pgzero.builtins import Actor
from pygame import Rect
import time
import Step_1 as step_1
import Step_2 as step_2

# =============================================
# STEP 3: ASSOCIATE I COLORI AI NOMI DELLE NOTE
# =============================================
NOTE_MAP = {
    '':    ('DO','do'),
    '':    ('RE', 're'),
    '':    ('MI', 'mi'),
    '':    ('FA', 'fa'),
    '':    ('SOL', 'sol'),
    '':    ('LA', 'la'),
    '':    ('SI', 'si'),
}

WIDTH = step_1.WIDTH
HEIGHT = step_1.HEIGHT
background = pygame.image.load("images/background.jpg")
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

STAFF_TOP, STAFF_LEFT = step_2.STAFF_TOP, step_2.STAFF_LEFT
STAFF_WIDTH, STAFF_HEIGHT = step_2.STAFF_WIDTH, step_2.STAFF_HEIGHT
staff_rect = Rect((STAFF_LEFT, STAFF_TOP), (STAFF_WIDTH, STAFF_HEIGHT))

# Create circle actors below the staff
placed_notes = []
circles = []
start_x, gap_y = 60, 75

def draw():
    screen.blit(background, (0, 0))
    # Staff background
    # screen.draw.filled_rect(staff_rect, (245, 245, 245))
    # Two horizontal staff lines with white space between
    line1_y = STAFF_TOP + (STAFF_HEIGHT // 3)
    line2_y = STAFF_TOP + 2 * (STAFF_HEIGHT // 3)

    # Draw white band between the two lines
    band_top = line1_y
    band_height = line2_y - line1_y
    screen.draw.filled_rect(Rect((STAFF_LEFT, band_top), (STAFF_WIDTH, band_height)), (255, 255, 255))

    # Draw the two staff lines
    screen.draw.line((STAFF_LEFT, line1_y), (STAFF_LEFT + STAFF_WIDTH, line1_y), (0, 0, 0))
    screen.draw.line((STAFF_LEFT, line2_y), (STAFF_LEFT + STAFF_WIDTH, line2_y), (0, 0, 0))
    
    for idx, colour in enumerate(NOTE_MAP.keys()):
        a = Actor(f'{colour}', (STAFF_LEFT + 450 + idx * 50, STAFF_TOP + STAFF_HEIGHT + 250))
        a._surf = pygame.transform.smoothscale(a._surf, (50, 50))
        a._update_pos()
        a.anchor = ('center', 'center')
        a.colour_name = colour
        circles.append(a)
    
    # Draw placed notes on staff
    for n in placed_notes:
        n.draw()
    # Draw draggable circles below staff
    for c in circles:
        c.draw()

if __name__ == '__main__':
    pgzrun.go()