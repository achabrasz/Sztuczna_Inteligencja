from exceptions import AgentException
import random

class AlphaBetaAgent:
    def __init__(self, token, depth=2):
        self.my_token = token
        self.depth = depth

    def alphabeta(self, connect4, depth, alpha=-float('inf'), beta=float('inf'), maximizingPlayer=True):
        if depth == 0 or connect4.game_over:
            return self.evaluate(connect4), None

        if maximizingPlayer:
            bestMove = None
            for move in connect4.possible_drops():
                connect4.drop_token(move)
                eval, _ = self.alphabeta(connect4, depth - 1, alpha, beta, False)
                connect4.undo_move(move)
                if eval is not None and eval > alpha:
                    alpha = eval
                    bestMove = move
                if alpha >= beta:
                    break
            return alpha, bestMove
        else:
            bestMove = None
            for move in connect4.possible_drops():
                connect4.drop_token(move)
                eval, _ = self.alphabeta(connect4, depth - 1, alpha, beta, True)
                connect4.undo_move(move)
                if eval is not None and eval < beta:
                    beta = eval
                    bestMove = move
                if alpha >= beta:
                    break
            return beta, bestMove

    def decide(self, connect4):
        while True:
            n_column = self.alphabeta(connect4, self.depth)[1]
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
