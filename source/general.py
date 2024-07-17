import pygame

import entity
from font import text_1

pygame.init()

# 게임의 진행 유무를 판단하기 위해 사용되는 값
running = True


class Time:
    """
    시간과 관련된 모든 변수들을 넣어 놓은 클래스 위의 클래스를 통해 시간 관련 변수들을 다룬다.
    """
    clock = pygame.time.Clock()
    timer_1 = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_1, 1000)


def event_checker():
    """
    게임 내에서 get()을 통해 받아오는 모든 이벤트를 처리하는 함수
    모든 이벤트 체킹은 해당 함수를 통해서만 이루어 져야 함
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == Time.timer_1:
            pass


def uad():
    """
    update and display의 약자로, 모든 엔티티 들을 update 하고 화면에 display 하기 위한 함수
    모든 update와 display는 해당 함수를 통해서만 이루어 져야 함
    """
    entity.window.fill((255, 255, 255))

    entity.window.blit(text_1.text, text_1.rect)

    # player
    entity.window.blit(entity.player.image, entity.player.rect)
    entity.player.update()

    pygame.display.update()

