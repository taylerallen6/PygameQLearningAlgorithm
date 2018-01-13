import pygame


class WallBlock:
    def __init__(self, x_pos, y_pos, speed):
        self.solid = True
        png_image = pygame.image.load("/home/taylerallen6/Downloads/white_square.png")
        self.display = pygame.transform.scale(png_image, (50, 50))
        self.rect = self.display.get_rect(topleft=(x_pos, y_pos))
        self.speed = speed
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, move_x, move_y):
        self.rect = self.rect.move(move_x, move_y)


class Reward:
    def __init__(self, x_pos, y_pos, speed):
        self.solid = False
        png_image = pygame.image.load("/home/taylerallen6/Downloads/green_square.png")
        self.display = pygame.transform.scale(png_image, (30, 30))
        self.rect = self.display.get_rect(topleft=(x_pos, y_pos))
        self.speed = speed
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self):
        self.rect = self.rect.move([self.x_left_change + self.x_right_change, self.y_up_change + self.y_down_change])
