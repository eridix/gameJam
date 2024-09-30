import pygame as pg


class Robot(pg.sprite.Sprite):
    size = (32, 32)
    screen_width = 1024
    screen_height = 768
    robokope_images = [
        pg.image.load("runR (1)-1.png.png"),
        pg.image.load("runR (1)-2.png.png"),
        pg.image.load("runR (1)-3.png.png"),
        pg.image.load("runR (1)-4.png.png"),
        pg.image.load("runR (1)-5.png.png"),
        pg.image.load("runR (1)-5.png (1).png"),
    ]

    def __init__(self,x,y , *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        #pour l'animation
        self.image = self.robokope_images[0]
        self.image_index = 0  # Index de l'image actuelle
        self.image_change_delay = 5  # Délai de changement d'image (ajustez selon la vitesse d'animation)
        self.image_counter = 0  # Compteur pour suivre le délai
        self.son_saut = pg.mixer.Sound("PygameAssets-main/son/son_saut.mp3")
        self.finish=False
        self.mort = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.vitesse_x = 2
        self.saut_en_cours = False
        self.vitesse_y = 0
        self.gravity = 0.5

        self.choix_hauteur = 0
        self.choix_tomber = 0.5

    def update(self,data):
        dt,map,finish,jump,gravite_lune,gravite_2,gravite_3,pic=data

        dx = 2
        dy = 0

        self.maplimit()

        if self.saut_en_cours:
            self.saut_en_cours = False
        else:
            if self.gravity > 10:
                self.gravity = 10
            dy += self.gravity
        self.gravity += self.choix_tomber

        #pour chaque tile dans la map
        for tile in map:
            #on vérifie si le robot est en collision avec une tile en x
            if tile.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                self.vitesse_x = 0
            # on vérifie si le robot est en collision avec une tile en x
            if tile.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.gravity < 0:
                    dy = tile.rect.bottom - self.rect.top
                elif self.gravity >= 0:
                    self.saut_en_cours = False
                    dy = tile.rect.top - self.rect.bottom
                    self.gravity = 0

        #on change l'image du robot
        self.image_counter += 1
        # Si le compteur atteint le délai
        if self.image_counter >= self.image_change_delay:
            self.image_counter = 0
            self.image_index = (self.image_index + 1) % len(self.robokope_images)
            self.image = self.robokope_images[self.image_index]


        #collision finish
        for tile in finish:
            if tile.rect.colliderect(self.rect.x + dx,self.rect.y + dy, self.width, self.height):
                self.finish=True
        #collision Pic
        for tile in pic:
            if tile.rect.colliderect(self.rect.x,self.rect.y, self.width, self.height):
                self.mort=True
        #collision jump
        for tile in jump:
            if tile.rect.colliderect(self.rect.x ,self.rect.y, self.width, self.height):
                self.sauter(self.choix_hauteur)
        #collision gravite_lune
        for tile in gravite_lune:
            if tile.rect.colliderect(self.rect.x - 32, self.rect.y + dy, self.width, self.height):
                self.setGraviteLune()
        #collision gravite_2
        for tile in gravite_2:
            if tile.rect.colliderect(self.rect.x - 32, self.rect.y + dy, self.width, self.height):
                self.setGravite2()
        #collision gravite_3
        for tile in gravite_3:
            if tile.rect.colliderect(self.rect.x - 32, self.rect.y + dy, self.width, self.height):
                self.setGravite3()

        #on mets à jour la position du robot
        self.rect.x += dx
        self.rect.y += dy
        self.rect.x += self.vitesse_x

    #on vérifie que le robot ne sorte pas de la map
    def maplimit(self):
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x >= self.screen_width - 50:
            self.rect.x = self.screen_width - 50
    #je fais sauter le robot
    def sauter(self, choix_hauteur):  # PARAMETRE A METTRE QUAND ON APPEL LA FONCTION POUR LE BLOC DE JUMP ET LE METTRE POUR SELF.GRAVITY
            self.son_saut.play()
            self.son_saut.set_volume(0.2)
            if choix_hauteur == 0:  # de base
                self.gravity = -6
            elif choix_hauteur == 1:  # pour lune
                self.gravity = -9
            elif choix_hauteur == 2:  # pour gravité 2 (saut plus loin)
                self.vitesse_x = 2
                self.gravity = -6
            elif choix_hauteur == 3:  # pour gravité 3
                self.gravity = -2
                self.vitesse_x = 2
    #vérifie si le robot est arrivé à la fin
    def isfinish(self):
        return self.finish
    #verifie si le robot est mort
    def ismort(self):
        return self.mort

    def setGraviteLune(self):
        self.choix_tomber = 0.3 #gravité (plus elle est grande plus
        self.choix_hauteur = 1 #cf sauter

    def setGravite2(self):
        self.choix_tomber = 0.5
        self.choix_hauteur = 2 #cf sauter

    def setGravite3(self):
        self.choix_tomber = 0.1
        self.choix_hauteur = 3 #cf sauter
