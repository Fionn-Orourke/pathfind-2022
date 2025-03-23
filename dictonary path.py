import pygame
import keyboard
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 225)
grey = (128, 128, 128)
yellow = (255, 255, 0)

WIDTH = 20
HEIGHT = 20
z = 0
MARGIN = 5

grid = []
for row in range(20):
    grid.append([])
    for column in range(20):
        grid[row].append(0)

pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("pathfinder")

done = False
end = False
clock = pygame.time.Clock()
c = 0
i = 0
obs = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    while obs == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if keyboard.is_pressed('RETURN'):

                obs = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                i += 1
                if i == 1:
                    grid[row][column] = -1
                if i == 2:
                    grid[row][column] = 200
                if i > 2:
                    grid[row][column] = 300

                print("Click ", pos, "Grid coordinates: ", row, column)
                screen.fill(BLACK)
                for row in range(10):
                    for column in range(10):
                        if grid[row][column] != -1:
                            color = WHITE
                        if grid[row][column] > 0:
                            color = grey
                        if grid[row][column] == -1:
                            color = GREEN
                        if grid[row][column] == 200:
                            color = RED
                        if grid[row][column] == 300:
                            color = BLUE
                        if grid[row][column] == 400:
                            color = yellow
                        pygame.draw.rect(screen,
                                         color,
                                         [(MARGIN + WIDTH) * column + MARGIN,
                                          (MARGIN + HEIGHT) * row + MARGIN,
                                          WIDTH,
                                          HEIGHT])

        clock.tick(60)

        pygame.display.flip()
        # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] > 0:
                color = grey

            if grid[row][column] == -1:
                color = GREEN
                start = row, column
            if grid[row][column] == 200:
                color = RED

            if grid[row][column] == 300:
                color = BLUE

            if grid[row][column] == 400:
                color = yellow

            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    y = start[0]
    x = start[1]
    # if y > 1 or start[1] < 9:
    if (y - 1) != -1 and (x + 1) != 10 and grid[y - 1][x + 1] != 300 and grid[y - 1][x + 1] != 400:
        grid[y - 1][x + 1] = 1.4  # northeast
    if (y + 1) != 10 and (x + 1) != 10 and grid[y + 1][x + 1] != 300 and grid[y + 1][x + 1] != 400:  #
        grid[y + 1][x + 1] = 1.4  # southeast
    if (y + 1) != 10 and (x - 1) != -1 and grid[y + 1][x - 1] != 300 and grid[y + 1][x - 1] != 400:
        grid[y + 1][x - 1] = 1.4  # southwest
    if (y - 1) != -1 and (x - 1) != -1 and grid[y - 1][x - 1] != 300 and grid[y - 1][x - 1] != 400:  #
        grid[y - 1][x - 1] = 1.4  # northwest

    if y > 0 and grid[y - 1][x] != 300 and grid[y - 1][x] != 400:
        grid[y - 1][x] = 1  # north
    if x < 9 and grid[y][x + 1] != 300 and grid[y][x + 1] != 400:
        grid[y][x + 1] = 1  # east
    if y < 9 and grid[y + 1][x] != 300 and grid[y + 1][x] != 400:
        grid[y + 1][x] = 1  # south
    if x > 0 and grid[y][x - 1] != 300 and grid[y][x - 1] != 400:
        grid[y][x - 1] = 1  # west

    for row in range(10):
        for column in range(10):
            if grid[row][column] > 0 and grid[row][column] != 300 and grid[row][column] != 200:
                if row >= 1 and grid[row - 1][column] != 300 and grid[row - 1][column] != 200 and grid[row - 1][column] != 400:  # north
                    if grid[row][column] + 1 < grid[row - 1][column] or grid[row - 1][column] == 0:
                        if grid[row - 1][column] != -1:
                            grid[row - 1][column] = grid[row][column] + 1

                if row < 9 and grid[row + 1][column] != 300 and grid[row + 1][column] != 200 and grid[row + 1][column] != 400:  # south
                    if grid[row][column] + 1 <= grid[row + 1][column] or grid[row + 1][column] == 0:
                        if grid[row + 1][column] != -1:
                            grid[row + 1][column] = grid[row][column] + 1

                if column < 9 and grid[row][column + 1] != 300 and grid[row][column + 1] != 200 and grid[row][column + 1] != 400:  # east
                    if grid[row][column] + 1 <= grid[row][column + 1] or grid[row][column + 1] == 0:
                        if grid[row][column + 1] != -1:
                            grid[row][column + 1] = grid[row][column] + 1

                if column > 0 and grid[row][column - 1] != 300 and grid[row][column - 1] != 200 and grid[row][column - 1] != 400:  # west
                    if grid[row][column] + 1 <= grid[row][column - 1] or grid[row][column - 1] == 0:
                        if grid[row][column - 1] != -1:
                            grid[row][column - 1] = grid[row][column] + 1
                # if (row - 1) != -1 and (column + 1) != 10 and grid[row-1][column+1] != 300:
                if row >= 1 and column < 9 and grid[row - 1][column + 1] != 300 and grid[row - 1][
                    column + 1] != 200 and grid[row - 1][column + 1] != 400:  # northeast
                    if grid[row][column] + 1.4 < grid[row - 1][column + 1] or grid[row - 1][column + 1] == 0:
                        if grid[row - 1][column + 1] != -1:
                            grid[row - 1][column + 1] = grid[row][column] + 1.4

                if row < 9 and column < 9 and grid[row + 1][column + 1] != 300 and grid[row + 1][
                    column + 1] != 200 and grid[row + 1][column + 1] != 400:  # southeast
                    if grid[row][column] + 1.4 < grid[row + 1][column + 1] or grid[row + 1][column + 1] == 0:
                        if grid[row + 1][column + 1] != -1:
                            grid[row + 1][column + 1] = grid[row][column] + 1.4

                if row < 9 and column > 0 and grid[row + 1][column - 1] != 300 and grid[row + 1][
                    column - 1] != 200 and grid[row + 1][column - 1] != 400:  # southwest
                    if grid[row][column] + 1.4 < grid[row + 1][column - 1] or grid[row + 1][column - 1] == 0:
                        if grid[row + 1][column - 1] != -1:
                            grid[row + 1][column - 1] = grid[row][column] + 1.4

                if row >= 1 and column > 0 and grid[row - 1][column - 1] != 300 and grid[row - 1][
                    column - 1] != 200 and grid[row - 1][column - 1] != 400:  # southwest
                    if grid[row][column] + 1.4 < grid[row - 1][column - 1] or grid[row - 1][column - 1] == 0:
                        if grid[row - 1][column - 1] != -1:
                            grid[row - 1][column - 1] = grid[row][column] + 1.4
    short = 100
    if z <= 0:
        for row in range(10):
            for column in range(10):
                if grid[row][column] == 200:
                    f = row
                    l = column


    if z > 0:
        f = o
        l = p

    for q in range(8):
        z += 1
        if (f - 1) != -1 and (l + 1) != 10:
            if grid[f - 1][l + 1] < short and grid[f - 1][l + 1] != -1:  # northeast
                short = grid[f - 1][l + 1]
                o = f - 1
                p = l + 1
        if (f + 1) != 10 and (l + 1) != 10:
            if grid[f + 1][l + 1] < short and grid[f + 1][l + 1] != -1:  # southeast
                short = grid[f + 1][l + 1]
                o = f + 1
                p = l + 1
        if (f + 1) != 10 and (l - 1) != -1:
            if grid[f + 1][l - 1] < short and grid[f + 1][l - 1] != -1:  # southwest
                short = grid[f + 1][l - 1]
                o = f + 1
                p = l - 1
        if (f - 1) != -1 and (l - 1) != -1:
            if grid[f - 1][l - 1] < short and grid[f - 1][l - 1] != -1:  # northwest
                short = grid[f - 1][l - 1]
                o = f - 1
                p = l - 1
        if f < 9:
            if grid[f + 1][l] < short and grid[f + 1][l] != -1:  # south
                short = grid[f + 1][l]
                o = f + 1
                p = l
        if f > 0:
            if grid[f - 1][l] < short and grid[f - 1][l] != -1:  # north
                short = grid[f - 1][l]
                o = f - 1
                p = l
        if l < 9:
            if grid[f][l + 1] < short and grid[f][l + 1] != -1:  # east
                short = grid[f][l + 1]
                o = f
                p = l + 1
        if l > 0:
            if grid[f][l - 1] < short and grid[f][l - 1] != -1:  # west
                short = grid[f][l - 1]
                o = f
                p = l - 1
        y = start[0]
        x = start[1]
        if y < 9:
            if grid[start[0] + 1][start[1]] == 400:
                end = True
        if y > 0:
            if grid[start[0] - 1][start[1]] == 400 :
                end = True
        if x < 9:
            if grid[start[0]][start[1] + 1] == 400:
                end = True
        if x > 0:
            if grid[start[0]][start[1] - 1] == 400:
                end = True
        if (y + 1) != 10 and (x + 1) != 10:
            if grid[start[0] + 1][start[1] + 1] == 400:
                end = True

        if (y + 1) != 10 and (x - 1) != -1:
            if grid[start[0] + 1][start[1] - 1] == 400:
                end = True

        if (y - 1) != -1 and (x - 1) != -1:
            if grid[start[0] - 1][start[1] - 1] == 400:
                end = True
        if (start[0] - 1) != -1 and (start[1] + 1) != 10:
            if grid[start[0] - 1][start[1] + 1] == 400:
                end = True
    if end == False:
        grid[o][p] = 400
    for row in range(10):
        for column in range(10):
            if grid[row][column] != -1:
                color = WHITE
            if grid[row][column] > 0:
                color = grey
            if grid[row][column] == -1:
                color = GREEN
            if grid[row][column] == 200:
                color = RED
            if grid[row][column] == 300:
                 color = BLUE
            if grid[row][column] == 400:
                 color = yellow
            pygame.draw.rect(screen,
                          color,
                              [(MARGIN + WIDTH) * column + MARGIN,
                               (MARGIN + HEIGHT) * row + MARGIN,
                               WIDTH,
                                      HEIGHT])
    clock.tick(60)
    pygame.display.flip()










            # if column < 9 and grid[row][column + 1] != 300 and 200:
            #   if grid[row][column] + 1 >= grid[row][column + 1]:
            #      if grid[row][column + 1] != -1:
            #         grid[row][column + 1] += grid[row][column] + 1 # east

            # if row < 9 and grid[row][column + 1] != 300:
            #    if grid[row][column] + 1 > grid[row][column + 1]:
            #       if grid[row][column + 1] != -1:
            #          grid[row][column + 1] += 1
            # grid[y][x + 1] = 1  # east

            # if row >= 1 and grid[row + 1][column] != 300:
            #   if grid[row][column] + 1 > grid[row + 1][column]:
            #      if grid[row + 1][column] != -1:
            #         grid[row + 1][column] += 1

    # for line in grid:
    #    for column in line:
    #       if grid[line][column] >= 0:
    #          if grid[row][column] != 300:
    #             print(grid[row][column])

    clock.tick(60)

    pygame.display.flip()
print(grid[start[0]][start[1]])
print(grid)
print(start)
print((y))

pygame.quit()
