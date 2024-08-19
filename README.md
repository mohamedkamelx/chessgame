### Running the Game

To run the game, simply execute the Python script:

```bash
python chess_game.py
```

### Chess Pieces and Movements

The game includes all standard chess pieces: King, Queen, Rook, Bishop, Knight, and Pawn. Each piece has its own class that defines its valid moves.

- **Pawn**: Can move forward one or two squares on the first move, captures diagonally.
- **Rook**: Moves any number of squares horizontally or vertically.
- **Knight**: Moves in an L-shape (two squares in one direction and one square perpendicular).
- **Bishop**: Moves diagonally any number of squares.
- **Queen**: Moves any number of squares in any direction.
- **King**: Moves one square in any direction.

### Code Structure

- `ChessPiece`: Base class for all chess pieces. Contains basic attributes like `color`, `position`, and methods like `move` and `valid_moves`.
  it also initiate that the king cant be taken ,so the other pieces inherete that
- `Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, `King`: Derived classes that implement the specific movement logic for each piece.

### Board Representation

The chessboard is represented as an 8x8 grid (a list of lists in Python), where each element can either be `None` (if no piece is present) or an instance of a chess piece class.

### User Interface

The game board is displayed using Pygame, with each piece rendered as an image on the appropriate square. The board alternates between white and gray squares to represent the chess grid.

### Game Logic

- Players take turns moving their pieces.
- A piece can be selected by clicking on it, and if the selected piece has valid moves, clicking on another square will move the piece.
- If a move is invalid, the piece remains in its original position.

### Future Improvements

- Implementing check and checkmate logic.
- Adding single player mode
- Implementing castling, en passant, and pawn promotion.

### Code Example

Here's a snippet of the main game loop:

```python
def main():
    global current_turn
    selected_piece = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // 100, pos[0] // 100
                piece = board[row][col]

                if selected_piece:
                    if move_piece(selected_piece, (row, col)):
                        current_turn = 'black' if current_turn == 'white' else 'white'
                    selected_piece = None
                else:
                    if piece and piece.color == current_turn:
                        selected_piece = piece

        draw_board()
        draw_pieces()
        pygame.display.update()

    pygame.quit()
```

### Screenshots

[![Chess Game](screenshot.png)](https://github.com/mohamedkamelx/chessgame/blob/main/chess/pygame%20window%208_19_2024%2011_10_06%20PM.png)

