import pygame
import collections
import os
from SpriteSheet import SpriteSheet

""" Creates gerald sprites and rect attributes from spritesheets"""
class Gerald(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        standing_imgs = SpriteSheet(os.path.join('resources', 'gerald_standing.png'),
                                             os.path.join('resources', 'gerald_standing.json')).sprite_images_list
        
        stand_sprite_list = self.__create_gerald_sprite_list(standing_imgs)
        # Starting Gerald sprite
        self.image = stand_sprite_list[0]
        self.rect = self.image.get_rect()
        self.width = self.rect[2]
        self.height = self.rect[3]
        self.x = self.rect[0]
        self.y = self.rect[1]
        
    def __create_gerald_sprite_list(self, image_list):
        img_background_color = [255, 127, 23]
        sprite_list = []
        for image in image_list:
            rect = image.get_rect()
            img_background = pygame.Surface((rect[2], rect[3]))
            img_background.fill(img_background_color)
            image.blit(img_background, (0,0), special_flags=pygame.BLEND_ADD)
            sprite_list.append(image)
        return sprite_list