from Settings import *


class Rocket(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = scale(pygame.image.load("images/asteroid.png"), (30, 30))
        self.image.set_colorkey(WHITE)
        self.rect = pygame.Rect(x, y, 30, 30)
        self.rect.center = (x, y)
        self.xvel = 0
        self.yvel = 0

    def update(self, xp, yp):
        if self.rect.x > xp:
            self.rect.x += 8.7 * self.xvel
            self.xvel -= 0.01
        else:
            self.rect.x += 8.7 * self.xvel
            self.xvel += 0.01

        if self.rect.y > yp:
            self.rect.y += 8.7 * self.yvel
            self.yvel -= 0.01
        else:
            self.rect.y += 8.7 * self.yvel
            self.yvel += 0.01

        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.left > WIDTH:
            self.kill()
        elif self.rect.top > HEIGHT:
            self.kill()
        elif self.rect.right < 0:
            self.kill()
