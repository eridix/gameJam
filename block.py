import pygame as pg

class Block(pg.sprite.Sprite):
    size = (32,32)
    def __init__(self,x,y, img , *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = pg.Surface(self.size)
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(pg.image.load('PygameAssets-main/bloc/' + img), (32, 32))
        self.rect.move_ip((x, y))
