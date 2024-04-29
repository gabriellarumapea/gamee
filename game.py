# abstraksi
import pygame
import random

# Abstract base class for game objects
class GameObject(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        pass  # Abstract method, to be overridden by subclasses

# polimorfisme
# Subclass for player's spaceship
class Player(GameObject):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

# Subclass for enemy spaceships
class Enemy(GameObject):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
        self.speed = random.randint(2, 4)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.rect.y = random.randint(-100, -50)
            self.rect.x = random.randint(50, 750)

# pewarisan 
# Subclass for bullets
class Bullet(GameObject):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# enkapsulasi

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space War")

# Objek
player = Player("player.png", 400, 500)
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Loop Game
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet("bullet.png", player.rect.centerx, player.rect.top)
                bullets.add(bullet)

    # Update
    player.update()
    enemies.update()
    bullets.update()

    for enemy in pygame.sprite.spritecollide(player, enemies, False):
        # Game over logic
        running = False

    for bullet in pygame.sprite.groupcollide(bullets, enemies, True, True):
        # Enemy destroyed logic
        pass  # Add score, play sound, etc.

    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)

    enemies.draw(screen)
    bullets.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
