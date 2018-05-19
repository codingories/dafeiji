# encoding = 'utf-8'
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()  # 初始化游戏并创建一个屏幕对象
    ai_settings = Settings()

    pygame.display.set_caption("Alien Invasion")


    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 创建一个用于存储游戏统计信息的实例

    # 创建Play 按钮
    play_button = Button(ai_settings, screen, "Play")


    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)



    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    #alien = Alien(ai_settings, screen)
    aliens = Group()
    gf.create_fleet(ai_settings, screen,ship,aliens)

    while True:  # 开始游戏主循环
        #ship.blitme()
        gf.check_events(ai_settings, screen, stats, sb, play_button , ship, aliens, bullets)
        if stats.game_active:
            # print(stats.game_active)
            ship.update()

            # 删除已消失的子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)




run_game()


