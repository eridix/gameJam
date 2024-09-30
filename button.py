import pygame as pg
import pygame.freetype

class Button(pg.sprite.Sprite):
    def __init__(self,x,y ,img,size=(64,64), *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image_originale = img
        self.image = pg.Surface(size)
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(pg.image.load('PygameAssets-main/editor/' + self.image_originale), size)
        self.rect.move_ip((x, y))


    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)

    def change_color(self,color):
        self.image.fill(color)

    def retrecir(self):
        x = self.rect.x
        y = self.rect.y
        self.rect.move_ip(10, 10)
        self.image = pg.transform.scale(pg.image.load('PygameAssets-main/editor/' + self.image_originale), (44, 44))

    def grossir(self):
        x = self.rect.x
        y = self.rect.y
        self.rect.move_ip(-10, -10)
        self.image = pg.transform.scale(pg.image.load('PygameAssets-main/editor/' + self.image_originale), (64, 64))