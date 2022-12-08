import pygame 
class Ship(): 
    def __init__(self, screen,ai_settings): 
        """初始化飞船并设置其初始位置""" 
        self.screen = screen 
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(r'E:\VSproject\Note\alien_invasioin\images\ship.bmp')
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() 
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom 

        #移动标志
        self.moving_right = False
        self.moving_left = False

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

    def update(self): 
        """根据移动标志调整飞船的位置""" 
        # 更新飞船的center值，而不是rect
        if self.moving_right: 
            self.rect.centerx += self.ai_settings.ship_speed_factor    

        if self.moving_left: 
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self): 
        """在指定位置绘制飞船""" 
        self.screen.blit(self.image, self.rect)

