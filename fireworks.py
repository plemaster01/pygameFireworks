import pygame, random

pygame.init()

WIDTH = 500
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption('Jetpack Joyride Rebuild!')
fps = 60
timer = pygame.time.Clock()
fireworks = []
counter = 0
new_fireworks = True
colors = [(255, 0, 0), (0, 0, 255), (255, 255, 255)]
projectiles = []


def draw_fireworks(firework_list, projectile_list):
    remove = []
    # comment out this line if you want the fireworks trails to stay on screen
    # surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    directions = [(1, 1), (1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
    for i in range(len(firework_list)):
        if firework_list[i][3] < counter and firework_list[i][2] < firework_list[i][1]:
            pygame.draw.rect(screen, firework_list[i][4], [firework_list[i][0], firework_list[i][1], 10, 10], 0, 3)
            firework_list[i][1] -= 7
        elif firework_list[i][2] >= firework_list[i][1]:
            x_start = firework_list[i][0]
            y_start = firework_list[i][1]
            # x and y directions
            # each projectile needs to store x and y pos, dir, y velocity, color, and time remaining before disappearing
            for j in range(len(directions)):
                projectile_list.append(
                    [x_start, y_start, directions[j][0] * 3, directions[j][1] * 3, firework_list[i][4], 60])
            remove.append(i)
    remove.sort(reverse=True)
    for r in remove:
        print(f'fireworks removal: {r}')
        firework_list.remove(firework_list[r])

    remove = []
    for i in range(len(projectile_list)):
        color = projectile_list[i][4][0], projectile_list[i][4][1], projectile_list[i][4][2], projectile_list[i][5] * 4
        pygame.draw.circle(surface, color, (projectile_list[i][0], projectile_list[i][1]), 3)
        projectile_list[i][5] -= 1
        projectile_list[i][0] += projectile_list[i][2]
        projectile_list[i][1] += projectile_list[i][3]
        projectile_list[i][3] += 0.1
        if projectile_list[i][5] < 0 or WIDTH < projectile_list[i][0] < -3 or HEIGHT < projectile_list[i][0]:
            remove.append(i)
    for p in range(len(remove)):
        projectile_list.pop(0)
    screen.blit(surface, (0, 0))
    return firework_list, projectile_list


run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    counter += 1
    if new_fireworks:
        for q in range(30):
            # starting x pos, starting y pos, explosion height, delay before launching
            fireworks.append(
                [random.randint(10, WIDTH - 10), HEIGHT, random.randint(10, HEIGHT / 2), random.randint(0, 300),
                 random.choice(colors)])
        new_fireworks = False
    fireworks, projectiles = draw_fireworks(fireworks, projectiles)

    if len(fireworks) == 0 and len(projectiles) == 0:
        counter = 0
        new_fireworks = True
        # add this line instead of inside the draw function if you want every round of fireworks to stay on screen
        surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
