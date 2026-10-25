import pygame
import sys
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK, WHITE, RETRO_PINK
from src.snake import FlappySnake
from src.pipe import Pipe

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Snake Arcade")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        
        self.reset_game()

    def reset_game(self):
        self.snake = FlappySnake()
        self.pipes = [Pipe()]
        self.score = 0
        self.spawn_timer = 0
        self.game_over = False

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.handle_events()
            if not self.game_over:
                self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    if self.game_over:
                        self.reset_game()
                    else:
                        self.snake.flap()

    def update(self):
        self.snake.update()
        
        # Rohre spawnen
        self.spawn_timer += 1
        if self.spawn_timer > 90:
            self.pipes.append(Pipe())
            self.spawn_timer = 0

        snake_rects = self.snake.get_rects()
        
        for pipe in self.pipes[:]:
            pipe.update()
            
            # Punktzahl erhöhen
            if not pipe.passed and pipe.x + pipe.width < self.snake.x:
                self.score += 1
                pipe.passed = True

            # Kollision prüfen (Kopf ODER Schwanz treffen Rohr)
            if pipe.collides_with(snake_rects):
                self.game_over = True

            if pipe.x + pipe.width < 0:
                self.pipes.remove(pipe)

        # Boden- und Deckenkollision
        head_rect = snake_rects[0]
        if head_rect.top < 0 or head_rect.bottom > SCREEN_HEIGHT:
            self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)
        
        for pipe in self.pipes:
            pipe.draw(self.screen)
            
        self.snake.draw(self.screen)
        
        # Score anzeigen
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (20, 20))

        if self.game_over:
            go_text = self.font.render("GAME OVER - Leertaste zum Neustarten", True, RETRO_PINK)
            self.screen.blit(go_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))

        pygame.display.flip()
      
