import pygame as pg

class Menu:
    def __init__(self,screen: pg.Surface,bgd:pg.Surface):
        self.screen=screen
        self.background=bgd
        # Chargement de l'image de fond
        self.background = pg.image.load('PygameAssets-main/Accueil.png')
        self.screen.blit(self.background, (0,0))
        # Couleurs
        self.blanc = (255, 255, 255)
        self.rouge = ("#bb0b0b")
        self.vert = (0, 255, 0)
        self.button_sound = pg.mixer.Sound("PygameAssets-main/son/son_Bouton.wav")

        # Police
        self.police = pg.font.Font(None, 40)

        # Création des boutons
        self.start_button = self.creer_bouton("Start", 680, 400, 200, 50, self.rouge)
        #self.tutorial_button = self.creer_bouton("Tutoriel", 440, 370, 200, 50, self.rouge)
        self.quit_button = self.creer_bouton("Exit", 680, 480, 200, 50, self.rouge)

    def creer_bouton(self, texte, x, y, largeur, hauteur, couleur):
        bouton = pg.Rect(x, y, largeur, hauteur)
        pg.draw.rect(self.screen, couleur, bouton)
        texte_bouton = self.police.render(texte, True, self.blanc)
        self.screen.blit(texte_bouton, (
            bouton.centerx - texte_bouton.get_width() / 2, bouton.centery - texte_bouton.get_height() / 2))
        return bouton

    def isRunning(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.start_button.collidepoint(event.pos):
                    self.button_sound.play()
                    # L'utilisateur a cliqué sur le bouton "Start"
                    # Vous pouvez ajouter ici le code pour démarrer le jeu
                    return False
                elif self.quit_button.collidepoint(event.pos):
                    self.button_sound.play()
                    pg.time.delay(300)

                    # L'utilisateur a cliqué sur le bouton "Quitter"
                    pg.quit()  # Quitter le jeu
        return True

    def isfinish(self):
        return True