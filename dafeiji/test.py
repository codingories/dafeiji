import pygame
import sys
while True:
    pygame.display.set_mode((1000,1000))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event.key)