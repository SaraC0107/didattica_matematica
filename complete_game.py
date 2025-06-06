import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
import pygame
import pgzrun
from pgzero.builtins import Actor
from pygame import Rect
import time

WIDTH, HEIGHT = 900, 600

background = pygame.image.load("images/background.jpg")
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

# Map circle colours to their note names and sound stems
NOTE_MAP = {
    'red':    ('DO','do'),
    'green':  ('RE', 're'),
    'blue':   ('MI', 'mi'),
    'yellow': ('FA', 'fa'),
    'purple': ('SOL', 'sol'),
    'orange': ('LA', 'la'),
    'pink':   ('SI', 'si'),
}

# Define the staff (pentagram) area
STAFF_TOP, STAFF_LEFT = 50, 0
STAFF_WIDTH, STAFF_HEIGHT = WIDTH, 250
staff_rect = Rect((STAFF_LEFT, STAFF_TOP), (STAFF_WIDTH, STAFF_HEIGHT))

placed_notes = []
play_button = Actor("play_button", (WIDTH - 25, HEIGHT+100))
# Scale the play_button right after creation
play_button._surf = pygame.transform.smoothscale(play_button._surf, (80, 60))
play_button._update_pos()

erase_button = Actor("erase_button", (play_button.x, play_button.y))
erase_button._surf = pygame.transform.smoothscale(erase_button._surf, (100, 60))
erase_button._update_pos()

# Create circle actors below the staff
circles = []
start_x, gap_y = 60, 75
for idx, colour in enumerate(NOTE_MAP.keys()):
    a = Actor(f'{colour}', (STAFF_LEFT + 450 + idx * 50, STAFF_TOP + STAFF_HEIGHT + 250))
    a._surf = pygame.transform.smoothscale(a._surf, (50, 50))
    a._update_pos()
    a.anchor = ('center', 'center')
    a.colour_name = colour
    circles.append(a)

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
    # Draw placed notes on staff
    for n in placed_notes:
        n.draw()
    # Draw draggable circles below staff
    for c in circles:
        c.draw()
    # Draw play button
    play_button.draw()
    erase_button.draw()

def on_mouse_down(pos):
    # Check if a placed note was clicked to remove it
    for note in reversed(placed_notes):
        if note.collidepoint(pos):
            placed_notes.remove(note)
            # Reposition all notes to fill the gap
            for i, n in enumerate(placed_notes):
                n.x = STAFF_LEFT + 175 + i * 60
            return
    # Check if a circle is clicked to place a copy on the staff
    for c in reversed(circles):
        if c.collidepoint(pos):
            x_pos = STAFF_LEFT + 175 + len(placed_notes) * 60
            y_pos = STAFF_TOP + 275
            new_note = Actor(f"{c.colour_name}", (x_pos, y_pos))
            new_note._surf = pygame.transform.smoothscale(new_note._surf, (50, 50))
            new_note._update_pos()
            new_note.colour_name = c.colour_name
            placed_notes.append(new_note)
            return
    # Check if play button clicked
    if play_button.collidepoint(pos):
        play_sequence()
    if erase_button.collidepoint(pos):
        placed_notes.clear()

def on_mouse_up(pos):
    pass

def on_key_down(key):
    if key == keys.SPACE:
        play_sequence()

def play_sequence():
    """Play notes for all placed notes on the staff, left to right."""
    def play_note_at_index(idx):
        if idx >= len(placed_notes):
            return
        note = placed_notes[idx]
        sound_stem = NOTE_MAP[note.colour_name][1]
        getattr(sounds, sound_stem).play()
    if placed_notes:
        for i in range(len(placed_notes)):
            play_note_at_index(i)
            time.sleep(0.5)

pgzrun.go()

def update():
    pass

def on_mouse_move(pos):
    pass