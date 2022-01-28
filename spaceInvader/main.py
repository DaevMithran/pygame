import pygame
import random

# Initialize
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./assets/ufo.png')
pygame.display.set_icon(icon)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 20)

textX = 10
textY = 10

# Player
playerImg = pygame.image.load('./assets/spaceship.png')
playerX = 370
playerY = 480
playerSpeed = 0.5
playerX_change = 0
playerRect = playerImg.get_rect()

# Enemy
num_of_enemies = 3
enemyImg = pygame.image.load('./assets/enemy.png')
enemyX = []
enemyY = []
enemyRect = []
enemySpeed = 0.7
enemyX_change = [enemySpeed] * num_of_enemies
enemyY_change = 70

for i in range(num_of_enemies):
    enemyX.append(random.choice([850, -100]))
    enemyY.append(random.randint(10, 150))
    enemyRect.append(enemyImg.get_rect())

# Bullets
bulletImg = pygame.image.load('./assets/bullet.png')
bulletX = playerX
bulletY = 460
bulletY_change = -1
bulletRect1 = bulletImg.get_rect()
bulletRect2 = bulletImg.get_rect()


def score():
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (textX, textY))


def player(x, y):
    playerRect.x = x
    playerRect.y = y
    screen.blit(playerImg, playerRect)


def enemy(i, x, y):
    enemyRect[i].x = x
    enemyRect[i].y = y
    screen.blit(enemyImg, enemyRect[i])


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


def reload_enemy(i):
    enemyY[i] = random.randint(10, 150)
    enemyX[i] = random.choice([850, -100])


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
                playerX_change = -playerSpeed
            if event.key == pygame.K_RIGHT:
                playerX_change = playerSpeed
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

    # Enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        # boundary conditions
        if enemyX[i] <= -100:
            enemyX_change[i] = enemySpeed
            enemyY[i] += enemyY_change
        elif enemyX[i] > 850:
            enemyX_change[i] = -enemySpeed
            enemyY[i] += enemyY_change

        enemy(i, enemyX[i], enemyY[i])

        if enemyRect[i].colliderect(playerRect):
            running = False

        if enemyRect[i].colliderect(bulletRect1) or enemyRect[i].colliderect(bulletRect2):
            score_value += 1
            reload_enemy(i)

    score()

    pygame.display.update()
