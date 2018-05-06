class Settings():
    '''存储《外星人入侵》的所有设置类'''
    def __init__(self):
        """初始化的游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (240,255,255)
        self.ship_speed_factor = 1.5