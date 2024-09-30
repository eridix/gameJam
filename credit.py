import pygame as pg

# pygame.init()
# pygame.display.set_caption('Crédits de fin')
# écran = pygame.display.set_mode((1024, 768))
# fond = pygame.Surface(écran.get_size())
class Credit:
    def __init__(self, screen: pg.Surface,bgd:pg.Surface):
        self.taille_police = 40
        self.police = pg.font.SysFont("Arial", self.taille_police)
        self.fond=bgd
        self.screen = screen
        self.hauteur=self.screen.get_height()
        self.en_cours=True
        self.liste = [
                "CRÉDITS - R-JUMP-3000",
                "",
                "Développé en Python avec la bibliothèque Pygame",
                "",
                "Groupe de développement :",
                "Tomoji",
                "",
                "Équipe de développement :",
                "Paul MATHIEU",
                "Muhamed HODZIC",
                "Fares MEDJAHED",
                "Jean-Emmanuel AUDEOUD",
                "",

                "Responsable de la Gamejam :",
                "Jean Pierre Chevalet",
                "",
                "Date de réalisation :",
                "Du 18/09/2023 au 22/09/2023",
                "",
                "Musique et effets sonores :",
                "- sources",
                    "Karmen Sally - Youtube",
            "Premium Music HQ - Youtube - INFINITY",
            "https://lasonotheque.org/",
                "Assets",
                 " - Jean Emmanuel AUDEOUD",

                "Merci d'avoir joué à R-JUMP-3000 !"
            ]

    def afficher_texte(self,y):
        self.fond.fill((0, 0, 0))
        for ligne in self.liste:
            surface_texte = self.police.render(ligne, 1, (255, 255, 255))
            rect_texte = surface_texte.get_rect(center=(self.fond.get_rect().centerx, y))
            self.fond.blit(surface_texte, rect_texte)
            y += 45

        self.screen.blit(self.fond, (0, 0))
        pg.display.flip()
        pg.time.delay(20)
        self.en_cours = False



    def isRunning(self):
        if self.hauteur > (0 - len(self.liste) * 50):
            self.afficher_texte(self.hauteur)
            self.hauteur -= 1
            return True
        return self.en_cours



    def isfinish(self):
        return True



