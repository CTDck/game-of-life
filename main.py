from game import GameBoard
import matplotlib.pyplot as plt
import numpy as np
import time

if __name__ == "__main__":
    game1 = GameBoard(shape=(100, 50))
    print(f"Game Board Shape {game1.board.shape}")
    game1.populate_random(2000)

    game2 = GameBoard(shape=(100, 50))
    print(f"Game Board Shape {game2.board.shape}")
    game2.populate_random(2000)
    
    plt.ion()
    fig, axs = plt.subplots(2, 2)
    image1 = axs[0][0].imshow(game1.board, aspect="auto", cmap="Greys", vmax=1, vmin=0, interpolation="none")
    image2 = axs[0][1].imshow(game2.board, aspect="auto", cmap="Greys", vmax=1, vmin=0, interpolation="none")
    dummy_x, dummy_y = (np.arange(0, 1000, 1), np.zeros(1000))
    line1, line2, = axs[1][0].plot(dummy_x, dummy_y, "b", dummy_x, dummy_y, "r")
    axs[1][0].set_ylim(0, 1000)

    i = 0
    while i < 1000:
        game1.evolve()
        game2.evolve()
        image1.set_array(game1.board)
        image2.set_array(game2.board)
        line1.set_ydata(np.concatenate([np.asarray(game1.population), np.zeros(998-i)]))
        line2.set_ydata(np.concatenate([np.asarray(game2.population), np.zeros(998-i)]))
        fig.canvas.draw()
        fig.canvas.flush_events()
        i += 1
    plt.close()

