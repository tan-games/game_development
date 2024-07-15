import pygame

import general

while general.running:
    general.event_checker()
    general.uad()

    general.Time.clock.tick(60)
