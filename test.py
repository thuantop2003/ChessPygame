
import chesspieces as cp
board=cp.makeBoard();
chess = cp.Chess("Wpawn",[2,4])
print(chess.name=="Wpawn")
print(chess.location==[2,5])
print(cp.validmoves(chess,board))