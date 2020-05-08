import pygame
import sys

res = [int(sys.argv[1]), int(sys.argv[2])]
running = True

screen = pygame.display.set_mode(res)

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
