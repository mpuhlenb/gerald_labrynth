import pygame

class Gerald(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 100
        self.height = 150
        self.img_bak = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.img_bak.get_rect()
        self.img_bak.fill([255, 127, 23])
        self.image = self.img_bak
        self.x = self.rect[0]
        self.y = self.rect[1]