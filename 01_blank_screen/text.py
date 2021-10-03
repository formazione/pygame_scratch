import pygame
from start import *
from events import *

# From starts
screen_size = get_screen_size(offset=50)
screen = pygame.display.set_mode(screen_size)

# From events
gameloop()