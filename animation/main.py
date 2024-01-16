import pygame
import spritesheet

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheets")

BG = (255, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Loading sprite sheet image
sprite_sheet_image = pygame.image.load('../spritesheet/hollow_knight_spritesheet.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

# Variables for animation
animation_list = []
animation_steps = [1, 4, 6, 8]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 150
frame = 0
step_counter = 0
animation_start = False
flip = False

# Knight's movement
animation_list_x = 300
animation_list_y = 500
move_left = False
move_right = False

# Knight's jump
jump = False
gravity = 1
jump_height = 20
y_velocity = jump_height

# Putting animation images in the main list
for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 77, 77, 2, WHITE))
        step_counter += 1
    animation_list.append(temp_img_list)

run = True
while run:

    screen.fill(BG)

    current_time = pygame.time.get_ticks()
    # Moving the images
    if animation_start:
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list[action]):
                frame = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                action = 1
                frame = 0
                animation_start = True
                move_right = True
                flip = False
            if event.key == pygame.K_LEFT:
                action = 1
                frame = 0
                animation_start = True
                move_left = True
                flip = True
            if event.key == pygame.K_UP:
                action = 3
                frame = 0
                animation_start = True
                jump = True
            if event.key == pygame.K_SPACE:
                action = 2
                frame = 0
                animation_start = True
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                action = 0
                frame = 0
                move_right = False
                flip = False
            if event.key == pygame.K_LEFT:
                action = 0
                frame = 0
                move_left = False
                flip = True
            if event.key == pygame.K_UP:
                action = 3
            if event.key == pygame.K_SPACE:
                action = 0
                frame = 0

    if move_left:
        animation_list_x -= 5
    if move_right:
        animation_list_x += 5
    if jump:
        animation_list_y -= y_velocity
        y_velocity -= gravity
        if y_velocity < -jump_height:
            jump = False
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        action = 0
                        frame = 0
                    if event.key == pygame.K_RIGHT:
                        action = 0
                        frame = 0
            action = 1
            frame = 0
            y_velocity = jump_height

    screen.blit(pygame.transform.flip(animation_list[action][frame], flip, False), (animation_list_x, animation_list_y))

    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
