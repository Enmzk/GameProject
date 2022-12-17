import pygame

FPS = 64
screen_width = 1560
screen_height = 798
display = pygame.display.set_mode((screen_width, screen_height))
game_clock = pygame.time.get_ticks()

class archer(pygame.sprite.Sprite):
    scale_width = 410
    scale_height = 410

    run1 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\run1.png"),
        (scale_width, scale_height))
    run2 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\run2.png"),
        (scale_width, scale_height))
    run3 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\run3.png"),
        (scale_width, scale_height))
    run4 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\run4.png"),
        (scale_width, scale_height))
    run5 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\run5.png"),
        (scale_width, scale_height))
    run6 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\run6.png"),
        (scale_width, scale_height))
    run7 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\run6.png"),
        (scale_width, scale_height))
    run8 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\run7.png"),
        (scale_width, scale_height))
    runRight = [run1, run2, run3, run4, run5, run6, run7, run8]
    runLeft = [pygame.transform.flip(run1, True, False),
                  pygame.transform.flip(run2, True, False),
                  pygame.transform.flip(run3, True, False),
                  pygame.transform.flip(run4, True, False),
                  pygame.transform.flip(run5, True, False),
                  pygame.transform.flip(run6, True, False),
                  pygame.transform.flip(run7, True, False),
                  pygame.transform.flip(run8, True, False),
                  ]

    arrow = pygame.transform.scale(pygame.image.load(r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\arrow.png'), (scale_width, scale_height))
    attack1 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\attack1.png"),
        (scale_width, scale_height))
    attack2 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\attack2.png"),
        (scale_width, scale_height))
    attack3 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\attack3.png"),
        (scale_width, scale_height))
    attack4 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\attack4.png"),
        (scale_width, scale_height))
    attack5 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\attack5.png"),
        (scale_width, scale_height))
    attack6 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\attack6.png"),
        (scale_width, scale_height))
    attack7 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\attack6.png"),
        (scale_width, scale_height))
    attack8 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\attack7.png"),
        (scale_width, scale_height))
    attackRight = [attack1, attack2, attack3, attack4, attack5, attack6, attack7, attack8]
    attackLeft = [pygame.transform.flip(attack1, True, False),
                  pygame.transform.flip(attack2, True, False),
                  pygame.transform.flip(attack3, True, False),
                  pygame.transform.flip(attack4, True, False),
                  pygame.transform.flip(attack5, True, False),
                  pygame.transform.flip(attack6, True, False),
                  pygame.transform.flip(attack7, True, False),
                  pygame.transform.flip(attack8, True, False),
                  ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 1500
        self.y = 450
        self.posx = 1260
        self.width = 250
        self.height = 250
        self.atk = 6
        self.atkspd = 1
        self.attackCount = 0
        self.hp = 13
        self.hp_max = self.hp
        self.vel = -3
        self.runCount = 0
        self.facing = -1
        self.hitbox = (self.x + 140, self.y + 20, 230, 230)
        self.greenBar = 0
        self.redBar = 0

    def draw(self, display):
        self.move()
        self.hitbox = (self.x + 140, self.y + 20, 230, 230)
        self.greenBar = (self.hp / self.hp_max) * (50)
        self.redBar = (self.hp_max / self.hp_max) * (50)
        pygame.draw.rect(display, (255, 0, 0),
                         (self.hitbox[0] + 20, self.hitbox[1] - 20, self.redBar, 10))  # RedHealthBar
        pygame.draw.rect(display, (0, 255, 0),
                         (self.hitbox[0] + 20, self.hitbox[1] - 20, self.greenBar, 10))  # GreenHealthBar

    def move(self):
        if self.hp > 0:
            if self.x != self.posx:
                self.x += self.vel
                display.blit(self.runLeft[self.runCount // 8], (self.x, self.y - 70))
                self.runCount += 2
                if self.runCount + 1 > FPS:
                    self.runCount = 0
            else:
                if self.attackCount + 1 > FPS:
                    self.attackCount = 0
                else:
                    if self.facing == 1:
                        display.blit(self.attackRight[self.attackCount // 8], (self.x, self.y - 50))
                        self.attackCount += self.atkspd
                    else:
                        display.blit(self.attackLeft[self.attackCount // 8], (self.x, self.y - 70))
                        self.attackCount += self.atkspd
                    if self.attackCount == 56:
                        archer_arrow(self.x, self.y, self.facing)

class archer_arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, facing):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y + 90
        self.width = 200
        self.height = 25
        self.facing = facing
        self.vel = 15 * facing

    def draw(self, display):
        arrowRight = pygame.transform.scale(pygame.image.load(r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Arcane archer\arrow.png'), (self.width, self.height))
        arrowLeft = pygame.transform.flip(arrowRight, True, False)

        if 0 < self.x + self.width < screen_width:
            self.x += self.vel
        if self.facing == 1:
            display.blit(arrowRight, (self.x, self.y))
        else:
            display.blit(arrowLeft, (self.x, self.y))
