from microbit import display, button_a, button_b, sleep, Image
import random

# direction on x/y
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# keep track of the direction
i = 0

# starting coordinates for the snake
x = 0
y = 0

level = 1
score = 0
score_increment = 1

# time until next move
snake_speed = 1000

# first apple
display.set_pixel(random.randint(0, 4), random.randint(0, 4) ,5)

snake = []

# starting point for the snake
display.set_pixel(x, y, 9)
snake.append((0, 0))


def next_level():
    global x
    global y
    global level
    global score_increment
    global snake_speed
    x = 0
    y = 0
    level += 1
    score_increment *= 10
    snake_speed  -= 100
    display.show(Image.YES)
    sleep(1000)
    display.scroll("Level: " + str(level))
    display.clear()
    snake.clear()
    snake.append((x, y))
    display.set_pixel(x, y, 9)
    display.set_pixel(random.randint(0, 4), random.randint(0, 4) ,5)

while True:
    sleep(snake_speed)

    # move left/right
    if button_a.was_pressed():
        i -= 1
        if i < 0:
            i = 3
    elif button_b.was_pressed():
        i += 1
        if i > 3:
            i = 0

    # move the snake
    x += dx[i]
    y += dy[i]

    # go through walls
    if x > 4:
        x = 0
    elif x < 0:
        x = 4
    if y > 4:
        y = 0
    elif y < 0:
        y = 4

    snake.append((x,y))

    # increase the score if touched an apple, place a new apple
    if display.get_pixel(x, y) == 5:
        score += score_increment
        while True:
            ax = random.randint(0, 4)
            ay = random.randint(0, 4)
            if (ax, ay) not in snake:
                break
        display.set_pixel(ax, ay, 5)
    elif display.get_pixel(x, y) == 9:
        # end the game if touched the snake
        display.clear()
        display.show(Image.NO)
        break
    else:
        # move the tail
        display.set_pixel(snake[0][0], snake[0][1], 0)
        del snake[0]

    display.set_pixel(x, y, 9)

    if len(snake) > 20:
        next_level()


sleep(1000)
while True:
    display.scroll(score)
    sleep(1000)
    if button_a.was_pressed():
        break





