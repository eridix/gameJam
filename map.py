import pygame as pg

import button
import robot
import block

class Map:
    def __init__(self,screen: pg.Surface,bgd:pg.Surface, data_map:[[]]):
        self.background=bgd
        self.map=pg.sprite.Group()
        self.robot=pg.sprite.Group()
        self.finish=pg.sprite.Group()
        self.pic=pg.sprite.Group()
        self.jump = pg.sprite.Group()
        self.gravity_lune = pg.sprite.Group()
        self.gravity_2 = pg.sprite.Group()
        self.gravity_3 = pg.sprite.Group()
        self.all = pg.sprite.Group()
        self.screen = screen
        self.data_map=data_map

        self.update_map()

    def draw(self,screen: pg.Surface):
        self.all.draw(screen)
        self.robot.draw(screen)

    def update(self,dt):
        arg=(dt,self.map,self.finish,self.jump,self.gravity_lune,self.gravity_2,self.gravity_3,self.pic)
        self.robot.update(arg)
        self.map.update()
        self.finish.update()
        self.pic.update()
        self.jump.update()
        self.gravity_lune.update()
        self.gravity_2.update()
        self.gravity_3.update()
        self.robot.clear(self.screen,self.background)
        self.all.clear(self.screen,self.background)

    def update_map(self):
        self.screen.blit(self.background, (0, 0))
        pos_y = 0
        for line in self.data_map:
            pos_x = 0
            for element_decor in line:
                if element_decor == 1:
                    self.robot.add(robot.Robot(pos_x * 32, pos_y * 32))
                elif element_decor == 2:
                    self.map.add(block.Block(pos_x * 32, pos_y * 32, 'sol_plein.png'))
                elif element_decor == 3:
                    self.finish.add(block.Block(pos_x * 32, pos_y * 32, 'porteFinish.png'))
                elif element_decor ==4:
                    self.pic.add(block.Block(pos_x * 32, pos_y * 32, 'pics.png'))
                elif element_decor ==5:
                    self.pic.add(block.Block(pos_x * 32, pos_y * 32, 'pics_bottom.png'))
                elif element_decor ==6:
                    self.pic.add(block.Block(pos_x * 32, pos_y * 32, 'pics_right.png'))
                elif element_decor == 7:
                    self.pic.add(block.Block(pos_x * 32, pos_y * 32, 'pics_left.png'))
                elif element_decor ==8:
                    self.map.add(block.Block(pos_x * 32, pos_y * 32, 'sol.png'))
                elif element_decor ==10:
                    self.map.add(block.Block(pos_x * 32, pos_y * 32, 'bloc_middle.png'))
                elif element_decor ==11:
                    self.map.add(block.Block(pos_x * 32, pos_y * 32, 'bloc_right.png'))
                elif element_decor ==12:
                    self.map.add(block.Block(pos_x * 32, pos_y * 32, 'bloc_left.png'))
                elif element_decor == 50:
                    self.jump.add(button.Button(pos_x * 32, pos_y * 32, 'tremplinEditor.png',(32,32)))
                elif element_decor == 52:
                    self.gravity_lune.add(button.Button(pos_x * 32, pos_y * 32, 'moon.png',(32,32)))
                elif element_decor == 54:
                    self.gravity_2.add(button.Button(pos_x * 32, pos_y * 32, 'earth.png',(32,32)))
                elif element_decor == 56:
                    self.gravity_3.add(button.Button(pos_x * 32, pos_y * 32, 'jupiter.png',(32,32)))
                pos_x += 1
            pos_y += 1
        self.all.add((self.map,self.jump,self.pic,self.finish,self.gravity_lune,self.gravity_2,self.gravity_3))

    def dell_block(self,x,y):
        for sprite in self.gravity_lune:
            if sprite.rect[0]==x and sprite.rect[1]==y:
                self.map.remove(sprite)
                self.update(0)
        for sprite in self.gravity_2:
            if sprite.rect[0]==x and sprite.rect[1]==y:
                self.map.remove(sprite)
                self.update(0)
        for sprite in self.gravity_3:
            if sprite.rect[0]==x and sprite.rect[1]==y:
                self.map.remove(sprite)
                self.update(0)
        for sprite in self.jump:
            if sprite.rect[0]==x and sprite.rect[1]==y:
                self.map.remove(sprite)
                self.update(0)

    def isfinish(self):
        finish=True
        for r in self.robot:
            finish=finish & r.isfinish()
        return finish

    def ismort(self):
        mort=False
        for r in self.robot:
            mort=mort | r.ismort()
        return mort