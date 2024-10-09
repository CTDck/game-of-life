from game import GameBoard

if __name__ == "__main__":
    game = GameBoard(shape=(10, 20))
    print(f"Game Board Shape {game.board.shape}")
    game.populate_random(100)
    print()
    print(f"Randomly populated Board")
    print(game.board)
    print()