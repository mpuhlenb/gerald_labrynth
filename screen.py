# its the screen class file
import pygame
#from pygame import local *
import os


class Screen():
    def __init__(self):
        pygame.display.init()
        # screen parameters
        height = 1008
        width = 1792
        self.red = 200
        self.green = 200
        self.blue = 200
        # starting with gray
        self.screen_color = [self.red, self.green, self.blue]
        self.surface = pygame.display.set_mode((width, height))
        # Start with the cracks image
        self.background = pygame.image.load(os.path.join('resources', 'cracks.png')).convert_alpha()
        self.background_color = pygame.Surface(self.surface.get_size())
        # Make a colored background
        self.background_color.convert()
        self.background_color.fill(self.screen_color)
        # Blit both to 1 surface which will be used for updating display
        self.total_bgd = pygame.Surface(self.surface.get_size())
        self.total_bgd.convert_alpha()
        self.total_bgd.blit(self.background_color, (0,0))
        self.total_bgd.blit(self.background,(0,0))
        # Blit total background onto surface initially
        self.surface.blit(self.total_bgd, (0,0))
        self.rect = self.surface.get_rect()
