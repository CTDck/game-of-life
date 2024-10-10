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

    def evolve(self):
        """Evolve the board 1 iteration
        """
        board_copy = np.zeros(shape=self.board.shape)
        
        for i, row in enumerate(self.board):
            for j, elem in enumerate(row):
                cell_state = elem

                # Set element to 0 to allow summation
                self.board[i, j] = 0

                # Look to the nearest neighbours in a square
                x_lims = (i-1 if i > 0 else 0, i + 2 if i < self.x_size else self.x_size - 2)
                y_lims = (j-1 if j > 0 else 0, j + 2 if j < self.y_size else self.y_size - 2)
                subsection = self.board[x_lims[0]:x_lims[1], y_lims[0]:y_lims[1]]
                
                # Get number of alive cells next to central cell
                cell_count = np.sum(subsection)
                #print(f"{subsection} has sum {cell_count}")
                
                # Cells will only be alive if their neighbour sum is 2 or 3
                if cell_count in [2, 3]: 
                    board_copy[i, j] = 1
                self.board[i, j] = cell_state
        
        # Update board with newest evolution
        self.board = board_copy
                    



