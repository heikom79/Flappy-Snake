import pygame
from src.settings import SCREEN_HEIGHT, RETRO_GREEN, RETRO_PINK

class FlappySnake:
    def __init__(self):
        self.x = 200
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.gravity = 0.5
        self.lift = -8
        self.radius = 12
        
        # Snake-Körper: Speichert die letzten Positionen für den Schwanz
        self.history = []
        self.length = 12  # Anzahl der Segmente
        for i in range(self.length):
            self.history.append((self.x - i * 10, self.y))

    def flap(self):
        self.velocity = self.lift

    def update(self):
        # Schwerkraft anwenden
        self.velocity += self.gravity
        self.y += self.velocity

        # Position in die Historie einfügen (für den Schlangenkörper)
        self.history.insert(0, (self.x, self.y))
        if len(self.history) > self.length * 6:
            self.history.pop()

    def draw(self, screen):
        # Zeichne den Körper und Kopf
        for i, pos in enumerate(self.history[::6]):
            color = RETRO_GREEN if i == 0 else RETRO_PINK
            pygame.draw.circle(screen, color, (int(pos[0]), int(pos[1])), self.radius)

    def get_rects(self):
        # Gibt Kollisions-Rects für den Kopf und alle Segmente zurück
        rects = []
        for pos in self.history[::6]:
            rects.append(pygame.Rect(pos[0] - self.radius, pos[1] - self.radius, self.radius * 2, self.radius * 2))
        return rects
      
