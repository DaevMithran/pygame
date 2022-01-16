import pygame
import random

# Initialize
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerRect = playerImg.get_rect()

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(0, 150)
enemyX_change = 0.3
enemyY_change = 70
enemyRect = enemyImg.get_rect()

# Bullets
bulletImg = pygame.image.load('bullet.png')
bulletX = playerX
bulletY = 460
bulletY_change = -1
bulletRect1 = bulletImg.get_rect()
bulletRect2 = bulletImg.get_rect()


def player(x, y):
    playerRect.x = x
    playerRect.y = y
    screen.blit(playerImg, playerRect)


def enemy(x, y):
    enemyRect.x = x
    enemyRect.y = y
    screen.blit(enemyImg, enemyRect)


def bullet(x, y):
    bulletRect1.x = x - 12
    bulletRect1.y = y
    bulletRect2.x = x + 44
    bulletRect2.y = y
    screen.blit(bulletImg, bulletRect1)
    screen.blit(bulletImg, bulletRect2)


def reload_bullet():
    global bulletY, bulletX
    bulletY = 460
    bulletX = playerX


# Game Loop
running = True
shoot = False
while running:
    screen.fill((155, 200, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # KEYDOWN : key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bulletY <= 0:
                    reload_bullet()
                shoot = True
        # KEYUP: key release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # player should be drawn after screen fill
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    player(playerX, playerY)
    if shoot:
        bulletY += bulletY_change
        bullet(bulletX, bulletY)

    enemyX += enemyX_change
    if enemyX <= -100:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX > 850:
        enemyX_change = -0.3
        enemyY += enemyY_change

    enemy(enemyX, enemyY)

    if enemyRect.colliderect(playerRect):
        running = False

    if enemyRect.colliderect(bulletRect1):
        print('Killed enemy')

    if enemyRect.colliderect(bulletRect2):
        print('Killed enemy')

    pygame.display.update()
