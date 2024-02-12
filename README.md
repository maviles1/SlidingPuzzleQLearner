## TODO:

###Change the way it represents a solved state:

####By poor design choice we represent it as:

`[1,2,0]`
`[3,4,5]`
`[6,7,8] `

####where 0 is the empty tile but that is hella confusing. I suggest representing it as:

`[1,2,3]`
`[4,5,6]`
`[7,8,0]`

#### But any other implementations are welcome.

# SlidingPuzzleQLearner

## Objective:
The objective of this project is to implement a reinforcement learning strategy using Q-Learning to solve 3x3 sliding tile puzzles. The 3x3 sliding tile puzzle is a classic problem where a player must rearrange tiles in a 3x3 grid by sliding them into the empty space until the tiles are ordered sequentially from from 1 to 9.

## Overview:
The project involves developing an agent that learns to solve the sliding tile puzzle through trial and error. The agent will interact with the environment by making moves (up, down, left, or right) to rearrange the tiles. It will learn a policy by updating Q-values based on the rewards obtained from its actions and the resulting states.

## Components:
1. **Environment**: The environment represents the 3x3 sliding tile puzzle. It provides methods for generating initial puzzle configurations, executing actions (moves), and calculating rewards.
   
2. **Agent**: The agent is responsible for learning to solve the puzzle using Q-Learning. It maintains a Q-table that stores Q-values for state-action pairs and updates these values based on rewards obtained during exploration.

3. **Training Loop**: The training loop orchestrates the interaction between the agent and the environment. It controls the exploration and exploitation of the agent, updating Q-values, and tracking performance metrics.

## Implementation:
The implementation will involve the following steps:

1. **State Representation**: Design a method to represent the states of the puzzle. This representation should capture the arrangement of tiles on the board.

2. **Action Space**: Define the action space for the agent. In the case of a 3x3 puzzle, actions can include moving a tile up, down, left, or right.

3. **Q-Learning**: Implement the Q-Learning algorithm to learn the optimal policy for solving the puzzle. Update Q-values based on rewards and explore-exploit strategies.

4. **Training**: Train the agent by running episodes where it interacts with the environment, updating Q-values based on observed rewards.

5. **Evaluation**: Evaluate the performance of the trained agent by testing it on unseen puzzle configurations. Measure metrics such as average steps to solve, success rate, and convergence of Q-values.

## Dependencies:
- Python 3.x
- numpy
- PyGame

## Usage:
1. Clone the repository:

     git clone https://github.com/your_username/SlidingPuzzleQLearner.git

2. Navigate to the project directory:

   cd SlidingPuzzleQLearner

3. Run main.py:

   python main.py



   
