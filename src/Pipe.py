import pygame
import random
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_COLOR

class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.width = 70
        self.gap = 190
        self.top = random.randint(60, SCREEN_HEIGHT - self.gap - 60)
        self.bottom = self.top + self.gap
        self.speed = 4
        self.passed = False

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        # Oberes Rohr
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, 0, self.width, self.top))
        # Unteres Rohr
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, self.bottom, self.width, SCREEN_HEIGHT - self.bottom))

    def collides_with(self, rects):
        top_rect = pygame.Rect(self.x, 0, self.width, self.top)
        bottom_rect = pygame.Rect(self.x, self.bottom, self.width, SCREEN_HEIGHT - self.bottom)
        
        for rect in rects:
            if rect.colliderect(top_rect) or rect.colliderect(bottom_rect):
                return True
        return False
      
