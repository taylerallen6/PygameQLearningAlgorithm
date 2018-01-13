import random

class QAgent:
    def __init__(self, possible_actions):
        self.Qtable = []
        # self.learning_rate = learning_rate
        self.possible_actions = possible_actions

        self.initial_state = 0
        self.initial_action_index = 0
        self.outcome_state = 0
        self.outcome_action_value = 0

        self.lr = .8
        self.y = .95

        self.firstIteration = True

    def main(self, cur_state, reward):
        if not self.firstIteration:
            self.outcome_state = cur_state

            exists = False
            for state in self.Qtable:
                if state[0] == self.outcome_state:
                    exists = True
                    self.outcome_action_value = max(state[1])

            for state in self.Qtable:
                if state[0] == self.initial_state:
                    if exists:
                        state[1][self.initial_action_index] += self.lr * (reward + self.y * self.outcome_action_value - state[1][self.initial_action_index])

                    if not exists:
                        state[1][self.initial_action_index] += self.lr * (reward + self.y * 0 - state[1][self.initial_action_index])

        self.initial_state = cur_state
        action_index = random.choice(list(range(self.possible_actions)))

        self.firstIteration = False

        exists = False
        if len(self.Qtable) > 0:
            for state in self.Qtable:
                if state[0] == self.initial_state:
                    exists = True
                    self.initial_action_index = state[1].index(max(state[1]))
                    return self.initial_action_index

        if not exists:
            self.Qtable.append([self.initial_state, [0] * self.possible_actions])

        print("Qtable count:   " + str(len(self.Qtable)))

        self.initial_action_index = action_index
        return self.initial_action_index

