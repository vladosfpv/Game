from Settings import *


class Player(pygame.sprite.Sprite):
    name = ""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scale(pygame.image.load("images/player.png"), (40, 20))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self, left, right, up, down):
        if left and self.rect.x > 0:
            self.rect.x -= 3
        if right and self.rect.x < WIDTH - 30:
            self.rect.x += 3
        if up and self.rect.y > 0:
            self.rect.y -= 3
        if down and self.rect.y < HEIGHT - 30:
            self.rect.y += 3

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
