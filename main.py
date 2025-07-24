import pygame
import random
import time
import math
from collections import deque

pygame.init()

class MouseSensitivityTester:
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Mouse Sensitivity Tester")
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.circle_radius = 25
        self.circle_pos = None
        self.circle_spawn_time = 0
        self.next_spawn_delay = random.uniform(1.0, 3.0)
        
        self.mouse_delay = 0.5
        self.mouse_positions = deque(maxlen=1000)
        self.delayed_mouse_pos = (0, 0)
        
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        
        self.hits = 0
        self.total_spawns = 0
        self.show_settings = False
        
        pygame.mouse.set_visible(True)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_s:
                    self.show_settings = not self.show_settings
                elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    self.circle_radius = min(100, self.circle_radius + 5)
                elif event.key == pygame.K_MINUS:
                    self.circle_radius = max(5, self.circle_radius - 5)
                elif event.key == pygame.K_UP:
                    self.mouse_delay = min(2.0, self.mouse_delay + 0.1)
                elif event.key == pygame.K_DOWN:
                    self.mouse_delay = max(0.0, self.mouse_delay - 0.1)
                elif event.key == pygame.K_r:
                    self.hits = 0
                    self.total_spawns = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.circle_pos:
                    mouse_x, mouse_y = event.pos
                    circle_x, circle_y = self.circle_pos
                    distance = math.sqrt((mouse_x - circle_x)**2 + (mouse_y - circle_y)**2)
                    if distance <= self.circle_radius:
                        self.hits += 1
                        self.circle_pos = None
    
    def update_mouse_delay(self):
        current_time = time.time()
        current_pos = pygame.mouse.get_pos()
        
        self.mouse_positions.append((current_pos, current_time))
        
        target_time = current_time - self.mouse_delay
        
        for pos, timestamp in self.mouse_positions:
            if timestamp <= target_time:
                self.delayed_mouse_pos = pos
            else:
                break
    
    def spawn_circle(self):
        current_time = time.time()
        
        if self.circle_pos is None and current_time - self.circle_spawn_time >= self.next_spawn_delay:
            margin = self.circle_radius + 10
            x = random.randint(margin, self.screen_width - margin)
            y = random.randint(margin, self.screen_height - margin)
            self.circle_pos = (x, y)
            self.circle_spawn_time = current_time
            self.next_spawn_delay = random.uniform(0.5, 2.5)
            self.total_spawns += 1
        
        elif self.circle_pos and current_time - self.circle_spawn_time >= 2.0:
            self.circle_pos = None
    
    def draw(self):
        self.screen.fill(self.BLACK)
        
        if self.circle_pos:
            pygame.draw.circle(self.screen, self.WHITE, self.circle_pos, self.circle_radius)
        
        pygame.draw.circle(self.screen, self.GREEN, self.delayed_mouse_pos, 5)
        
        if self.show_settings:
            font = pygame.font.Font(None, 36)
            settings_text = [
                f"Circle Size: {self.circle_radius} (±/- to change)",
                f"Mouse Delay: {self.mouse_delay:.1f}s (‘/“ to change)",
                f"Hits: {self.hits}/{self.total_spawns} ({(self.hits/max(1,self.total_spawns)*100):.1f}%)",
                "",
                "Controls:",
                "S - Toggle settings",
                "R - Reset stats",
                "ESC - Exit"
            ]
            
            for i, text in enumerate(settings_text):
                surface = font.render(text, True, self.WHITE)
                self.screen.blit(surface, (20, 20 + i * 40))
        else:
            font = pygame.font.Font(None, 24)
            help_text = font.render("Press 'S' for settings", True, self.WHITE)
            self.screen.blit(help_text, (20, 20))
            
            stats_text = font.render(f"Hits: {self.hits}/{self.total_spawns}", True, self.WHITE)
            self.screen.blit(stats_text, (20, 50))
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update_mouse_delay()
            self.spawn_circle()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    tester = MouseSensitivityTester()
    tester.run()