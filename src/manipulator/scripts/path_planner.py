#   CS22B1090
#   Shubh Khandelwal

import gymnasium as gym
import numpy as np

class manipulator_environment(gym.Env):

    def __init__(self, grid_size):

        super(manipulator_environment, self).__init__()

        self.grid_size = grid_size
        self.action_space = gym.spaces.Discrete(6)  # 0: FRONT, 1: BACK, 2: LEFT, 3: RIGHT, 5: UP, 6: DOWN
        self.observation_space = gym.spaces.Discrete(grid_size[0] * grid_size[1] * grid_size[2])
        self.max_steps = 1000
        self.current_step = 0

        # self.space = np.zeros([])

        self.start_state = (0, 0, 1.3)
        self.goal_state = (0, 0, 0)

        self.state = self.start_state