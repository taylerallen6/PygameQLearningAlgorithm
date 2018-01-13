import sys, pygame
from Player_display import PlayerDisplay
from Game_objects import *
from Environment import Environment
from QLearner import QAgent

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 20)

size = width, height = 900, 700
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

wins = 0
total_time_count = 0


env = Environment()
env.maze_design_3()
reward_obj = env.game_object_list[-1]


while True:
    player = PlayerDisplay(x_pos=300, y_pos=150, speed=50)

    total_reward = 0
    time_count = 0
    done = False

    # pygame.key.set_repeat(1, 10)

    while True and not done:
        clock.tick(60)
        reward = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_LEFT:
                    player.rect = player.rect.move(-player.speed, 0)
                    if (player.rect.left < 0):
                        player.rect.left = 0
                    player.collision_left(env.game_object_list)
                if event.key == pygame.K_RIGHT:
                    player.rect = player.rect.move(player.speed, 0)
                    if (player.rect.right > width):
                        player.rect.right = width
                    player.collision_right(env.game_object_list)
                if event.key == pygame.K_UP:
                    player.rect = player.rect.move(0, -player.speed)
                    if (player.rect.top < 0):
                        player.rect.top = 0
                    player.collision_top(env.game_object_list)
                if event.key == pygame.K_DOWN:
                    player.rect = player.rect.move(0, player.speed)
                    if (player.rect.bottom > height):
                        player.rect.bottom = height
                    player.collision_bottom(env.game_object_list)
                    

        reward -= 1
        if player.is_collided_with(reward_obj):
            reward += 10.0
            wins += 1
            done = True

        time_count += 1

        screen.fill(black)
        for game_object in env.game_object_list:
            screen.blit(game_object.display, game_object.rect)
        screen.blit(player.display, player.rect)

        screen.blit(my_font.render("wins = " + str(wins), False, white), (0, 0))
        screen.blit(my_font.render("time count = " + str(total_time_count), False, white), (0, 20))

        pygame.display.flip()

    total_time_count = time_count
