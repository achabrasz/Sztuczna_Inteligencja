from exceptions import AgentException
import random

class AlphaBetaAgent:
    def __init__(self, token, depth=2):
        self.my_token = token
        self.enemy_token = 'o' if token == 'x' else 'x'
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
                return 160
            elif connect4.wins is not None:
                return -160
        else:
            bestValue = 0
            for four in connect4.iter_fours():
                count_mine = 0
                count_enemy = 0
                count_empty = 0
                for token in four:
                    if token == self.my_token:
                        count_mine += 1
                    elif token == '_':
                        count_empty += 1
                    else:
                        count_enemy += 1
                    bestValue += count_mine - count_enemy
                    if four[0] == self.enemy_token:
                        bestValue -= 1
                    if four[0] == self.my_token:
                        bestValue += 1
                    if four[3] == self.enemy_token:
                        bestValue -= 1
                    if four[3] == self.my_token:
                        bestValue += 1
            if len(list(connect4.iter_fours())) == 0:
                return bestValue
            return bestValue / len(list(connect4.iter_fours()))
