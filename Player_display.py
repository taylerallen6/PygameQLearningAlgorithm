import pygame


class PlayerDisplay:
    def __init__(self, x_pos, y_pos, speed, possible_actions):
        self.solid = True
        png_image = pygame.image.load("/home/taylerallen6/Downloads/angry_ball.png")
        self.display = pygame.transform.scale(png_image, (50, 50))
        self.rect = self.display.get_rect(topleft=(x_pos, y_pos))
        self.speed = speed
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.possible_actions = possible_actions

    def move(self, move_x, move_y):
        self.rect = self.rect.move(move_x, move_y)

    def is_collided_with(self, game_object):
        return self.rect.colliderect(game_object)

    def collision_left(self, game_object_list):
        for game_object in game_object_list:
            if game_object.solid:
                if self.is_collided_with(game_object):
                    if self.rect.left < game_object.rect.right:
                        self.rect.left = game_object.rect.right

    def collision_right(self, game_object_list):
        for game_object in game_object_list:
            if game_object.solid:
                if self.is_collided_with(game_object):
                    if self.rect.right > game_object.rect.left:
                        self.rect.right = game_object.rect.left

    def collision_top(self, game_object_list):
        for game_object in game_object_list:
            if game_object.solid:
                if self.is_collided_with(game_object):
                    if self.rect.top < game_object.rect.bottom:
                        self.rect.top = game_object.rect.bottom

    def collision_bottom(self, game_object_list):
        for game_object in game_object_list:
            if game_object.solid:
                if self.is_collided_with(game_object):
                    if self.rect.bottom > game_object.rect.top:
                        self.rect.bottom = game_object.rect.top
