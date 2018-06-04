import random
import time
class TicTacToe:

    def __init__(self, size=3):
        self.size = size
        self.game_pieces = ["O","X"]
        self.blank = " "
        self.human = "X"
        self.robot = "O"
        self.turn  = 1
        self.depth = 0
        self.max_depth = 15 # TODO: Change for various board sizes
        self.grid  = [[self.blank for i in range(self.size)] for j in range(self.size)]

    def play_game(self):
        print("Play tic-tac-toe. Enter your choice as row,col, 0-indexed.")
        print("The top row is 0, the leftmost column is 0.\n\n")

        


        gameover, winner = self.is_gameover()

        while not gameover:
            self.print_board()
            print()

            move = input("Enter a a valid move: ")

            print()
            if not self.valid_move(move):
                print("Not a valid move. Try again.")
                continue

            self.print_board()
            print()
            gameover, winner = self.is_gameover()

            if gameover:
                break

            print()
            print("Here in the computer's move: ")
            print()

            self.minimax()

            gameover, winner = self.is_gameover()

        if winner == self.human:
            print("You Win!")
        elif winner == self.robot:
            print("You Lose!")
        else:
            print("It's a tie!")

    def minimax(self):
        board = self.copy_board()

        possible_moves = self.all_valid_moves(board)
        random.shuffle(possible_moves)
        best_move = possible_moves[0]
        best_val  = -1

        for move in possible_moves:
            copy = self.copy_board(board)
            copy[move[0]][move[1]] = self.robot

            value = self.min_player(copy,1)

            if value == 1: # Might as well stop and save time
                return move

            if best_val < value:
                best_move = move
                best_val  = value
        
        self.grid[best_move[0]][best_move[1]] = self.robot

    def min_player(self,board,depth):
        gameover, winner = self.is_gameover(board)

        if gameover:
            if winner == self.human:
                return -1
            return int(winner == self.robot)

        if depth >= self.max_depth:
            return 0 # TODO: Board eval

        possible_moves = self.all_valid_moves(board)
        random.shuffle(possible_moves)
        best_val = 1

        for move in possible_moves:
            copy = self.copy_board(board)
            copy[move[0]][move[1]] = self.human

            value = self.max_player(copy, depth+1)

            if value == -1:
                return -1

            if best_val > value:
                best_val = value
        return best_val

    def max_player(self,board,depth):
        gameover, winner = self.is_gameover(board)

        if gameover:
            if winner == self.human:
                return -1
            return int(winner == self.robot)

        if depth >= self.max_depth:
            return 0 # TODO: Board eval

        possible_moves = self.all_valid_moves(board)
        random.shuffle(possible_moves)
        best_val = -1

        for move in possible_moves:
            copy = self.copy_board(board)
            copy[move[0]][move[1]] = self.robot

            value = self.min_player(copy, depth+1)

            if value == 1:
                return 1

            if best_val < value:
                best_val = value

        return best_val





    def print_board(self, grid=None):
        temp = self.copy_board(grid)

        for i in range(len(temp)):
            print("{}|{}|{}".format(*temp[i]))
            if i != len(temp) -1:
                print("-"*5)

    def copy_board(self,grid=None):

        if grid == None:
            temp = [[col for col in row] for row in self.grid]
        else:
            temp = [[col for col in row] for row in grid]

        return temp

    def is_gameover(self, grid=None):
        board = self.copy_board(grid)

        for player in self.game_pieces:
            for row in board:
                if all([x==player for x in row]):
                    return True, player
            for col in self.get_columns(board):
                if all([x==player for x in col]):
                    return True, player

            for diag in self.get_diagonals(board):
                if all([x==player for x in diag]):
                    return True, player

        for row in board:
            if any([x==self.blank for x in row]):
                return False, None

        return True, None

    def get_columns(self, grid=None):
        board = self.copy_board(grid)

        if True:
            return [[board[col][row] for col in range(self.size)] for row in range(self.size)]

        columns = [[None for i in range(self.size)] for j in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):

                columns[row][col] = board[col][row]
        return columns

    def get_diagonals(self,grid=None):
        board = self.copy_board(grid)

        diags = []
        diags.append([board[i][i] for i in range(self.size)])
        diags.append([board[self.size-i-1][i] for i in range(self.size)])
        return diags

    def valid_move(self, s):
        try:
            row,col = [int(val.strip()) for val in s.split(",")[:2]]
            if 0 <= row < self.size and 0<= col < self.size:
                if self.grid[row][col] == self.blank:
                    self.grid[row][col] = self.human
                    return True
            return False
        except:
            return False

    def all_valid_moves(self,grid=None):
        board = self.copy_board(grid)

        valid = []

        for row in range(self.size):
            for col in range(self.size):
                if board[row][col] == self.blank:
                    valid.append((row,col))
        return valid

if __name__ == "__main__":
    TicTacToe().play_game()