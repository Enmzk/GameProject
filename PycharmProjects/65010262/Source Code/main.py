import os.path
import pygame
import random
from Player import player
from Archer import archer
from Archer import archer_arrow
from Explosion import explosion

pygame.init()

screen_width = 1560
screen_height = 798
FPS = 64
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("King Geshi")
pixel_font = pygame.font.Font(r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Font\BitPotionExt.ttf', 48)
score_font = pygame.font.Font(r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Font\BitPotionExt.ttf', 96)
mainMenu_font = pygame.font.Font(r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Font\BitPotionExt.ttf', 128)
user_text = '65010262 NAPHAT PHATINAWIN'

bg = pygame.image.load(
    r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Background\PNG\Battleground3\Pale\Battleground3.png")

clock = pygame.time.Clock()

# -------------------------------------Name------------------#
player_name = ''
text_box = pygame.Rect(650, 150, 100, 100)
game_over = False
active = False


class enemy(pygame.sprite.Sprite):
    scale_width = 600
    scale_height = 600
    walkLeft = [pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\walkL1.png"),
                pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\walkL2.png"),
                pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\walkL3.png"),
                pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\walkL4.png")]
    walkRight = [pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\walkR1.png"),
                 pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\walkR2.png"),
                 pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\walkR3.png"),
                 pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\walkR4.png")]
    attack1 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\enemy_attack1.png"),
        (scale_width, scale_height))
    attack2 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\enemy_attack2.png"),
        (scale_width, scale_height))
    attack3 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\enemy_attack3.png"),
        (scale_width, scale_height))
    attack4 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\enemy_attack4.png"),
        (scale_width, scale_height))
    attack5 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\enemy_attack5.png"),
        (scale_width, scale_height))
    attack6 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\enemy_attack6.png"),
        (scale_width, scale_height))
    attack7 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\enemy_attack7.png"),
        (scale_width, scale_height))
    attack8 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Skeleton\enemy_attack8.png"),
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
        self.width = 260
        self.height = 260
        self.vel = -3
        self.vel_toLeft = -3
        self.vel_toRight = 3
        self.atk = 3
        self.atkspd = 2
        self.attack = False
        self.attackCount = 0
        self.attackCooldown = 2000
        self.hp = 40
        self.hp_max = self.hp
        self.walkCount = 0
        self.deathCount = 0
        self.distancing = 0
        self.player_is_on_right = False
        self.hitbox = (self.x + 30, self.y + 20, 230, 230)
        self.greenBar = 0
        self.redBar = 0

    def draw(self, display):
        self.move()
        if self.walkCount + 1 >= FPS:
            self.walkCount = 0
        if not self.attack:
            if self.vel > 0:
                display.blit(self.walkRight[self.walkCount // 16], (self.x, self.y))
                self.walkCount += 2
            elif self.vel < 0:
                display.blit(self.walkLeft[self.walkCount // 16], (self.x, self.y))
                self.walkCount += 2
        if self.player_is_on_right:
            self.vel = self.vel_toRight
        else:
            self.vel = self.vel_toLeft
        self.hitbox = (self.x + 30, self.y + 20, 230, 230)
        self.greenBar = (self.hp / self.hp_max) * (100)
        self.redBar = (self.hp_max / self.hp_max) * (100)
        pygame.draw.rect(display, (255, 0, 0),
                         (self.hitbox[0] + 20, self.hitbox[1] - 20, self.redBar, 10))  # RedHealthBar
        pygame.draw.rect(display, (0, 255, 0),
                         (self.hitbox[0] + 20, self.hitbox[1] - 20, self.greenBar, 10))  # GreenHealthBar

    def move(self):
        if self.hp > 0:
            if self.vel > 0:
                if self.x + self.width < man.hitbox[0] + 50 - self.distancing:
                    self.x += self.vel
                else:
                    self.walkCount = 0
            else:
                if self.x - self.vel > man.hitbox[0] + man.hitbox[2] - 50 + self.distancing:
                    self.x += self.vel
                else:
                    self.walkCount = 0
            if self.attackCount + 1 > FPS:
                self.attackCount = 0
            elif self.attack:
                if self.player_is_on_right:
                    display.blit(self.attackRight[self.attackCount // 8], (self.x - 110, self.y - 170))
                    self.attackCount += self.atkspd
                else:
                    display.blit(self.attackLeft[self.attackCount // 8], (self.x - 110, self.y - 170))
                    self.attackCount += self.atkspd
            else:
                self.attackCount = 0


class flying(pygame.sprite.Sprite):
    scale_width = 540
    scale_height = 540

    fly1 = pygame.transform.scale(
        pygame.image.load(r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\flight1.png'),
        (scale_width, scale_height))
    fly2 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\flight2.png"),
        (scale_width, scale_height))
    fly3 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\flight3.png"),
        (scale_width, scale_height))
    fly4 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\flight4.png"),
        (scale_width, scale_height))
    fly5 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\flight5.png"),
        (scale_width, scale_height))
    fly6 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\flight6.png"),
        (scale_width, scale_height))
    fly7 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\flight7.png"),
        (scale_width, scale_height))
    fly8 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\flight8.png"),
        (scale_width, scale_height))

    flyRight = [fly1, fly2, fly3, fly4, fly5, fly6, fly7, fly8]
    flyLeft = [pygame.transform.flip(fly1, True, False),
               pygame.transform.flip(fly2, True, False),
               pygame.transform.flip(fly3, True, False),
               pygame.transform.flip(fly4, True, False),
               pygame.transform.flip(fly5, True, False),
               pygame.transform.flip(fly6, True, False),
               pygame.transform.flip(fly7, True, False),
               pygame.transform.flip(fly8, True, False),
               ]
    attack1 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\attack1.png"),
        (scale_width, scale_height))
    attack2 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\attack2.png"),
        (scale_width, scale_height))
    attack3 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\attack3.png"),
        (scale_width, scale_height))
    attack4 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\attack4.png"),
        (scale_width, scale_height))
    attack5 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\attack5.png"),
        (scale_width, scale_height))
    attack6 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\attack6.png"),
        (scale_width, scale_height))
    attack7 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\attack7.png"),
        (scale_width, scale_height))
    attack8 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Flying eye\attack8.png"),
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
        self.y = 175
        self.width = 260
        self.height = 260
        self.vel = -10
        self.vel_toLeft = -10
        self.vel_toRight = 10
        self.atk = 1
        self.atkspd = 2
        self.attack = False
        self.attackCount = 0
        self.hp = 20
        self.hp_max = self.hp
        self.flyCount = 0
        self.deathCount = 0
        self.distancing = 0
        self.player_is_on_right = False
        self.hitbox = (self.x + 200, self.y + 210, 130, 130)
        self.greenBar = 0
        self.redBar = 0

    def draw(self, display):
        self.move()
        if self.flyCount + 1 >= FPS:
            self.flyCount = 0
        if not self.attack:
            if self.vel > 0:
                display.blit(self.flyRight[self.flyCount // 8], (self.x, self.y))
                self.flyCount += 2
            elif self.vel < 0:
                display.blit(self.flyLeft[self.flyCount // 8], (self.x, self.y))
                self.flyCount += 2
        if self.player_is_on_right:
            self.vel = self.vel_toRight
        else:
            self.vel = self.vel_toLeft
        self.hitbox = (self.x + 200, self.y + 210, 130, 130)
        self.greenBar = (self.hp / self.hp_max) * (50)
        self.redBar = (self.hp_max / self.hp_max) * (50)
        pygame.draw.rect(display, (255, 0, 0),
                         (self.hitbox[0] + 20, self.hitbox[1] - 20, self.redBar, 10))  # RedHealthBar
        pygame.draw.rect(display, (0, 255, 0),
                         (self.hitbox[0] + 20, self.hitbox[1] - 20, self.greenBar, 10))  # GreenHealthBar

    def move(self):
        if self.hp > 0:
            if self.vel > 0:
                if self.x + self.width < man.x - self.distancing:
                    self.x += self.vel
                else:
                    self.flyCount = 0
            else:
                if self.x - self.vel > man.x - 20 + self.distancing:
                    self.x += self.vel
                else:
                    self.flyCount = 0
            if self.attackCount + 1 > FPS:
                self.attackCount = 0
            elif self.attack:
                if self.player_is_on_right:
                    display.blit(self.attackRight[self.attackCount // 8], (self.x, self.y))
                    self.attackCount += self.atkspd
                else:
                    display.blit(self.attackLeft[self.attackCount // 8], (self.x, self.y))
                    self.attackCount += self.atkspd
            else:
                self.attackCount = 0


class firewizard(pygame.sprite.Sprite):
    scale_width = 800
    scale_height = 800
    move1 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Move1.png"),
        (scale_width, scale_height))
    move2 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Move2.png"),
        (scale_width, scale_height))
    move3 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Move3.png"),
        (scale_width, scale_height))
    move4 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Move4.png"),
        (scale_width, scale_height))
    move5 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Move5.png"),
        (scale_width, scale_height))
    move6 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Move6.png"),
        (scale_width, scale_height))
    move7 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Move7.png"),
        (scale_width, scale_height))
    move8 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Move8.png"),
        (scale_width, scale_height))

    moveRight = [move1, move2, move3, move4, move5, move6, move7, move8]
    moveLeft = [pygame.transform.flip(move1, True, False),
                pygame.transform.flip(move2, True, False),
                pygame.transform.flip(move3, True, False),
                pygame.transform.flip(move4, True, False),
                pygame.transform.flip(move5, True, False),
                pygame.transform.flip(move6, True, False),
                pygame.transform.flip(move7, True, False),
                pygame.transform.flip(move8, True, False)
                ]

    attack1 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Attack1.png"),
        (scale_width, scale_height))
    attack2 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Attack2.png"),
        (scale_width, scale_height))
    attack3 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Attack3.png"),
        (scale_width, scale_height))
    attack4 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Attack4.png"),
        (scale_width, scale_height))
    attack5 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Attack5.png"),
        (scale_width, scale_height))
    attack6 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Attack6.png"),
        (scale_width, scale_height))
    attack7 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Attack7.png"),
        (scale_width, scale_height))
    attack8 = pygame.transform.scale(
        pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Evil Wizard\Attack8.png"),
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
        self.x = 1250
        self.y = 450
        self.width = 120
        self.height = 220
        self.vel = -6
        self.vel_toLeft = -6
        self.vel_toRight = 6
        self.atk = 2
        self.atkspd = 4
        self.attack = False
        self.attackCount = 0
        self.attackCooldown = 2000
        self.hp = 100
        self.hp_max = self.hp
        self.moveCount = 0
        self.waitCount = 0
        self.player_is_on_right = False
        self.hitbox = (self.x + 320, self.y - 10, 120, 220)
        self.greenBar = 0
        self.redBar = 0

    def draw(self, display):
        self.move()
        if self.moveCount + 1 >= FPS:
            self.moveCount = 0
        if not self.attack:
            if self.vel > 0:
                display.blit(self.moveRight[self.moveCount // 8], (self.x, self.y - 320))
                self.moveCount += 2
            elif self.vel < 0:
                display.blit(self.moveLeft[self.moveCount // 8], (self.x, self.y - 320))
                self.moveCount += 2
        if self.player_is_on_right:
            self.vel = self.vel_toRight
        else:
            self.vel = self.vel_toLeft
        self.hitbox = (self.x + 320, self.y - 10, 120, 220)
        self.greenBar = (self.hp / self.hp_max) * (150)
        self.redBar = (self.hp_max / self.hp_max) * (150)
        pygame.draw.rect(display, (255, 0, 0),
                         (self.hitbox[0] + 20, self.hitbox[1] - 20, self.redBar, 10))  # RedHealthBar
        pygame.draw.rect(display, (0, 255, 0),
                         (self.hitbox[0] + 20, self.hitbox[1] - 20, self.greenBar, 10))  # GreenHealthBar

    def move(self):
        if self.hp > 0:
            if self.vel > 0:
                if self.hitbox[0] + self.hitbox[2] < man.hitbox[0] + 20:
                    self.x += self.vel
                else:
                    self.moveCount = 0
            else:
                if self.hitbox[0] - self.vel > man.hitbox[0] + 100:
                    self.x += self.vel
                else:
                    self.moveCount = 0
            if self.y > man.y and not man.isJump:
                self.y -= self.vel_toRight / 12
            elif self.y < man.y and not man.isJump:
                self.y += self.vel_toRight / 12
            if self.attackCount + 1 > FPS:
                self.attackCount = 0
            elif self.attack:
                if self.player_is_on_right:
                    display.blit(self.attackRight[self.attackCount // 8], (self.x, self.y - 320))
                    self.attackCount += self.atkspd
                else:
                    display.blit(self.attackLeft[self.attackCount // 8], (self.x, self.y - 320))
                    self.attackCount += self.atkspd
            else:
                self.attackCount = 0


class GreenFire(pygame.sprite.Sprite):
    scale_width = 150
    scale_height = 200
    start1 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\start\burning_start_1_1.png'),
        (scale_width, scale_height))
    start2 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\start\burning_start_1_2.png'),
        (scale_width, scale_height))
    start3 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\start\burning_start_1_3.png'),
        (scale_width, scale_height))
    start4 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\start\burning_start_1_4.png'),
        (scale_width, scale_height))
    green_start = [start1, start2, start3, start4]

    loop1 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\loops\burning_loop_1_1.png'),
        (scale_width, scale_height))
    loop2 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\loops\burning_loop_1_2.png'),
        (scale_width, scale_height))
    loop3 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\loops\burning_loop_1_3.png'),
        (scale_width, scale_height))
    loop4 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\loops\burning_loop_1_4.png'),
        (scale_width, scale_height))
    loop5 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\loops\burning_loop_1_5.png'),
        (scale_width, scale_height))
    loop6 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\loops\burning_loop_1_6.png'),
        (scale_width, scale_height))
    loop7 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\loops\burning_loop_1_7.png'),
        (scale_width, scale_height))
    loop8 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\loops\burning_loop_1_8.png'),
        (scale_width, scale_height))
    green_loops = [loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 1000
        self.y = 100
        self.ignite = False
        self.loopCount = 0
        self.hitbox = (self.x + 40, self.y + 100, 80, 100)

    def draw(self, display):
        if self.loopCount + 1 > FPS:
            self.loopCount = 0
        else:
            display.blit(self.green_loops[self.loopCount // 8], (self.x, self.y))
            self.loopCount += 4
        self.hitbox = (self.x + 40, self.y + 100, 80, 100)

class OrangeFire(pygame.sprite.Sprite):
    scale_width = 150
    scale_height = 200

    loop1 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\orange\loops\burning_loop_1_1.png'),
        (scale_width, scale_height))
    loop2 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\orange\loops\burning_loop_1_2.png'),
        (scale_width, scale_height))
    loop3 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\orange\loops\burning_loop_1_3.png'),
        (scale_width, scale_height))
    loop4 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\orange\loops\burning_loop_1_4.png'),
        (scale_width, scale_height))
    loop5 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\orange\loops\burning_loop_1_5.png'),
        (scale_width, scale_height))
    loop6 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\orange\loops\burning_loop_1_6.png'),
        (scale_width, scale_height))
    loop7 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\orange\loops\burning_loop_1_7.png'),
        (scale_width, scale_height))
    loop8 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\orange\loops\burning_loop_1_8.png'),
        (scale_width, scale_height))
    orange_loops = [loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 1000
        self.y = 100
        self.ignite = False
        self.loopCount = 0
        self.hitbox = (self.x + 40, self.y + 100, 80, 100)

    def draw(self, display):
        if self.loopCount + 1 > FPS:
            self.loopCount = 0
        else:
            display.blit(self.orange_loops[self.loopCount // 8], (self.x, self.y))
            self.loopCount += 4
        self.hitbox = (self.x + 40, self.y + 100, 80, 100)

class BlueFire(pygame.sprite.Sprite):
    scale_width = 150
    scale_height = 200

    loop1 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\blue\loops\burning_loop_1_1.png'),
        (scale_width, scale_height))
    loop2 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\blue\loops\burning_loop_1_2.png'),
        (scale_width, scale_height))
    loop3 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\blue\loops\burning_loop_1_3.png'),
        (scale_width, scale_height))
    loop4 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\blue\loops\burning_loop_1_4.png'),
        (scale_width, scale_height))
    loop5 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\blue\loops\burning_loop_1_5.png'),
        (scale_width, scale_height))
    loop6 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\blue\loops\burning_loop_1_6.png'),
        (scale_width, scale_height))
    loop7 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\blue\loops\burning_loop_1_7.png'),
        (scale_width, scale_height))
    loop8 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\blue\loops\burning_loop_1_8.png'),
        (scale_width, scale_height))
    blue_loops = [loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 1000
        self.y = 100
        self.ignite = False
        self.loopCount = 0
        self.hitbox = (self.x + 40, self.y + 100, 80, 100)

    def draw(self, display):
        if self.loopCount + 1 > FPS:
            self.loopCount = 0
        else:
            display.blit(self.blue_loops[self.loopCount // 8], (self.x, self.y))
            self.loopCount += 4
        self.hitbox = (self.x + 40, self.y + 100, 80, 100)

class green_aura(pygame.sprite.Sprite):
    scale_width = 200
    scale_height = 320

    greenloop1 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\loops\burning_loop_3_1.png'),
        (scale_width, scale_height))
    greenloop2 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\loops\burning_loop_3_2.png'),
        (scale_width, scale_height))
    greenloop3 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\loops\burning_loop_3_3.png'),
        (scale_width, scale_height))
    greenloop4 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\green\loops\burning_loop_3_4.png'),
        (scale_width, scale_height))
    green_loops = [greenloop1, greenloop2, greenloop3, greenloop4]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.greenCount = 0
        self.ignite = False

    def draw(self, display):
        if self.greenCount + 1 > FPS:
            self.greenCount = 0
        else:
            display.blit(self.green_loops[self.greenCount // 16], (man.x + 20, man.y - 100))
            self.greenCount += 8


class blue_aura(pygame.sprite.Sprite):
    scale_width = 200
    scale_height = 320

    blueloop1 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\blue\loops\burning_loop_3_1.png'),
        (scale_width, scale_height))
    blueloop2 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\blue\loops\burning_loop_3_2.png'),
        (scale_width, scale_height))
    blueloop3 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\blue\loops\burning_loop_3_3.png'),
        (scale_width, scale_height))
    blueloop4 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\blue\loops\burning_loop_3_4.png'),
        (scale_width, scale_height))
    blue_loops = [blueloop1, blueloop2, blueloop3, blueloop4]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.blueCount = 0
        self.ignite = False

    def draw(self, display):
        if self.blueCount + 1 > FPS:
            self.blueCount = 0
        else:
            display.blit(self.blue_loops[self.blueCount // 16], (man.x + 20, man.y - 100))
            self.blueCount += 8


class orange_aura(pygame.sprite.Sprite):
    scale_width = 200
    scale_height = 320

    orangeloop1 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\orange\loops\burning_loop_3_1.png'),
        (scale_width, scale_height))
    orangeloop2 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\orange\loops\burning_loop_3_2.png'),
        (scale_width, scale_height))
    orangeloop3 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\orange\loops\burning_loop_3_3.png'),
        (scale_width, scale_height))
    orangeloop4 = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Enemy\Fire_buff\png\orange\loops\burning_loop_3_4.png'),
        (scale_width, scale_height))
    orange_loops = [orangeloop1, orangeloop2, orangeloop3, orangeloop4]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.orangeCount = 0
        self.ignite = False

    def draw(self, display):
        if self.orangeCount + 1 > FPS:
            self.orangeCount = 0
        else:
            display.blit(self.orange_loops[self.orangeCount // 16], (man.x + 20, man.y - 100))
            self.orangeCount += 8

def create_font(s, color):
    return pixel_font.render(s, True, color)

def create_score(s, color):
    return score_font.render(s, True, color)

def create_menu(s, color):
    return mainMenu_font.render(s, True, color)

# ---------------------------------Update--------------------------------------------------------#
def redrawGameWindow():
    display.blit(bg, (0, 0))
    display.blit(create_font(user_text, (255, 255, 255)), (1160, 20))
    display.blit(create_font("Red Soul   :", redColor), (50, 100))
    display.blit(create_font(str(soul[0]), redColor), (250, 100))
    display.blit(create_font("/", redColor), (275, 100))
    display.blit(create_font(str(upgradeRed), redColor), (300, 100))
    display.blit(create_font("Blue Soul  :", blueColor), (50, 160))
    display.blit(create_font(str(soul[1]), blueColor), (250, 160))
    display.blit(create_font("/", blueColor), (275, 160))
    display.blit(create_font(str(upgradeBlue), blueColor), (300, 160))
    display.blit(create_font("Green Soul :", greenColor), (50, 220))
    display.blit(create_font(str(soul[2]), greenColor), (250, 220))
    display.blit(create_font("/", greenColor), (275, 220))
    display.blit(create_font(str(upgradeGreen), greenColor), (300, 220))
    display.blit(create_score(show_score.rjust(6, '0'), (255, 255, 255)), (1360, 50))
    for a in aura:
        if a.ignite:
            a.draw(display)
    man.draw(display)
    for f in fire:
        if f.ignite:
            f.draw(display)
    for skeleton in skeletons:
        skeleton.draw(display)
    for arch in archers:
        arch.draw(display)
    for arrow in arrows:
        arrow.draw(display)
    for fly in flies:
        fly.draw(display)
    for b in bosses:
        b.draw(display)
    show_explosion.draw(display)

def pause():
    game_paused = True
    show_score = str(score)
    bg = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Background\PNG\Battleground3\Pale\trees&bushes.png'),
                                (screen_width, screen_height))
    sky = pygame.transform.scale(
        pygame.image.load(r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Background\PNG\Battleground3\Pale\sky.png'),
        (screen_width, screen_height))
    while game_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_h:
                    game_paused = False
                    highscore()
        display.blit(sky, (0, 0))
        display.blit(bg, (0, 0))
        display.blit(create_menu("PAUSED", greenColor), (680, 100))
        display.blit(create_menu("Press SPACE to continue", greenColor), (350, 300))
        display.blit(create_menu("Press H to view highscore", greenColor), (350, 450))
        display.blit(create_menu("Press ESC to quit a game", greenColor), (350, 600))
        pygame.display.update()


def gameover():
    global show_score
    score_sixdigit = 0
    active = False
    player_name = ''
    game_over = True
    sky = pygame.transform.scale(
        pygame.image.load(r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Background\PNG\Battleground3\Pale\sky.png'),
        (screen_width, screen_height))
    star = pygame.transform.scale(pygame.image.load(
        r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Background\PNG\Battleground3\Pale\fireflys.png'),
                                  (screen_width, screen_height))
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    game_over = False
                elif event.key == pygame.K_RETURN:
                    file_write = open("score.txt", 'a')
                    file_write.write(show_score + ',' + player_name + '\n')
                    file_write.close()
                    scoreList = list()
                    filename = 'score.txt'
                    with open(filename) as fin:
                        for line in fin:
                            scoreList.append(line)
                            if int(show_score) < 1000000:
                                show_score = show_score.zfill(6)
                    scoreList.sort(reverse=True)
                    filename = 'score_sorted.txt'
                    with open(filename, 'w') as fout:
                        for s in scoreList:
                            fout.write(s)
                    game_over = False
                    highscore()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode
        if active:
            color = redColor
        else:
            color = greenColor
        display.blit(sky, (0, 0))
        display.blit(star, (0, 0))
        display.blit(create_menu("YOU DIED!", redColor), (680, 50))
        display.blit(create_menu("Name:", redColor), (350, 150))
        display.blit(create_menu("Score:", redColor), (350, 300))
        display.blit(create_menu(show_score, greenColor), (650, 300))
        display.blit(create_score("Press ENTER to submit your score", redColor), (350, 450))
        display.blit(create_score("Press ESC to quit a game", redColor), (350, 600))
        pygame.draw.rect(display, color, text_box, 4)
        surf = mainMenu_font.render(player_name, True, 'orange')
        display.blit(surf, (text_box.x + 5, text_box.y + 5))
        text_box.w = max(100, surf.get_width() + 10)
        pygame.display.update()


def highscore():
    list1 = []
    list2 = []
    dataCount = 0
    floor = pygame.transform.scale(
        pygame.image.load(r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Background\PNG\Battleground2\Pale\floor.png'),
        (screen_width, screen_height))
    bg = pygame.transform.scale(
        pygame.image.load(
            r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Background\PNG\Battleground2\Pale\bg.png'),
        (screen_width, screen_height))
    dragon = pygame.transform.scale(
        pygame.image.load(
            r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Background\PNG\Battleground2\Pale\dragon.png'),
        (screen_width, screen_height))
    scoreboard = True
    file = open('score_sorted.txt', 'r')
    file_zero = open('score.txt', 'r')
    lines = file.readlines()
    lines_zero = file_zero.readlines()
    while scoreboard:
        dataCount = 0
        display.blit(bg, (0, 0))
        display.blit(floor, (0, 0))
        display.blit(dragon, (0, 0))
        if man.hp > 0:
            display.blit(create_score("Press B to back to pause menu", (0, 0, 0)), (400, 600))
        display.blit(create_score("Press ESC to quit a game", (0, 0, 0)), (450, 680))
        if os.path.getsize('score_sorted.txt'):
            for x in lines:
                data = x.split(',')
                list1.append(data[0])
                list2.append(data[1])
                dataCount += 1
        else:
            for x in lines_zero:
                data = x.split(',')
                list1.append(data[0].zfill(6))
                list2.append(data[1])
                dataCount += 1
        if dataCount < 5:
            for i in range(dataCount):
                display.blit(create_score(list2[i].strip(), (255, 255, 255)), (450, (i + 1) * 100))
                display.blit(create_score(list1[i], (255, 255, 255)), (1000, (i + 1) * 100))
        else:
            for j in range(0, 5):
                display.blit(create_score(list2[j].strip(), (255, 255, 255)), (450, (j + 1) * 100))
                display.blit(create_score(list1[j], (255, 255, 255)), (1000, (j + 1) * 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    scoreboard = False
                if event.key == pygame.K_b:
                    scoreboard = False
                    pause()
        pygame.display.update()


# --------------------------------Skeleton setup--------------------------------------------------------#
man = player(100, 450, 100, 220)
score = 0
enemy_deathCount = 0
show_explosion = explosion()
skeletons = pygame.sprite.Group()
skeleton = enemy()
skeleton_max = 1
skeleton_count = 0
skeleton_timespawn = 5000
enemies_list = []
skeleton_upgrade = 30000
upgrade = 1
timespawn = 1

# -----------------------------------------------------Boss setup--------------------------#
bosses = pygame.sprite.Group()
boss = firewizard()
boss_count = 0
boss_spawn = 45000
boss_init = 90000
# ------------------------------------Archer setup--------------------------------------------#
archers = pygame.sprite.Group()
arch = archer()
archer_timespawn = 15000
archer_upgrade = 30000
archer_upgrade_count = 1
archer_count = 0
archer_init = 30000
arrows = pygame.sprite.Group()

# --------------------------------------------Flying setup---------------#
flies = pygame.sprite.Group()
fly = flying()
fly_max = 1
fly_count = 0
fly_timespawn = 5000
fly_init = 30000
fly_upgrade = 30000
flies_list = []
fly_upgrade_count = 1

darktree_color = (60, 60, 53)
darktree_x = 860
darktree_y = 480
brighttree_color = (77, 82, 70)
tree_x = 870
tree_y = 200
tree_width = 170
platform_height = 300

# ---------------------------------------------------Fire setup------------------------#
fire_cooldown = 10000
fire_count = 1
greenfire = GreenFire()
orangefire = OrangeFire()
bluefire = BlueFire()
greenAura = green_aura()
blueAura = blue_aura()
orangeAura = orange_aura()
aura = [greenAura, blueAura, orangeAura]
fire = [orangefire, bluefire, greenfire]
soulOrange = 0
soulBlue = 0
soulGreen = 0
soul = [soulOrange, soulBlue, soulGreen]
last_flame_num = -1
stopcheck = False
upgradeRed = 3
upgradeBlue = 3
upgradeGreen = 3
redColor = (232, 92, 68)
blueColor = (72, 220, 248)
greenColor = (68, 228, 100)
ult1 = 0
ult2 = 0
ult3 = 0
ultColorChange = [ult1, ult2, ult3]
ultColor = (0, 0, 0)
show_status = 3000
timestampRed = 0
timestampBlue = 0
timestampGreen = 0
upgradeRed_count = 0
upgradeBlue_count = 0
upgradeGreen_count = 0
enemiesCollision_list = []
# --------------------------UI-------------------------#
game_paused = False
run = True

while run:
    show_score = str(score)

    ultChange = list(ultColorChange)
    for c in range(len(ultChange)):
        if ultChange[c] == 255:
            ultChange[c] = 0
        else:
            ultChange[c] += 1
    ultColorChange = tuple(ultChange)

    clock.tick(FPS)
    game_clock = pygame.time.get_ticks()

    # --------------------------------------------Skeleton Upgrade-----#
    if game_clock > skeleton_upgrade * upgrade:
        upgrade += 1

    # -----------------------------------------------Skeleton Spawner--#
    if game_clock > skeleton_timespawn * timespawn:
        skt = enemy()
        if orangefire.ignite:
            skt.atk *= 2
        elif bluefire.ignite:
            skt.atkspd *= 2
        elif greenfire.ignite:
            skt.hp *= 2
            skt.hp_max *= 2
        skt.hp += ((upgrade - 1) * 5)
        skeletons.add(skt)
        enemies_list.append(skt)
        skeleton_count += 1
        timespawn += 1

    # ----------------------------------------------Boss Spawner-----------------#
    if game_clock > (boss_spawn * boss_count) + boss_init:
        b = firewizard()
        bosses.add(b)
        enemies_list.append(b)
        boss_count += 1
    # ---------------------------------------------------------Archer upgrade-----------#
    if game_clock > archer_upgrade * archer_upgrade_count:
        skt.hp += (upgrade * 5)
        archer_upgrade_count += 1
    # ------------------------------------------------------------------Archer Spawner----#
    if game_clock > archer_init + (archer_timespawn * archer_count):
        arch = archer()
        if orangefire.ignite:
            arch.atk *= 2
        elif bluefire.ignite:
            arch.atkspd *= 2
        elif greenfire.ignite:
            arch.hp *= 2
            arch.hp_max *= 2
        arch.atk += ((archer_upgrade_count - 1) * 2)
        archers.add(arch)
        enemies_list.append(arch)
        archer_count += 1

        # -----------------------------------------------Flying Upgrade-------#
    if game_clock > fly_init + (fly_upgrade * fly_upgrade_count):
        fly_timespawn -= 50
        fly_upgrade_count += 1

    # -----------------------------------------------------------Flying Spawner------------#
    if game_clock > fly_init + (fly_timespawn * fly_count):
        fly = flying()
        if orangefire.ignite:
            fly.atk *= 2
        elif bluefire.ignite:
            fly.atkspd *= 2
        elif greenfire.ignite:
            fly.hp *= 2
            fly.hp_max *= 2
        fly.atk += (fly_upgrade_count - 1)
        flies.add(fly)
        enemies_list.append(fly)
        fly_count += 1

    # ---------------------------------------------------Fire spawner-----------------------#
    if game_clock > fire_cooldown * fire_count:
        flame_num = random.randrange(0, len(fire), 1)
        if last_flame_num != -1:
            fire[last_flame_num].ignite = False
        fire[flame_num].ignite = True
        flame_color = fire[flame_num]
        fire_count += 1
        last_flame_num = flame_num

    # --------------------------------------------------Event_Type--------------------------------------------#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            man.attack = True
            man.attackCount = 0
        if event.type == pygame.MOUSEBUTTONUP:
            if man.attackCount < FPS:
                man.attack = True
            else:
                man.attack = False
    pygame.event.clear()
    # -------------------------------------------------------------Movement--------------------------------------------#
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and man.x > man.edgeL:
        man.x -= man.vel
        man.right = False
        man.left = True
        man.face = 0
    elif keys[pygame.K_d] and man.x < man.edgeR - man.vel - (man.width / 2):
        man.x += man.vel
        man.right = True
        man.left = False
        man.face = 1
    else:
        man.right = False
        man.left = False
        man.runCount = 0
    if keys[pygame.K_ESCAPE]:
        pause()
    if keys[pygame.K_h] and game_paused:
        highscore()
    # --------------------------------------------Check soul for unlock skill-------------------#
    if soul[0] == upgradeRed:
        upgradeRed_count += 1
        timestampRed = game_clock
        if upgradeRed == 5:
            man.atk += 3
        upgradeRed = 5
        soul[0] = 0
        score += 100
        man.pressQ = True
        man.unlockQ = True
    if soul[1] == upgradeBlue:
        upgradeBlue_count += 1
        timestampBlue = game_clock
        if upgradeBlue == 5:
            man.hp_max += 3
        upgradeBlue = 5
        soul[1] = 0
        score += 100
        man.pressE = True
        man.unlockE = True
    if soul[2] == upgradeGreen:
        upgradeGreen_count += 1
        timestampGreen = game_clock
        if upgradeGreen == 5:
            man.hp_max += 3
        upgradeGreen = 5
        soul[2] = 0
        score += 100
        man.pressR = True
        man.unlockR = True
    if man.unlockQ and man.unlockE and man.unlockR and not stopcheck:
        man.unlockF = True
        man.pressF = True
        man.timeUnlock_F = game_clock
        score += 500
        stopcheck = True
    # ---------------------------------------------------------------------------------------Keys check----------------#
    if man.pressQ and keys[pygame.K_q] and not blueAura.ignite and not greenAura.ignite:
        man.skill_Q = True
        orangeAura.ignite = True
        man.timePress_Q = game_clock
    elif man.pressE and keys[pygame.K_e] and not orangeAura.ignite and not greenAura.ignite:
        man.skill_E = True
        blueAura.ignite = True
        man.timePress_E = game_clock
    elif man.pressR and keys[pygame.K_r] and not blueAura.ignite and not orangeAura.ignite:
        man.hp = man.hp_max
        greenAura.ignite = True
        man.timePress_R = game_clock
        man.pressR = False
    elif man.pressF and keys[pygame.K_f]:
        show_explosion = explosion()
        show_explosion.show = True
        man.timePress_F = game_clock
        for e in enemies_list:
            e.kill()
            score += len(enemies_list) * 50
        man.pressF = False
    # -----------------------------------------------------------------------------------Cooldown---------------#
    if man.unlockQ:
        if game_clock > man.timePress_Q + man.timerange_Q and orangeAura.ignite:
            orangeAura.ignite = False
            man.pressQ = False
            man.skill_Q = False
            man.time_Q = game_clock
        if game_clock > man.time_Q + man.cooldown_Q:
            man.pressQ = True
    if man.unlockE:
        if game_clock > man.timePress_E + man.timerange_E and blueAura.ignite:
            blueAura.ignite = False
            man.pressE = False
            man.time_E = game_clock
        if game_clock > man.time_E + man.cooldown_E:
            man.pressE = True
    if man.unlockR:
        if game_clock > man.timePress_R + man.timerange_R and greenAura.ignite:
            greenAura.ignite = False
            man.pressR = False
            man.time_R = game_clock
        if game_clock > man.time_R + man.cooldown_R:
            man.pressR = True
    if man.unlockF:
        if game_clock > man.timePress_F + man.timerange_E:
            man.pressF = False
        if game_clock > man.timePress_F + man.cooldown_F:
            man.pressF = True

    # -------------------------------------------------------------------------------Climbing------------------#
    if keys[pygame.K_w] and man.y > tree_y and tree_x < man.x + (man.width / 3) < tree_x + tree_width:
        man.y -= man.vel / 3
    elif keys[pygame.K_s] and man.y < 450 and tree_x < man.x + (man.width / 3) < tree_x + tree_width:
        man.y += man.vel / 3

    if man.y < 450 and man.isJump == False:
        man.climb = True
    else:
        man.climb = False

    if man.climb == True:
        man.edgeL = tree_x - 40
        man.edgeR = tree_x + tree_width
    else:
        man.edgeL = -40
        man.edgeR = screen_width

    if not (man.isJump):
        if keys[pygame.K_SPACE] and not man.climb:
            man.isJump = True
            man.right = False
            man.left = False
            man.runCount = 0
    else:
        if man.jumpCount >= -12:
            negative = 1
            if man.jumpCount < 0:
                negative = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * negative
            man.jumpCount -= 1.5
        else:
            man.isJump = False
            man.jumpCount = 12

    # ------------------------------------------------------Collision--------------------------------------------#
    i = 0
    # -----------------------------------------------Skeleton collision check--------------------------------------#
    for skeleton in skeletons:
        if (man.hitbox[0] + man.hitbox[2] > skeleton.hitbox[0] and man.hitbox[0] + man.hitbox[2] < skeleton.hitbox[0] +
            skeleton.hitbox[2]) and man.hitbox[1] + man.hitbox[3] > skeleton.hitbox[1] and not man.climb or (
                skeleton.hitbox[0] + skeleton.hitbox[2] > man.hitbox[0] and skeleton.hitbox[0] + skeleton.hitbox[2] <
                man.hitbox[0] + man.hitbox[2]):
            if not man.climb:
                skeleton.attack = True
            else:
                skeleton.attack = False
            if skeleton.attackCount == 56 and not blueAura.ignite:
                man.hp -= skeleton.atk
            if man.climb:
                pass
            elif man.attackCount == 48 and not man.climb:
                if man.skill_Q:
                    skeleton.hp -= (man.atk * 2)
                else:
                    skeleton.hp -= man.atk
            if skeleton.hp <= 0:
                skeleton.kill()
                enemies_list.remove(skeleton)
                score += 25
                skeleton_count -= 1
                enemy_deathCount += 1
        else:
            skeleton.attack = False
        if len(skeletons) > 1:
            skeleton.distancing = 25 * (i - 1)
        if man.hitbox[0] > skeleton.hitbox[0] + (skeleton.hitbox[2] / 2):
            skeleton.player_is_on_right = True
        else:
            skeleton.player_is_on_right = False
        i += 1

    # -------------------------------------------------------------Boss collision check-------------------#
    for b in bosses:
        if man.hitbox[0] + man.hitbox[2] > b.hitbox[0] and man.hitbox[0] + man.hitbox[2] < b.hitbox[0] + \
                b.hitbox[2] or (man.hitbox[0] < b.hitbox[0] + b.hitbox[2] and man.hitbox[0] > \
                                b.hitbox[0]):
            b.attack = True
            if b.attackCount % 8 == 0 and not blueAura.ignite and man.hitbox[1] + man.hitbox[3] - 100 > b.hitbox[1] + (
                    b.hitbox[3] / 2):
                man.hp -= b.atk
            if man.attackCount == 48:
                if man.skill_Q:
                    b.hp -= (man.atk * 2)
                else:
                    b.hp -= man.atk
            if b.hp <= 0:
                b.kill()
                enemies_list.remove(b)
                score += 250
                enemy_deathCount += 1

        else:
            b.attack = False
        if man.hitbox[0] > b.hitbox[0] + (b.hitbox[2] / 2):
            b.player_is_on_right = True
        else:
            b.player_is_on_right = False
    # ---------------------------------------------------------Archer collision check----------------#
    for a in archers:
        if man.hitbox[0] + man.hitbox[2] > a.hitbox[0] and man.hitbox[0] + man.hitbox[2] < a.hitbox[0] + \
                a.hitbox[2] or man.hitbox[0] < a.hitbox[0] + a.hitbox[2] and man.hitbox[0] > \
                a.hitbox[0]:
            if man.attackCount == 48:
                if man.skill_Q:
                    a.hp -= (man.atk * 2)
                else:
                    a.hp -= man.atk
        if a.attackCount == 56:
            arrow = archer_arrow(a.x, a.y, a.facing)
            arrows.add(arrow)

        if a.hp <= 0:
            a.kill()
            enemies_list.remove(a)
            score += 25
            enemy_deathCount += 1
        if man.x > a.x + (a.width / 2):
            a.facing = 1
        else:
            a.facing = -1
        i += 1

    # ------------------------------Arrow collision check--------------#
    for arw in arrows:
        if man.hitbox[0] < arw.x < man.hitbox[0] + man.hitbox[2] and man.hitbox[1] < arw.y < man.hitbox[1] + man.hitbox[
            3]:
            if not blueAura.ignite:
                man.hp -= arch.atk
            arw.kill()

    # -------------------------------Fly collision check----------------#
    j = 0
    fly_hit = []
    for f in flies:
        if man.hitbox[0] + man.hitbox[2] > f.hitbox[0] and man.hitbox[0] + man.hitbox[2] < f.hitbox[0] + \
                f.hitbox[2] or man.hitbox[0] < f.hitbox[0] + f.hitbox[2] and man.hitbox[0] > \
                f.hitbox[0]:
            f.attack = True
            if f.attackCount == 56 and not blueAura.ignite:
                man.hp -= f.atk
            if man.attackCount == 48 and (man.isJump or man.climb):
                if man.skill_Q:
                    f.hp -= (man.atk * 2)
                else:
                    f.hp -= man.atk
        else:
            f.attack = False

        if f.hp <= 0:
            enemy_deathCount += 1
            f.kill()
            enemies_list.remove(f)
            score += 10

        if len(flies) > 1:
            f.distancing = 5 * (j - 1)
        if man.x > f.x + (f.width / 2):
            f.player_is_on_right = True
        else:
            f.player_is_on_right = False
        j += 1
    # ---------------------------------------------------------Flame collision check----------------#
    k = 0
    for f in fire:
        if f.ignite:
            if man.hitbox[0] + man.hitbox[2] > f.hitbox[0] and man.hitbox[0] + man.hitbox[2] < f.hitbox[0] + \
                    f.hitbox[2] or (man.hitbox[0] < f.hitbox[0] + f.hitbox[2] and man.hitbox[0] > \
                                    f.hitbox[0]) and man.climb:
                if man.attackCount == 48:
                    f.ignite = False
                    soul[k] += 1
                    score += 25
                    f.kill()
        k += 1
    if man.hp <= 0:
        man.x = 5000
        menu_state = 'gameover'
        if int(show_score) < 1000000:
            show_score = show_score.zfill(6)
        gameover()

    redrawGameWindow()
    # ----------------------------------------------------------------------------Soul upgrade status update---------#
    if game_clock < timestampRed + show_status and upgradeRed_count == 1:
        display.blit(create_font("Sword Dance unlock", redColor), (400, 100))
    elif game_clock < timestampRed + show_status and upgradeRed_count > 1:
        display.blit(create_font("ATK + 3", redColor), (500, 100))

    if game_clock < timestampBlue + show_status and upgradeBlue_count == 1:
        display.blit(create_font("Immunity unlock", blueColor), (400, 160))
    elif game_clock < timestampBlue + show_status and upgradeBlue_count > 1:
        display.blit(create_font("MAX HP + 3", blueColor), (500, 160))

    if game_clock < timestampGreen + show_status and upgradeGreen_count == 1:
        display.blit(create_font("Regeneration unlock", greenColor), (400, 220))
    elif game_clock < timestampGreen + show_status and upgradeGreen_count > 1:
        display.blit(create_font("MAX HP + 3", greenColor), (500, 220))

    if game_clock < man.timeUnlock_F + show_status and man.unlockF:
        display.blit(create_font("The Rumbling unlock", ultColorChange), (50, 280))

    if man.pressQ:
        display.blit(create_font("Q", redColor), (360, 100))
    if man.pressE:
        display.blit(create_font("E", blueColor), (360, 160))
    if man.pressR:
        display.blit(create_font("R", greenColor), (360, 220))
    if man.pressF:
        display.blit(create_font("F", ultColorChange), (360, 280))
    display.blit(create_font(str(man.hp), (0, 0, 0)), (60, 20))
    pygame.display.update()
pygame.quit()