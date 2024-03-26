from exceptions import AgentException
import random

class MinMaxAgent:
    def __init__(self, token, depth=2):
        self.my_token = token
        self.depth = depth

    def minimax(self, connect4, depth, maximizingPlayer=True):
        if depth == 0 or connect4.game_over:
            return self.evaluate(connect4), None

        if maximizingPlayer:
            maxEval = -float('inf')
            bestMove = None
            for move in connect4.possible_drops():
                connect4.drop_token(move)
                eval, _ = self.minimax(connect4, depth - 1, False)
                connect4.undo_move(move)
                if eval > maxEval:
                    maxEval = eval
                    bestMove = move
            return maxEval, bestMove
        else:
            minEval = float('inf')
            bestMove = None
            for move in connect4.possible_drops():
                connect4.drop_token(move)
                eval, _ = self.minimax(connect4, depth - 1, True)
                connect4.undo_move(move)
                if eval < minEval:
                    minEval = eval
                    bestMove = move
            return minEval, bestMove

    def decide(self, connect4):
        while True:
            n_column = self.minimax(connect4, self.depth)[1]
            if n_column in connect4.possible_drops():
                return n_column
            else:
                return random.choice(connect4.possible_drops())

    def evaluate(self, connect4):
        if connect4.game_over:
            if connect4.wins == self.my_token:
                return float('inf')
            elif connect4.wins is not None:
                return -float('inf')
            else:
                bestValue = -float('inf')
                for col in range (connect4.width, 0, -1):
                    count = 0
                    for row in range (connect4.height, 0, -1):
                        if connect4.board[row][col] == self.my_token:
                            count += 2
                        elif connect4.board[row][col] == '_':
                            count += 1
                        else:
                            count = 0
                    if count > bestValue:
                        bestValue = count
                for row in range (connect4.height, 0, -1):
                    count = 0
                    for col in range (connect4.width, 0, -1):
                        if connect4.board[row][col] == self.my_token:
                            count += 2
                        elif connect4.board[row][col] == '_':
                            count += 1
                        else:
                            count = 0
                    if count > bestValue:
                        bestValue = count
                for row in range (connect4.height, 0, -1):
                    for col in range (connect4.width, 0, -1):
                        count = 0
                        for i in range (4):
                            if row - i >= 0 and col - i >= 0:
                                if connect4.board[row - i][col - i] == self.my_token:
                                    count += 2
                                elif connect4.board[row - i][col - i] == '_':
                                    count += 1
                                else:
                                    count = 0
                        if count > bestValue:
                            bestValue = count
                for row in range (connect4.height, 0, -1):
                    for col in range (connect4.width, 0, -1):
                        count = 0
                        for i in range (4):
                            if row - i >= 0 and col + i < connect4.width:
                                if connect4.board[row - i][col + i] == self.my_token:
                                    count += 2
                                elif connect4.board[row - i][col + i] == '_':
                                    count += 1
                                else:
                                    count = 0
                        if count > bestValue:
                            bestValue = count
                return bestValue
        else:
            return 0
