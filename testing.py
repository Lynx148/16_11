import chess
import numpy as np
# np.set_printoptions(suppress=True)
import moves
from game import Game, GameState
# import itertools
from chess import Board
import itertools

# a = GameState(Board('rnbqkb1r/1pppp1pp/5p2/p2n4/3P4/1P2BN2/P1P1PPPP/RN1QKB1R w - - 0 5'),0)
# print(a.board)
# print(a.board.status())
# print("###")
# a = GameState(Board('rnbqkb1r/1pppp1pp/5p1B/p2n4/3P4/1P3N2/P1P1PPPP/RN1QKB1R b - - 1 5'),1)
# print(a.board)
# print(a.board.status())
#
# a.board.push_uci("h6c1")
# print("###")
# print(a.board)
# print(a.board.status())

a1 = Board('rnbqkb1r/pppppppp/8/3n4/3P4/1P3N2/P1P1PPPP/RNBQKB1R b - - 0 3')
a2 = Board('rnbqkb1r/1ppppppp/8/p2n4/3P4/1P3N2/P1P1PPPP/RNBQKB1R w - - 0 4')
a3 = Board('rnbqkb1r/1ppppppp/8/p2n4/3P4/1P2BN2/P1P1PPPP/RN1QKB1R b - - 1 4')
a4 = Board('rnbqkb1r/1pppp1pp/5p2/p2n4/3P4/1P2BN2/P1P1PPPP/RN1QKB1R w - - 0 5')
a5 = Board('rnbqkb1r/1pppp1pp/5p1B/p2n4/3P4/1P3N2/P1P1PPPP/RN1QKB1R b - - 1 5')
a6 = Board('rnbqkb1r/1pppp1pp/5p2/p2n4/3P4/1P3N2/P1P1PPPP/RNbQKB1R w - - 0 6')

print(a5.fen())
# a5.push_uci("h8g8")
# print(a5.fen())
# a5.push_uci("a1c4")
# a5.push_uci("h6c1")
# print(a5)
# print(list(a5.legal_moves))
print(a5.epd()[:-6])

# actions = list(a5.legal_moves)
# # ml = moves.movelist
# indexes = [(np.where(moves.movelist == str(action))[0]) for action in actions]
# print(indexes)
# chain = list(itertools.chain.from_iterable(indexes))
# print(chain)
# print(moves.movelist[chain])
# for item in list(a5.legal_moves):
#     print(item)

# for b in a:
#     print(str(b), flush=True)
#     print("\n")


# # b = list(a.board.legal_moves)
# #
# # indexes = [(np.where(moves.movelist == str(action))[0]) for action in b]
# # chain = list(itertools.chain.from_iterable(indexes))
# #
# # for move in chain:
# #     print(move)
# #
# # print(len(chain))
# print(moves.movelist[4031])
# print(moves.movelist[4094])
#

# do sprawdzenia
# 2021-10-03 00:00:52,126 INFO rnb1kbnB/p2ppp1p/1pp5/6q1/1P6/8/P1PPPPPP/RN1QKBNR b - - 0 5
# 2021-10-03 00:00:54,317 INFO action: g5a5
# 2021-10-03 00:00:54,317 INFO MCTS perceived value for BLACK: 0.020000
# 2021-10-03 00:00:54,317 INFO NN perceived value for BLACK: -0.020000
# 2021-10-03 00:00:54,318 INFO ====================
# 2021-10-03 00:00:54,322 INFO rnb1kbnB/p2ppp1p/1pp5/q7/1P6/8/P1PPPPPP/RN1QKBNR w - - 1 6
# 2021-10-03 00:00:56,262 INFO action: a5a4
# 2021-10-03 00:00:56,262 INFO MCTS perceived value for WHITE: -0.140000
# 2021-10-03 00:00:56,262 INFO NN perceived value for WHITE: -0.150000
# 2021-10-03 00:00:56,262 INFO ====================
# 2021-10-03 00:00:56,266 INFO rnb1kbnB/p2ppp1p/1pp5/8/QP6/8/P1PPPPPP/RN1QKBNR b - - 0 6
#
# from random import random
# for i in range(20):
#     done = 0
#     print(i)
#     while done == 0:
#         a = random()
#         if a < 0.4:
#             print("a<0.4")
#             print("##")
#             done = 1
#         elif a > 0.9:
#             print(i)
#             print(a)
#             i = i-1
#             print(i)
#             print("##")
