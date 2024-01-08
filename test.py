
import chesspieces as cp
board=cp.makeBoard();
chess = cp.Chess("Wknight",[1,7])
print(cp.WknightValid(chess,board))
print(cp.validmoves(chess,board))