# encoding = 'utf-8'
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init() # 初始化游戏并创建一个屏幕对象
    ai_settings = Settings()
    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)

    while True: # 开始游戏主循环

        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)



run_game()

print("aaa")
