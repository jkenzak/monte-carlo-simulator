from montecarlo.montecarlo import Die, Game, Analyzer
import unittest
import numpy as np
import pandas as pd

class TestDieMethods(unittest.TestCase):
    def test_Die_initializer(self):
        die1 = Die(np.array(['H', 'T']))
        self.assertTrue(type(die1) == Die)

    def test_change_weight(self):
        die1 = Die(np.array(['H', 'T']))
        die1.change_weight('H', 5)
        statement = die1._die_df.loc['H'].values
        self.assertEqual(statement, 5)

    def test_roll_die(self):
        die1 = Die(np.array(['H', 'T']))
        die_rolls = die1.roll_die(5)
        statement = (len(die_rolls) == 5) & (type(die_rolls) == list)
        self.assertTrue(statement)

    def test_die_state(self):
        die1 = Die(np.array(['H', 'T']))
        state = die1.die_state()
        self.assertEqual(type(state), pd.DataFrame)


class TestGameMethods(unittest.TestCase):
    def test_Game_initializer(self):
        die1 = Die(np.array(['H', 'T']))
        game1 = Game([die1, die1])
        self.assertEqual(type(game1), Game)

    def test_Game_roll(self):
        die1 = Die(np.array(['H', 'T']))
        game1 = Game([die1, die1])
        game1.play(10)
        self.assertEqual(len(game1._result), 10)

    def test_return_result(self):
        die1 = Die(np.array(['H', 'T']))
        game1 = Game([die1, die1])
        game1.play(10)
        result = game1.return_result(True)
        self.assertEqual(type(result), pd.DataFrame)

class TestAnalyzerMethods(unittest.TestCase):
    def test_Analyzer_initializer(self):
        die1 = Die(np.array(['H', 'T']))
        game1 = Game([die1, die1])
        game1.play(10)
        analysis = Analyzer(game1)
        self.assertEqual(type(analysis), Analyzer)
        
    def test_jackpot(self):
        die1 = Die(np.array(['H', 'T']))
        game1 = Game([die1, die1])
        game1.play(10)
        analysis = Analyzer(game1)
        self.assertEqual(type(analysis.jackpot()), int)
        
    def test_face_counts(self):
        die1 = Die(np.array(['H', 'T']))
        game1 = Game([die1, die1])
        game1.play(10)
        analysis = Analyzer(game1)
        self.assertEqual(type(analysis.face_counts()), pd.DataFrame)

    def test_combo_count(self):
        die1 = Die(np.array(['H', 'T']))
        game1 = Game([die1, die1])
        game1.play(10)
        analysis = Analyzer(game1)
        self.assertEqual(type(analysis.combo_count()), pd.DataFrame)

    def test_permutation_count(self):
        die1 = Die(np.array(['H', 'T']))
        game1 = Game([die1, die1])
        game1.play(10)
        analysis = Analyzer(game1)
        self.assertEqual(type(analysis.permutation_count()), pd.DataFrame)
        
   
if __name__ == '__main__':
    unittest.main(verbosity=2)