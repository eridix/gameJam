import pygame as pg
import map
import button

class Niveau:
    def __init__(self, screen: pg.Surface,bgd:pg.Surface,data_map,mode=1,nb_jump=9,gravites=(1,1,1)):
        self.data_map=data_map
        self.background=bgd
        self.screen = screen
        self.bg_image = pg.transform.scale(pg.image.load('PygameAssets-main/bg_level.jpg'), (1024,768))

        self.map = map.Map(self.screen,bgd,self.data_map)
        self.all_button = pg.sprite.RenderUpdates()
        self.all = pg.sprite.RenderUpdates()

        #Mode de jeu 1=creation / 2=action
        self.mode=mode
        self.finish = False
        #Boutons
        self.jump_button = button.Button(300, 650, 'tremplinEditor.png')
        self.nb_jump=nb_jump
        self.all_button.add(self.jump_button)

        self.gravite1,self.gravite2,self.gravite3=gravites
        if self.gravite1==1:
            self.gravite1_button = button.Button(400, 650, 'moon.png')
            self.all_button.add(self.gravite1_button)
        if self.gravite2==1:
            self.gravite2_button = button.Button(500, 650, 'earth.png')
            self.all_button.add(self.gravite2_button)
        if self.gravite3==1:
            self.gravite3_button = button.Button(600, 650, 'jupiter.png')
            self.all_button.add(self.gravite3_button)
        #Attention si on ajoute des boutons il faudra modifier le code du bouton supprimer plus loin (actuellement à 5)
        self.button_supp = button.Button(700, 650, 'bin.png')
        self.all_button.add(self.button_supp)

        # Police
        self.police = pg.freetype.Font(None, 18)

        #Objet selctionné pour ajouter sur la map
        self.obj_select=0 #Initilisé à 0, 1 pour test_button, 10 pour la suppression

    def isRunning(self):
        if self.mode==1: #Mode Creation
            self.all.add(self.all_button)
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.event_pos_x, self.event_pos_y = event.pos
                    i=0
                    bouton_collision=False
                    for bouton in self.all_button:
                        if bouton.collidepoint(event.pos):
                            bouton_collision=True
                            if self.obj_select != i+1:
                                self.obj_select = i+1
                                for onebutton in self.all_button:
                                    if onebutton.image.get_width()==44:
                                        onebutton.grossir()
                                bouton.retrecir()
                            else:
                                self.obj_select = 0
                                bouton.grossir()
                        i+=1
                    #Cas ou il y a pas de bloc au clic
                    if not bouton_collision and self.data_map[self.event_pos_y//32][self.event_pos_x//32]==0: #0 est le vide
                        for a in range(i-1):
                            if self.obj_select == a+1:
                                if self.obj_select!=1:
                                    self.data_map[self.event_pos_y // 32][self.event_pos_x // 32] = 50 + a * 2
                                elif self.nb_jump>0:
                                    self.nb_jump -= 1
                                    self.data_map[self.event_pos_y // 32][self.event_pos_x // 32] = 50 + a * 2
                                self.map.update_map()
                    elif not bouton_collision and self.data_map[self.event_pos_y // 32][self.event_pos_x // 32] >= 50:
                        if self.obj_select==i:#Attention bouton suppression
                            if self.data_map[self.event_pos_y // 32][self.event_pos_x // 32]==50:
                                self.nb_jump+=1
                            self.data_map[self.event_pos_y // 32][self.event_pos_x // 32] = 0
                            self.map.dell_block((self.event_pos_x // 32)*32,(self.event_pos_y // 32)*32)
                            return False
                elif event.type ==pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        #print("Entrer")
                        self.mode=2
                        self.all.remove(self.all_button)
            return True
        elif self.mode==2: #Mode Action
            if self.map.isfinish():
                self.finish = True
                return False
            elif self.map.ismort():
                return False
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        #print("Entrer")
                        return False
            return True
        elif self.mode == 3: #Mode cinématique debut
            if self.map.isfinish():
                self.finish=True
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_RETURN:
                            self.mode=2
            return True
        elif self.mode == 4: #Mode cinématique fin
            if self.map.isfinish():
                self.finish=True
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_RETURN:
                            self.mode=2
            return True

    def isfinish(self):
        return self.finish


    def update(self,dt:int):
        if self.mode!=1:
            self.map.update(dt)
        self.all.update(dt)
        self.all.clear(self.screen, self.background)
        self.screen.blit(self.bg_image, (0,0))
        pg.display.update(self.map.draw(self.screen))
        pg.display.update(self.all.draw(self.screen))
        if self.mode==1:
            self.police.render_to(self.screen, (75, 20), "Appuyez sur Entrée pour démarrer", "black")
            self.police.render_to(self.screen, (320, 720), self.nb_jump.__str__(), "black")
        if self.mode==2:
            self.police.render_to(self.screen, (90, 20), "Appuyer sur Entrer pour restart ", "black")
        if self.mode==3:
            self.police.render_to(self.screen, (100, 100),"Il était une fois, dans un laboratoire spatial un robot nommé R-3000 qui rêvait de liberté.","white")
            self.police.render_to(self.screen, (100, 130), "Son créateur, M. Smith, avait d'autres projets sinistres pour lui.", "white")
            self.police.render_to(self.screen, (100, 160),"R-3000 entreprit alors son évasion, un voyage épique pour échapper à M. Smith et à son laboratoire.","white")
            if self.finish:
                self.police.render_to(self.screen, (300, 250), "Appuyez sur Entrée pour démarrer", "black")
        if self.mode==4:
            self.police.render_to(self.screen, (150, 100),"R-3000 a réussi à s'échapper de M. Smith grâce à vous. Il est enfin libre et heureux.","white")
            if self.finish:
                self.police.render_to(self.screen, (300, 250), "Appuyez sur Entrée pour terminer le jeu", "black")