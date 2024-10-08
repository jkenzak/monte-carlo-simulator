# Monte Carlo Simulator - Jack Kenzakowski

## Synopsis

Upon downloading this repo, you can install the montecarlo module by running the following command in this directory:

```bash
pip install .
```

Once that is installed, you will be able to import it into your python files

```python
import montecarlo.montecarlo
```
This module also utilizes numpy and pandas

```python
import numpy as np
import pandas as pd
```

This will allow you to instantiate the subsequent classes of Die, Game, and Analyzer in order to implement this simulator. Here is an example if you wanted to flip two fair coins multiple times and analyze the results:

```python
fair_coin = montecarlo.montecarlo.Die(np.array('H', 'T'))
coin_game = montecarlo.montecarlo.Game([fair_coin, fair_coin])
coin_game.play(n = 5) # 5 coin flips each

coin_analyzer = montecarlo.montecarlo.Analyzer(coin_game)
```

From here, you would be able to call the return_result() function under the game class to return the results of the flips in either narrow or wide form. Along with that, you would be able to get the various statistics computed using the Analyzer functions. These available functions will be described more in detail below.

## API Description

### Die class

#### `Die(faces)`

Takes in a NumPy array of distinct values, `faces`, that would serve as the representation of each side of the 'die' object. Initializes the Die with each side having an equal weight of 1

#### `Die.change_weight(face, new_weight)`

Takes in `face`, which is the face of the side that you want to change the weight of and then `new_weight` is the weight value that would replace the new one. This must be a numeric value or a numeric string. It changes the value within the Die instance and doesn't return anything

#### `Die.roll_die(n=1)`

Rolls the die one or more times in accordance with the corresponding weights. `n` must be a positive int and if no arguments are passed it defaults to 1. It will output a list of length `n` that shows the faces that each roll landed on

#### `Die.die_state()`

Shows the current Die's attributes by returning a pandas DataFrame that shows each die face and their corresponding weights

### Game class

#### `Game(dice)`

Creates a collection of dice that are intended to be rolled simultaneously. It takes in a list of Die objects, `dice`

#### `Game.play(n)`

Rolls the dice `n` times using the Die.roll_die() method and stores the results in a private dataframe

#### `Game.return_result(wide=True)`

Returns a pandas DataFrame of the roll results for each roll number and die number. Takes in a boolean, `wide`, that indicates whether the resulting DataFrame will be output in narrow or wide format

### Analyzer class

#### `Analyzer(game)`

Takes in a Game object, `game`, that has already had the play method called in order to compute properties and statistics of that game

#### `Analyzer.jackpot()`

Calculates the number of instances where all faces are the same in a single roll, returning an integer value >= 0

#### `Analyzer.face_counts()`

Counts the number of times each face is rolled on for each singular roll, returns a pandas DataFrame containing each face value for every roll

#### `Analyzer.combo_count()`

Calculates the distinct combinations of faces rolled, regardless of the die ordering. Returns a pandas DataFrame of all the combinations and their counts

#### `Analyzer.permutation_count()`

Similar to the combo_count() method but with the combinations being dependent on the ordering of the die. Returns a pandas DataFrame of all the permutations and their counts
