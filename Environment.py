import pygame
from Game_objects import *

class Environment:
    def __init__(self):
        self.game_object_list = []

    def add_object(self, game_object):
        self.game_object_list.append(game_object)

    def maze_design_1(self):
        # beginning
        self.add_object(WallBlock(x_pos=250, y_pos=150, speed=1))

        # top right row
        self.add_object(WallBlock(x_pos=300, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=350, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=400, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=450, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=450, y_pos=150, speed=1))
        self.add_object(WallBlock(x_pos=450, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=500, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=550, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=250, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=300, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=350, speed=1))

        # bottom left row
        self.add_object(WallBlock(x_pos=300, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=350, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=350, y_pos=250, speed=1))
        self.add_object(WallBlock(x_pos=350, y_pos=300, speed=1))
        self.add_object(WallBlock(x_pos=400, y_pos=300, speed=1))
        self.add_object(WallBlock(x_pos=450, y_pos=300, speed=1))
        self.add_object(WallBlock(x_pos=500, y_pos=300, speed=1))
        self.add_object(WallBlock(x_pos=500, y_pos=350, speed=1))
        self.add_object(WallBlock(x_pos=500, y_pos=350, speed=1))
        self.add_object(WallBlock(x_pos=500, y_pos=350, speed=1))
        self.add_object(WallBlock(x_pos=500, y_pos=350, speed=1))
        self.add_object(WallBlock(x_pos=500, y_pos=350, speed=1))

        # end
        self.add_object(WallBlock(x_pos=550, y_pos=400, speed=1))

        # reward_obj
        self.add_object(Reward(x_pos=560, y_pos=360, speed=1))


    def maze_design_2(self):
        # beginning
        self.add_object(WallBlock(x_pos=250, y_pos=150, speed=1))

        # top right row
        self.add_object(WallBlock(x_pos=250, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=350, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=400, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=450, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=500, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=550, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=150, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=250, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=300, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=350, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=400, speed=1))

        # bottom left row
        self.add_object(WallBlock(x_pos=250, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=250, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=250, y_pos=250, speed=1))
        self.add_object(WallBlock(x_pos=250, y_pos=300, speed=1))
        self.add_object(WallBlock(x_pos=250, y_pos=350, speed=1))
        self.add_object(WallBlock(x_pos=250, y_pos=400, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=400, speed=1))
        self.add_object(WallBlock(x_pos=350, y_pos=400, speed=1))
        self.add_object(WallBlock(x_pos=400, y_pos=400, speed=1))
        self.add_object(WallBlock(x_pos=450, y_pos=400, speed=1))
        self.add_object(WallBlock(x_pos=500, y_pos=400, speed=1))

        # end
        self.add_object(WallBlock(x_pos=550, y_pos=400, speed=1))

        # reward_obj
        self.add_object(Reward(x_pos=560, y_pos=360, speed=1))


    def maze_design_3(self):
        # beginning
        self.add_object(WallBlock(x_pos=250, y_pos=150, speed=1))

        # top right row
        self.add_object(WallBlock(x_pos=250, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=350, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=400, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=450, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=500, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=550, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=150, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=250, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=300, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=350, speed=1))
        self.add_object(WallBlock(x_pos=600, y_pos=400, speed=1))

        # bottom left row
        self.add_object(WallBlock(x_pos=250, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=250, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=250, y_pos=250, speed=1))
        self.add_object(WallBlock(x_pos=250, y_pos=300, speed=1))
        self.add_object(WallBlock(x_pos=250, y_pos=350, speed=1))
        self.add_object(WallBlock(x_pos=250, y_pos=400, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=400, speed=1))
        self.add_object(WallBlock(x_pos=350, y_pos=400, speed=1))
        self.add_object(WallBlock(x_pos=400, y_pos=400, speed=1))
        self.add_object(WallBlock(x_pos=450, y_pos=400, speed=1))
        self.add_object(WallBlock(x_pos=500, y_pos=400, speed=1))

        # obstacles
        self.add_object(WallBlock(x_pos=450, y_pos=250, speed=1))
        self.add_object(WallBlock(x_pos=450, y_pos=300, speed=1))
        self.add_object(WallBlock(x_pos=400, y_pos=300, speed=1))

        # end
        self.add_object(WallBlock(x_pos=550, y_pos=400, speed=1))

        # reward_obj
        self.add_object(Reward(x_pos=560, y_pos=360, speed=1))

    def maze_design_4(self):
        # wall 1
        self.add_object(WallBlock(x_pos=100, y_pos=0, speed=1))
        self.add_object(WallBlock(x_pos=100, y_pos=50, speed=1))
        self.add_object(WallBlock(x_pos=100, y_pos=100, speed=1))
        self.add_object(WallBlock(x_pos=100, y_pos=150, speed=1))
        self.add_object(WallBlock(x_pos=100, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=100, y_pos=250, speed=1))
        self.add_object(WallBlock(x_pos=100, y_pos=300, speed=1))
        self.add_object(WallBlock(x_pos=100, y_pos=350, speed=1))
        self.add_object(WallBlock(x_pos=100, y_pos=400, speed=1))

        # wall 2
        self.add_object(WallBlock(x_pos=300, y_pos=650, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=600, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=550, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=500, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=450, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=400, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=350, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=300, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=250, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=200, speed=1))
        self.add_object(WallBlock(x_pos=300, y_pos=150, speed=1))

        # reward_obj
        self.add_object(Reward(x_pos=450, y_pos=350, speed=1))
