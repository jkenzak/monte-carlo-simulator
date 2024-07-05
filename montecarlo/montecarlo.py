import numpy as np
import pandas as pd

class Die:
    def __init__(self, faces):
        if type(faces) != np.ndarray:
            raise TypeError('Input must be a NumPy array')

        if len(np.unique(faces)) != len(faces):
            raise ValueError('The array\'s values must be distinct')

        weights = np.ones(len(faces))

        self._die_df = pd.DataFrame({
            'faces': faces,
            'weights': weights
        }).set_index('faces')

    def change_weight(self, face, new_weight):
        if face not in self._die_df.index:
            raise IndexError('Face passed must be a valid value')
    ## What about boolean???
        if type(new_weight) == str:
            if new_weight.isnumeric() == False:
                raise TypeError('String must be castable as numeric')
        elif type(new_weight) != int and type(new_weight) != float:
                raise TypeError('Value must be numeric or castable as numeric')
        else:
            self._die_df.loc[face] = new_weight

    def roll_die(self, n=1):
        outcomes = []
        probs = self._die_df.weights / sum(self._die_df.weights)
        for i in range(n):
            outcome = np.random.choice(self._die_df.index.values, p = probs)
            outcomes.append(outcome)
        return outcomes


    def die_state(self):
        return self._die_df.copy()
        

class Game:
    def __init__(self, dice):
        self.dice = dice

    def play(self, n):
        self._result = pd.DataFrame()
        for die in self.dice:
            self._result[die.index] = die.roll_die(n)
        self._result.index.name = "roll_number"
            
        

class Analyzer:
    def __init__(self, game):
        if type(game) != Game:
            raise TypeError('Input must be a Game object')
        self.game = game
