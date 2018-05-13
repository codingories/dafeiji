class Settings():
    '''存储《外星人入侵》的所有设置类'''
    def __init__(self):
        """初始化的游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (240,255,255)
        self.ship_speed_factor = 15
        self.bullet_speed_factor = 15
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
        # alien set
        self.alien_speed_factor = 10 # alien move speed
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移动, 为-1表示向左移
        self.fleet_direction= 1 # 移动的方向

