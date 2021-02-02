import pygame
from pygame.sprite import Sprite


class Block(Sprite):

    def __init__(self, sets, screen):
        super(Block, self).__init__()
        self.screen = screen
        self.sets = sets

#        #加载block图像并设置rect属性
        self.image = pygame.image.load('images/blocks.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
#        #初始位置
        self.rect.x = 300
        self.rect.y = 0
#        #存储准确位置
        self.x = float(self.rect.x)

    def update(self):
        """向左移动"""
        self.x -= self.sets.block_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
