import pygame

pygame.init()


class Font:
    def __init__(self, size: int, text: str):
        """
        텍스트를 Sprite로 반환하는 클래스. self.image 대신 self.text를 사용함
        :param size: Sprite 크기
        :param text: Sprite의 텍스트
        """
        super().__init__()
        self.font: pygame.font.Font = pygame.font.Font(None, size)
        self.text: pygame.Surface = self.font.render(text, True, (0, 0, 0))
        self.rect: pygame.Rect = self.text.get_rect()

    def text_convert(self, text: str):
        """텍스트 변환 메서드"""
        self.text = self.font.render(text, True, (0, 0, 0))


text_1 = Font(50, 'Test Font')
