import numpy as np
import math
import random
class Puzzle():
    def __init__(self, puzzle_arr: np.array = None, q_table = None):
        if puzzle_arr is not None:
            self.puzzle = puzzle_arr
        else:
            puzzle = np.zeros(shape=(3, 3))
            counter = 1
            for i in range(3):
                for j in range(3):
                    if i == 0 and j == 2:
                        puzzle[i,j] = 0
                    else:
                        puzzle[i,j] = counter
                        counter += 1
            self.puzzle = puzzle
        if puzzle_arr is not None:
            self.q_table = q_table
        else:
            self.q_table = {}


    def is_solved(self):
        rows, cols = np.shape(self.puzzle)
        counter = 1
        if self.puzzle[0,cols - 1] != 0:
            return False
        for row in range(rows):
            for col in range(cols):
                if self.puzzle[row,col] != 0:
                    if  self.puzzle[row,col ]!= counter:
                        return False
                    else:    
                        counter += 1
        return True

    def get_movable_pieces(self):
        movable_pieces = []
        row,col = self._get_empty_tile()
        for i in range(-1,2):
            for j in range(-1,2):
                if abs(i) != abs(j):
                    if (row + i < np.shape(self.puzzle)[0] and row + i >= 0 ) and (col + j < np.shape(self.puzzle)[1] and col + j >= 0 ):
                        movable_pieces.append((row+i,col+j))
        return movable_pieces
    
    def scramble(self, steps = 20):

        for step in range(steps):
            zero_tile = self._get_empty_tile()
            move_tile = random.sample(self.get_movable_pieces(),1)[0]
            self._swap(zero_tile,move_tile)

            
    def _get_empty_tile(self):
        for i in range(np.shape(self.puzzle)[0]):
            for j in range(np.shape(self.puzzle)[1]):
                if self.puzzle[i,j] == 0:
                    return i,j
    
    def _swap(self, pos1: tuple, pos2: tuple):
        temp = self.puzzle[pos1[0],pos1[1]]
        self.puzzle[pos1[0],pos1[1]] = self.puzzle[pos2[0],pos2[1]]
        self.puzzle[pos2[0],pos2[1]] = temp

    def q_learning(self, num_episodes=10, learning_rate=0.1, discount_factor=0.9, exploration_prob=0.2):
        for episode in range(num_episodes):
            while not self.is_solved():
                state = self.get_state_representation()
                action = self.select_action(state, exploration_prob)
                reward = self.perform_action(action)
                next_state = self.get_state_representation(action)

                # Q-value update
                self.update_q_value(state, action, reward, next_state, learning_rate, discount_factor)


    def get_state_representation(self, action = None):
        if action:
            self._swap(self._get_empty_tile(), action)
            return tuple(self.puzzle.flatten()), self._get_empty_tile()

        return tuple(self.puzzle.flatten()), self._get_empty_tile()

    def select_action(self, state, exploration_prob):
        if state not in self.q_table or random.uniform(0, 1) < exploration_prob or self.q_table[state] == {}:
            return random.choice(self.get_movable_pieces())
        else:
            action = -10,-10
            maximum = -5
            for key in self.q_table[state].keys():
                if self.q_table[state][key] > maximum:
                    maximum = self.q_table[state][key]
                    action = key
            
            return action

    def perform_action(self, action):
        zero_tile = self._get_empty_tile()
        self._swap(zero_tile, action)
        return -1 if not self.is_solved() else 1

    def update_q_value(self, state, action, reward, next_state, learning_rate, discount_factor):
        state = tuple(state) 
        action = tuple(action)
        
        if state not in self.q_table or action not in self.q_table[state].keys():
            self.q_table[state] = {action: 0}

        if next_state not in self.q_table:
            self.q_table[next_state] = {}
        max_next_q_value = max(self.q_table[next_state].values()) if self.q_table[next_state] else 0
        # print(self.q_table) 
        current_q_value = self.q_table[state][action]
        self.q_table[state][action] = (1 - learning_rate) * current_q_value + \
            learning_rate * (reward + discount_factor * max_next_q_value)

