import pygame

scale_width = 450
scale_height = 450
runRight = [pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\Run1.png"),
            pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\Run2.png"),
            pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\Run3.png"),
            pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\Run4.png"),
            pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\Run5.png"),
            pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\Run6.png"),
            pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\Run7.png"),
            pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\Run8.png")]
runLeft = [pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\RunL1.png"),
           pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\RunL2.png"),
           pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\RunL3.png"),
           pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\RunL4.png"),
           pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\RunL5.png"),
           pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\RunL6.png"),
           pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\RunL7.png"),
           pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\RunL8.png")]
stand = [pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\stand0.png"),
         pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\stand1.png")]
sword = [pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\sword1.png"),
         pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\sword2.png"),
         pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\sword3.png"),
         pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\sword4.png")]
swordL = [pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\swordL1.png"),
         pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\swordL2.png"),
         pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\swordL3.png"),
         pygame.image.load(r"C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\swordL4.png")]

jump1 = pygame.image.load(r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\Jump1.png')
jump2 = pygame.image.load(r'C:\Users\Naphat\PycharmProjects\65010262\Source Code\Sprites\Player\Jump2.png')
jumpRight = [pygame.transform.scale(jump1, (scale_width, scale_height)),
             pygame.transform.scale(jump2, (scale_width, scale_height))]
jumpLeft = [pygame.transform.flip(jump1, True, False),
            pygame.transform.flip(jump2, True, False)]

screen_width = 1560
screen_height = 798
FPS = 64
display = pygame.display.set_mode((screen_width, screen_height))

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = 100
        self.hp_max = 100
        self.atk = 10
        self.vel = 14
        self.isJump = False
        self.jumpCount = 12
        self.climb = False
        self.left = False
        self.right = False
        self.edgeL = -40
        self.edgeR = screen_width
        self.face = 1
        self.runCount = 0
        self.attack = False
        self.attackCount = 0
        self.standing = True
        self.hitbox = (self.x + 80, self.y + 20, 100, 220)
        self.skill_Q = False        # --------AOE and ATK Speed Buff-------#
        self.skill_E = False        # --------Immune-----------------------#
        self.skill_R = False        # --------Recovery---------------------#
        self.ult_F = False          # --------The Rumbling-----------------#
        self.timePress_Q = 0
        self.timePress_E = 0
        self.timePress_R = 0
        self.timePress_F = 0
        self.time_Q = 0
        self.time_E = 0
        self.time_R = 0
        self.timeUnlock_F = 0
        self.timerange_Q = 5000
        self.timerange_E = 5000
        self.timerange_R = 2000
        self.cooldown_Q = 15000
        self.cooldown_E = 15000
        self.cooldown_R = 15000
        self.cooldown_F = 60000
        self.unlockQ = False
        self.unlockE = False
        self.unlockR = False
        self.unlockF = False
        self.pressQ = False
        self.pressE = False
        self.pressR = False
        self.pressF = False
        self.greenBar = 0
        self.redBar = 0

    def draw(self, win):
        if self.attack and self.attackCount < FPS:
            if self.face == 0:
                win.blit(swordL[self.attackCount // 16], (self.x - 50, self.y - 50))
            else:
                win.blit(sword[self.attackCount // 16], (self.x - 50, self.y - 50))
            self.attackCount += 3
        else:
            self.attack = False
            if self.runCount + 1 >= FPS:
                self.runCount = 0
            if self.left:
                win.blit(runLeft[self.runCount // 8], (self.x, self.y))
                self.runCount += 2
            elif self.right:
                win.blit(runRight[self.runCount // 8], (self.x, self.y))
                self.runCount += 2
            elif self.attackCount > FPS:
                win.blit(stand[self.face], (self.x, self.y))
                self.attackCount = 0
            else:
                win.blit(stand[self.face], (self.x, self.y))
        self.hitbox = (self.x + 80, self.y + 20, 100, 220)
        self.greenBar = (self.hp / self.hp_max) * (560)
        self.redBar = (self.hp_max / self.hp_max) * (560)
        pygame.draw.rect(display, (255, 0, 0),
                         (50, 20, self.redBar, 50))  # RedHealthBar
        pygame.draw.rect(display, (0, 255, 0),
                         (50, 20, self.greenBar, 50))  # GreenHealthBar



