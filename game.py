from resolve import *
from part import *


def getinput():
    return tuple(map(int, input('Black''s Turn-->').split(',')))


class Game:
    dimension = 15
    board = [(x, y) for x in range(15) for y in range(15)]
    line1 = [[(x + i, y) for i in range(5) if x + i < 15] for x in range(15) for y in range(15)]
    line3 = [[(x, y + i) for i in range(5) if y + i < 15] for x in range(15) for y in range(15)]
    line2 = [[(x + i, y + i) for i in range(5) if x + i < 15 and y + i < 15] for x in range(15) for y in range(15)]
    line4 = [[(x - i, y + i) for i in range(5) if x - i >= 0 and y + i < 15] for x in range(15) for y in range(15)]
    blackmove = []
    whitemove = []
    blacklines = [Line(x) for x in line1 + line2 + line3 + line4 if len(x) == 5]
    whitelines = [Line(x) for x in line1 + line2 + line3 + line4 if len(x) == 5]
    black = Part(blacklines)
    white = Part(whitelines)

    def invalidmove(self, point):
        return point in self.blackmove + self.whitemove or point not in self.board

    def accept(self, move):
        self.black.go(move, self.white)
        self.blackmove.append(move)
    def response(self):
        togo = resolve(self.white, self.black)
        self.white.go(togo, self.black)
        self.whitemove.append(togo)
        return togo
    '''    
    while not black.win() and not white.win():
        print("Black moves: ", blackmove)
        print("White moves: ", whitemove)
        move = getinput()
        if invalidmove(move):
            print("Invalid move: Black", move)
            continue
        black.go(move, white)
        blackmove.append(move)
        if black.win():
            print('Black Win')
            exit()
        # white turn
        togo = resolve(white, black)
        white.go(togo, black)
        whitemove.append(togo)
        print('White goes ', togo)
        if white.win():
            print('White Win')
            exit()
'''