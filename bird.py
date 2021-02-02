import pygame


class Bird:

    def __init__(self, sets, screen):
        """初始化bird设置"""
        self.screen = screen
        self.sets = sets
#       加载鸟儿
        self.image = pygame.image.load('images/bird.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
#       放置鸟儿
        self.rect.left = self.screen_rect.left + 100
        self.rect.top = 0.5 * self.screen_rect.bottom
#        #在bird的属性y中存储小数值
        self.y = float(self.rect.y)
#        移动标识
        self.moving_down = False
        self.moving_up = False

    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.sets.bird_speed
        if self.moving_up and self.rect.y > 0:
            self.y -= self.sets.bird_speed
        self.rect.y = self.y

    def center(self):
        """居中"""
        self.y = 0.5 * self.screen_rect.bottom

    def blitme(self):
        """绘制鸟儿"""
        self.screen.blit(self.image, self.rect)
