class Chess:
    def __init__(self,name,location):
        self.name=name
        self.location=location
def makeBoard():
    board=[]
    for i in range(1,9):
        a= Chess("Wpawn",[2,i])
        b= Chess("Bpawn",[7,i])
        board.append(a)
        board.append(b)
    board.append(Chess("Wbishop",[1,3]))
    board.append(Chess("Wbishop",[1,6]))
    board.append(Chess("Wknight",[1,2]))
    board.append(Chess("Wknight",[1,7]))
    board.append(Chess("Wrook",[1,1]))
    board.append(Chess("Wrook",[1,8]))
    board.append(Chess("WKing",[1,5]))
    board.append(Chess("WQueen",[1,4]))
    board.append(Chess("Bbishop",[8,3]))
    board.append(Chess("Bbishop",[8,6]))
    board.append(Chess("Bknight",[8,2]))
    board.append(Chess("Bknight",[8,7]))
    board.append(Chess("Brook",[8,1]))
    board.append(Chess("Brook",[8,8]))
    board.append(Chess("BKing",[8,5]))
    board.append(Chess("BQueen",[8,4]))
    return board
def loadimage(chess,pg,screen):
    chessimage=pg.image.load(r"image/"+chess.name+".png")
    if(chess.name=="Bpawn"or chess.name=="Wpawn"):
        chessimage=pg.transform.scale(chessimage,(65,65))
        screen.blit(chessimage,((chess.location[0]-1)*100+20,(chess.location[1]-1)*100+20))
    else:
        chessimage=pg.transform.scale(chessimage,(80,80))
        screen.blit(chessimage,((chess.location[0]-1)*100+10,(chess.location[1]-1)*100+10))
def validmoves (chess,board):
    validmove=[]
    if(chess.name=="Wpawn"):
        k1=0
        check1=[chess.location[0]+1,chess.location[1]]
        for chessb in board:
            if(check1==chessb.location):
                k1=1
                break
        if(k1==0):
            validmove.append(check1)
        print(k1)
        check2=[chess.location[0]+2,chess.location[1]]
        k2=1
        if(chess.location[0]==2):
            k2=0
            for chessb in board:
                if(check2==chessb.location):
                    k2=1
                    break
        if(k2==0):
            validmove.append(check2)

        check3=[chess.location[0]+1,chess.location[1]+1]
        check4=[chess.location[0]+1,chess.location[1]-1]
        for chessb in board:
                if check3==chessb.location and chessb.name[0]=="B":
                    validmove.append(check3)
                    break
                if check4==chessb.location and chessb.name[0]=="B":
                    validmove.append(check4)
                    break
    if(chess.name=="Bpawn"):
        k1=0
        check1=[chess.location[0]-1,chess.location[1]]
        for chessb in board:
            if(check1==chessb.location):
                k1=1
                break
        if(k1==0):
            validmove.append(check1)
        print(k1)
        check2=[chess.location[0]-2,chess.location[1]]
        k2=1
        if(chess.location[0]==7):
            k2=0
            for chessb in board:
                if(check2==chessb.location):
                    k2=1
                    break
        if(k2==0):
            validmove.append(check2)
        check3=[chess.location[0]-1,chess.location[1]+1]
        check4=[chess.location[0]-1,chess.location[1]-1]
        for chessb in board:
                if check3==chessb.location and chessb.name[0]=="W":
                    validmove.append(check3)
                    break
                if check4==chessb.location and chessb.name[0]=="W":
                    validmove.append(check4)
                    break
    return validmove       

