import numpy as np
import pandas as pd

class Die:
    ''' Initialize an N-sided die with weights that is meant to be rolled one or more times '''
    def __init__(self, faces):
        '''
        Creates the Die instance. Takes in an array of distnct die faces and initializes all their weights to 1
        
        INPUTS
        faces : NumPy array of strings, integers, or floats
        '''
        
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
        '''
        Changes the weight of a single side of the dice
        
        INPUTS
        face : string, integer, or float
            the face value to be changed, must be in the die darray
        new_weight : integer, float, or numeric string
            the new weight of the passed face on the die
        '''
        
        if face not in self._die_df.index:
            raise IndexError('Face passed must be a valid value')
        if type(new_weight) == str:
            if new_weight.isnumeric() == False:
                raise TypeError('String must be castable as numeric')
        elif type(new_weight) != int and type(new_weight) != float:
                raise TypeError('Value must be numeric or castable as numeric')
        else:
            self._die_df.loc[face] = new_weight

    def roll_die(self, n=1):
        '''
        Rolls the dice one or more times. Returns a list of the faces that the die rolled on
        
        INPUTS
        n : positive int
            number of times the die is to be rolled
            default: n=1
        
        OUTPUT
        list of die faces
        '''
        
        outcomes = []
        probs = self._die_df.weights / sum(self._die_df.weights)
        for i in range(n):
            outcome = np.random.choice(self._die_df.index.values, p = probs)
            outcomes.append(outcome)
        return outcomes


    def die_state(self):
        '''
        Show the die's current state, with each die face and their corresponding weights
        
        OUTPUT
        pandas dataframe
        '''
        
        return self._die_df.copy()
        

class Game:
    ''' Collection of dice with the purpose of rolling them and storing the results of the most recent play'''
    def __init__(self, dice):
        '''
        Game initializer
        
        INPUTS
        dice    list of Die objects
            All Die in the list have the same faces
        '''
        
        self.dice = dice

    def play(self, n):
        '''
       Rolls the dice a specified amount of times using the Die methods and stores them in a private dataframe
        
        INPUTS
        n : number of times to roll the dice
        '''
        
        result = pd.DataFrame()
        result.index.name = "roll_number"
        for i in range(0, len(self.dice)):
            result[i] = self.dice[i].roll_die(n)
        self._result = result

    def return_result(self, wide=True):
        '''
        Shows the results of the most recent play
        
        INPUTS
        wide : bool
            Whether the outputted dataframe should be in narrow or wide format
            Default: wide=True
        
        OUTPUT
        pandas dataframe of the roll results, in narrow or wide form
        '''
        
        if type(wide) != bool:
            raise ValueError('Must pass True or False for wide format')
        if wide == False:
            result_narrow = self._result.stack().to_frame('outcome')
            result_narrow.index.names = ['roll_number', 'die_number']
            return result_narrow.copy()
        return self._result.copy()
        
        
        
class Analyzer:
    ''' Takes the results of a Game object and computes properties and statistics of the game '''
    def __init__(self, game):
        '''
        Initializes Analyzer class
        
        INPUTS
        game    Game object
        '''
    
        if type(game) != Game:
            raise ValueError('Input must be a Game object')
        self.game = game
        
    def jackpot(self):
        '''
        Calculates number of instances where all faces are the same in a single roll, AKA a jackpot

        OUTPUT
        num_jackpot : int
        '''
        
        num_jackpot = 0
        results = self.game.return_result()
        for i in range(0, len(results)):
            result_row = results.iloc[i]
            if len(np.unique(result_row)) == 1:
                num_jackpot += 1
        return num_jackpot

    def face_counts(self):
        '''
        Computes how many times each face is rolled for each singular roll
        
        
        OUTPUT
        counts : pandas dataframe of counts for each roll
        '''
        results = self.game.return_result()
        faces = self.game.dice[0].die_state().index.values
        counts = pd.DataFrame(0, columns = faces, index = results.index)
        for i in range(0, len(results)):
            for j in results.columns:
                face_val = results.loc[i,j]
                counts.loc[(i, face_val)] += 1

        return counts

    def combo_count(self):
        '''
        Calculates the distinct combinations of faces rolled, in no particular order

        OUTPUT
        combos : pandas dataframe containing all of the combinations and their counts
        '''
        results = self.game.return_result()
        combinations = []
        for i in range(0, len(results)):
            permutation = results.iloc[i].sort_values()
            combinations.append(tuple(permutation))
        combos = pd.Series(combinations).value_counts().to_frame()
        index = pd.MultiIndex.from_tuples(combos.index.values)
        combos = combos.set_index(index)
        return combos

    def permutation_count(self):
        '''
        Calculates the distinct, order-dependent permutations of faces rolled

        OUTPUT
        perms : pandas dataframe containing all of the permutations and their counts
        '''
        results = self.game.return_result()
        combinations = []
        for i in range(0, len(results)):
            permutation = results.iloc[i]
            combinations.append(tuple(permutation))
        perms = pd.Series(combinations).value_counts().to_frame()
        index = pd.MultiIndex.from_tuples(perms.index.values)
        perms = perms.set_index(index)
        return perms