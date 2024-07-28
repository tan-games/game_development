import pygame

import random

# window setting
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../resource/items/rock.png")
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images: dict[str, pygame.Surface] = {
            'normal': pygame.image.load("../resource/player.png"),
            'rotated': pygame.image.load("../resource/player_rotated.png")
        }
        self.image = self.images['normal']
        self.rect = self.image.get_rect()
        self.health = 3
        self.vel = 0
        self.rect.centerx = 600
        self.rect.bottom = WINDOW_HEIGHT

    def update(self):
        self.rect.y += self.vel
        if self.rect.bottom <= WINDOW_HEIGHT:
            self.vel += 2
        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.vel = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.image = self.images['rotated']
        else:
            self.image = self.images['normal']

        if keys[pygame.K_d] and (self.rect.bottom == WINDOW_HEIGHT):
            self.vel -= 35

class Icicle(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.size = random.choice([0, 1])
        if self.size == 0:
            self.image = self.image.load("../resource/items/icicle/200.png")
        if self.size == 1:
            self.image = self.image.load("../resource/items/icicle/400.png")
        self.rect = self.image.get_rect()

player = Player()

