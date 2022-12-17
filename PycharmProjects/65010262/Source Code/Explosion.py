import pygame

screen_width = 1560
screen_height = 798
FPS = 64
display = pygame.display.set_mode((screen_width, screen_height))


class explosion(pygame.sprite.Sprite):
    scale_width = screen_width * 1.5
    scale_height = screen_height * 1.5

    explosion1 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Explosion\explosion-6_1.png"),
        (scale_width, scale_height))
    explosion2 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Explosion\explosion-6_2.png"),
        (scale_width, scale_height))
    explosion3 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Explosion\explosion-6_3.png"),
        (scale_width, scale_height))
    explosion4 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Explosion\explosion-6_4.png"),
        (scale_width, scale_height))
    explosion5 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Explosion\explosion-6_5.png"),
        (scale_width, scale_height))
    explosion6 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Explosion\explosion-6_6.png"),
        (scale_width, scale_height))
    explosion7 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Explosion\explosion-6_7.png"),
        (scale_width, scale_height))
    explosion8 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Explosion\explosion-6_8.png"),
        (scale_width, scale_height))
    boom = [explosion1, explosion2, explosion3, explosion4, explosion5, explosion6, explosion7, explosion8]
    def __init__(self):
        self.boomCount = 0
        self.show = False

    def draw(self, display):
        if self.show:
            if self.boomCount + 1 > FPS:
                self.show = False
            else:
                display.blit(self.boom[self.boomCount // 8], (-200, -200))
                self.boomCount += 4
