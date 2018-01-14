# Pygame QLearning Algorithm #

This Q learning agent is built in a pygame environment. The Q learning agent code is kept seperate from the pygame environment code in the [Qlearner.py](Qlearner.py) file. This is the brain of the program. This is so the agent can be taken out of the pygame environment and used in other environments.

## Requiremnets: ##
- [python](https://www.python.org/downloads/)
- [pygame](https://www.pygame.org/)
- files from in the repository.

To run this code, first install [python](https://www.python.org/downloads/) and [pygame](https://www.pygame.org/). Then clone or download this repository and run the [main.py](main.py) file in python. 

![](READMEcontent/PygameQlearnerImage.png)

The Q learning agent is a reinforcement learning agent that learns to achieve a goal through recieving a reward. In this example, the agent recieves a positive reward of 50 points for each time it makes it to the green square and recieves a negative reward of -1 for each move it makes. It can only make 4 moves: up, down, left, and right. Once it makes it to the green square, it restarts to its original position and tries again, each time getting closer to the optimal path.

(NOTE: It cannot "see" the green square or its surroundings. It is only aware of its x and y coordinates and the reward it recieves.)

## Q Learning Algorithm ##

An detailed explanation of the Q learning algorithm can be found at [http://www.cse.unsw.edu.au/~cs9417ml/RL1/algorithms.html](http://www.cse.unsw.edu.au/~cs9417ml/RL1/algorithms.html) but here is short explaination from the article:

1. Initialize the Q-values table, Q(s, a).
2. Observe the current state, s.
3. Choose an action, a, for that state based on an action selection policies (this example uses a Greedy policy).
4. Take the action, and observe the reward, r, as well as the new state, s'.
5. Update the Q-value for the state using the following formula:

      Q(s, a) <-- Q(s, a) + alpha [r + y MAXa'Q(s', a) - Q(s, a)]
6. Set the state to the new state, and repeat the process until a terminal state is reached.


