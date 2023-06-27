# Wave function collapse

This is a graphical implementation of wave function collapse described in quantum 
mechanics. Inspiration taken from this repository 
https://github.com/mxgmn/WaveFunctionCollapse

> In quantum mechanics, wave function collapse occurs when a wave function—initially in a superposition of several eigenstates—reduces to a single eigenstate due to interaction with the external world. This interaction is called an observation, and is the essence of a measurement in quantum mechanics, which connects the wave function with classical observables such as position and momentum. 
> 
> - https://en.wikipedia.org/wiki/Wave_function_collapse

Within this implementation each cell in the grid starts in a super position of all the 
possible states that it could be.

The cell with the lowest entropy is chosen to be collapsed into one of its possible 
states at random. Entropy is described as the number
of possible states the cell could be in. If there is a draw between the cells one of
the cells that drew is chosen at random.

Each cell is required to be able to connect to its neighbours, so on collapsing a cell
the possible states the neighbours needs to be reduced to a valid subset. 


Disclaimer: Interaction not via observation, see Schrodinger's cat.

**Requires:**
* Python3 
* Pillow
* (optionally) pyenv


To run:

`PYTHONPATH=src python src/wfc/main.py`