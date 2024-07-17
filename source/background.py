import pygame

pygame.init()


class Background:
    vel = 10

    def __init__(self, n: int):
        self.image = pygame.image.load(f"../resource/backgrounds/jungle/jungle_{n}.jpg")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= Background.vel

    @classmethod
    def adjust_vel(cls, vel):
        cls.vel = vel


class BackgroundSystem:
    def __init__(self):
        self.background_list: list[Background] = []

    def add_background(self, background: Background):
        if len(self.background_list) == 0:
            background.rect.left = 0
        else:
            background.rect.left = self.background_list[-1].rect.right

        self.background_list.append(background)

    def update(self):
        for background in self.background_list:
            background.update()
            if background.rect.right < 0:
                background.rect.left = self.background_list[-1].rect.right

                self.background_list.remove(background)
                self.background_list.append(background)

    def draw(self, window: pygame.Surface):
        for background in self.background_list:
            window.blit(background.image, background.rect)

    @staticmethod
    def adjust_vel(vel):
        Background.adjust_vel(vel)


background_system = BackgroundSystem()
for i in range(1, 13):
    background_system.add_background(Background(i))

