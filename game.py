"""Board for the game of life"""


import numpy as np
import matplotlib.pyplot as plt

class GameBoard():
    """GameBoard is a class which is used to generate the playing field, 
    randomly or custom populate the playing field and evolves the playing 
    field by 1 iteration
    """
    def __init__(self, shape):
        """Initialise the Game board 

        Args:
            shape (tuple[int]): Set the size of the game board (X, Y)
        """
        self.x_size, self.y_size = shape
        self.board = np.zeros(shape=shape)
        pass

    def populate_random(self, n_cells):
        """Randomly populate the custom grid with alive cells

        Args:
            n_cells (int): Number of alive cells to place in the empty playing field
        """     
        coords = np.random.randint(low=[[0], [0]], high=[[self.x_size], [self.y_size]], size=(2, n_cells))
        self.board[coords[0], coords[1]] = 1
        pass



