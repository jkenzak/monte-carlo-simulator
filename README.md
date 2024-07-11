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

