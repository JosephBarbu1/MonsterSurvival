import pygame
from settings import *

def check_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def update_screen(screen, player):
    screen.fill(BLACK)
    # Draw player and other game elements here
    pygame.display.flip()
