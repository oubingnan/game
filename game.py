from part import *


def getinput():
    return tuple(map(int, input('Black''s Turn-->').split(',')))


class Game:
    def __init__(self):
        self.dimension = 15
        self.board = [(x, y) for x in range(15) for y in range(15)]
        line1 = [[(x + i, y) for i in range(5) if x + i < 15] for x in range(15) for y in range(15)]
        line3 = [[(x, y + i) for i in range(5) if y + i < 15] for x in range(15) for y in range(15)]
        line2 = [[(x + i, y + i) for i in range(5) if x + i < 15 and y + i < 15] for x in range(15) for y in range(15)]
        line4 = [[(x - i, y + i) for i in range(5) if x - i >= 0 and y + i < 15] for x in range(15) for y in range(15)]
        self.blackmove = []
        self.whitemove = []
        self.blacklines = [Line(x) for x in line1 + line2 + line3 + line4 if len(x) == 5]
        self.whitelines = [Line(x) for x in line1 + line2 + line3 + line4 if len(x) == 5]
        self.black = Part(self.blacklines)
        self.white = Part(self.whitelines)

    def invalidmove(self, point):
        return point in self.blackmove + self.whitemove or point not in self.board

    def accept(self, move):
        self.black.go(move)
        self.blackmove.append(move)
        self.white.receive(move)
    def response(self):
        #togo = resolve(self.white, self.black)
        w  =self.white.getPoint()
        b = self.black.getPoint()
        togo = max(w,b,key=lambda x:x[1])[0]
        self.white.go(togo[0])
        self.whitemove.append(togo)
        self.black.receive(togo)
        return togo
