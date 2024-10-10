from game import GameBoard
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
import time

if __name__ == "__main__":
    game1 = GameBoard(shape=(50, 50))
    print(f"Game Board Shape {game1.board.shape}")
    game1.populate_random(1000)

    game2 = GameBoard(shape=(50, 50))
    print(f"Game Board Shape {game2.board.shape}")
    game2.populate_random(1000)
    
    plt.ion()

    fig = plt.figure()
    grid = GridSpec(2, 2, figure=fig)

    axs1 = fig.add_subplot(grid[0,0])
    axs2 = fig.add_subplot(grid[0,1])
    image1 = axs1.imshow(game1.board, aspect="auto", cmap="Greys", vmax=1, vmin=0, interpolation="none")
    image2 = axs2.imshow(game2.board, aspect="auto", cmap="Greys", vmax=1, vmin=0, interpolation="none")
    dummy_x, dummy_y = (np.arange(0, 1000, 1), np.zeros(1000))
    axs3 = fig.add_subplot(grid[1, :])
    line1, = axs3.plot(dummy_x, dummy_y, "b", label="pop1")
    line2, = axs3.plot(dummy_x, dummy_y, "r", label="pop2")
    axs3.set_ylim(0, 2000)

    axs3.legend()

    i = 0
    while i < 1000:
        game1.evolve()
        game2.evolve()
        image1.set_array(game1.board)
        image2.set_array(game2.board)
        line1.set_ydata(np.concatenate([np.asarray(game1.population), np.zeros(1000-i-2)]))

        line2.set_ydata(np.concatenate([np.asarray(game2.population), np.zeros(1000-i-2)]))
        fig.canvas.draw()
        fig.canvas.flush_events()
        axs3.set_xlim(0, i+1)
        i += 1
    plt.close()

