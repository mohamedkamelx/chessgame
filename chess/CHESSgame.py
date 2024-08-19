import pygame

pygame.init()


WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)


class ChessPiece:
    def __init__(self, color, position):
        self.color = color
        self.position = position 
        self.image = None

    def move(self, new_position):
        self.position = new_position

    def valid_moves(self, board,potential_moves):
        filtered_moves = []
        for move in potential_moves:
            target_piece = board[move[0]][move[1]]
            # Filter out moves that land on the opponent's king
            if not isinstance(target_piece, King) or target_piece.color == self.color:
                filtered_moves.append(move)
        return filtered_moves
        




class Pawn(ChessPiece):
    first_move = 0

    def __init__(self, color, position):
        
        super().__init__(color, position)
        self.image = pygame.image.load(f"{'wP' if color == 'white' else 'bP'}.png")

    def valid_moves(self, board):
        moves = []

        if self.color == 'white':
            directions = [(1, 0)]
            special_directions = [(1, 1), (1, -1)]
            if self.first_move == 0:
                first_move = (self.position[0] + 2, self.position[1])
        else:
            directions = [(-1, 0)]
            special_directions = [(-1, 1), (-1, -1)]
            if self.first_move == 0:
                first_move = (self.position[0] - 2, self.position[1])

        # Forward move
        for direction in directions:
            new_row = self.position[0] + direction[0]
            new_col = self.position[1] + direction[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = board[new_row][new_col]
                if target_piece is None:
                    moves.append((new_row, new_col))
        
        # Two-square move on first move
        if self.first_move == 0:
            if 0 <= first_move[0] < 8 and board[first_move[0]][first_move[1]] is None:
                moves.append(first_move)

        # Diagonal capture moves
        for direction in special_directions:
            new_row = self.position[0] + direction[0]
            new_col = self.position[1] + direction[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = board[new_row][new_col]
                if target_piece and target_piece.color != self.color:
                    moves.append((new_row, new_col))

        return super().valid_moves(board, moves)


class Rook(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.image = pygame.image.load(f"{'wR' if color == 'white' else 'bR'}.png")

    def valid_moves(self, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Horizontal and vertical

        for direction in directions:
            row, col = self.position
            while True:
                row += direction[0]
                col += direction[1]
                if 0 <= row < 8 and 0 <= col < 8:
                    if board[row][col] is None:
                        moves.append((row, col))
                    elif board[row][col].color != self.color:
                        moves.append((row, col))
                        break
                    else:
                        break
                else:
                    break

        return super().valid_moves(board, moves)
    

class King(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.image = pygame.image.load(f"{'wK' if color == 'white' else 'bK'}.png")

    def valid_moves(self, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # All possible directions

        for direction in directions:
            new_row = self.position[0] + direction[0]
            new_col = self.position[1] + direction[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = board[new_row][new_col]
                if target_piece is None or target_piece.color != self.color:
                    moves.append((new_row, new_col))

        return super().valid_moves(board, moves)
    

class Knight(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.image = pygame.image.load(f"{'wN' if color == 'white' else 'bN'}.png")

    def valid_moves(self, board):
        moves = []
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),  # L-shaped moves (vertical first)
            (1, 2), (1, -2), (-1, 2), (-1, -2)   # L-shaped moves (horizontal first)
        ]

        for move in knight_moves:
            new_row = self.position[0] + move[0]
            new_col = self.position[1] + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = board[new_row][new_col]
                if target_piece is None or target_piece.color != self.color:
                    moves.append((new_row, new_col))

        return super().valid_moves(board, moves)


class Queen(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.image = pygame.image.load(f"{'wQ' if color == 'white' else 'bQ'}.png")

    def valid_moves(self, board):
        moves = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),   # Horizontal and vertical
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonal
        ]

        for direction in directions:
            new_row, new_col = self.position

            while True:
                new_row += direction[0]
                new_col += direction[1]

                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target_piece = board[new_row][new_col]
                    if target_piece is None:
                        moves.append((new_row, new_col))
                    elif target_piece.color != self.color:
                        moves.append((new_row, new_col))
                        break
                    else:
                        break
                else:
                    break

        return super().valid_moves(board, moves)
    

class Bishop(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.image = pygame.image.load(f"{'wB' if color == 'white' else 'bB'}.png")

    def valid_moves(self, board):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # All possible diagonal directions

        for direction in directions:
            new_row, new_col = self.position

            while True:
                new_row += direction[0]
                new_col += direction[1]

                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target_piece = board[new_row][new_col]
                    if target_piece is None:
                        moves.append((new_row, new_col))
                    elif target_piece.color != self.color:
                        moves.append((new_row, new_col))
                        break
                    else:
                        break
                else:
                    break

        return super().valid_moves(board, moves)



board = [[None for _ in range(8)] for _ in range(8)]


board[0][0] = Rook('white', (0, 0))
board[0][1] = Knight('white', (0, 1))
board[0][2] = Bishop('white', (0, 2))
board[0][3] = Queen('white', (0, 3))
board[0][4] = King('white', (0, 4))
board[0][5] = Bishop('white', (0, 5))
board[0][6] = Knight('white', (0, 6))
board[0][7] = Rook('white', (0, 7))
board[1] = [Pawn('white', (1, i)) for i in range(8)]

board[7][0] = Rook('black', (7, 0))
board[7][1] = Knight('black', (7, 1))
board[7][2] = Bishop('black', (7, 2))
board[7][3] = Queen('black', (7, 3))
board[7][4] = King('black', (7, 4))
board[7][5] = Bishop('black', (7, 5))
board[7][6] = Knight('black', (7, 6))
board[7][7] = Rook('black', (7, 7))
board[6] = [Pawn('black', (6, i)) for i in range(8)]


current_turn = 'white'

def draw_board():#only draws the grid of the board
    WINDOW.fill(GRAY)
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else GRAY
            pygame.draw.rect(WINDOW, color, (col * 100, row * 100, 100, 100))

def draw_pieces(): #puts pieces on board according to thier index block
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                img = pygame.transform.scale(piece.image, (100, 100))
                WINDOW.blit(img, (col * 100, row * 100))


def move_piece(piece, new_position):
    print(type(piece))
    if new_position in piece.valid_moves(board):
        board[piece.position[0]][piece.position[1]] = None
        piece.move(new_position)
        board[new_position[0]][new_position[1]] = piece
        if Pawn.__instancecheck__(piece):piece.first_move+=1
        return True
    return False


def main():
    global current_turn
    selected_piece = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos() #returns the coordenates of the mouse click as tuple (x,y)
                row, col = pos[1] // 100, pos[0] // 100  #the square block index
                piece = board[row][col] #None if there is no piece on the clicked block and a piece object if theres a piece on

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

if __name__ == "__main__":
    main()
