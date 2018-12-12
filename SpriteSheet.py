import json
import collections
import pygame as pg

""" Spritesheet class creates a sorted by name image list
    from a spritesheet and data atlas json file provided
"""
class SpriteSheet:
    # load an atlas image
    # can also pass an associated XML file (ref. Kenney art)
    def __init__(self, img_file, data_file=None):
        self.__spritesheet = pg.image.load(img_file).convert_alpha()
        if data_file:
            with open(data_file) as f:
                tree = json.load(f)            
            for item in tree:
                if item == 'sprites':
                    sprites = tree[item]
            sprites_dict = {}
#            self.sprite_list = []
            for sprite in sprites:
                name = sprite
                sprites_dict[name] = {}
                sprites_dict[name]['x'] = sprites[name]['x']
                sprites_dict[name]['y'] = sprites[name]['y']
                sprites_dict[name]['height'] = sprites[name]['height']
                sprites_dict[name]['width'] = sprites[name]['width']
            images = {}
            for name, rect in sprites_dict.items():
                images[name] =  self.__get_image_name(sprites_dict, name).convert_alpha()
            sorted_items = collections.OrderedDict(sorted(images.items()))
            self.sprite_images_list = []
            for name in sorted_items:
                self.sprite_images_list.append(sorted_items[name])

    def __get_image_rect(self, x, y, w, h):
        return self.__spritesheet.subsurface(pg.Rect(x, y, w, h))

    def __get_image_name(self, sprite_collection, name):
        rect = pg.Rect(sprite_collection[name]['x'], sprite_collection[name]['y'],
                       sprite_collection[name]['width'], sprite_collection[name]['height'])
        return self.__spritesheet.subsurface(rect)