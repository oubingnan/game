from functools import reduce
from collections import *


class Line:
    def __init__(self, points):
        self.available = points
        self.occupied = []

    def update(self, point):
        if point in self.available:
            self.available.remove(point)
            self.occupied.append(point)

    def length(self):
        return len(self.occupied)


class Part:
    def __init__(self, lines):
        self.lines = lines

    def go(self, point, opponent):
        for l in self.lines:
            l.update(point)
        if opponent is not None:
            opponent.receive(point)

    def receive(self, point):
        for l in self.lines:
            if point in l.available: self.lines.remove(l)

    def win(self):
        for l in self.lines:
            if len(l.occupied) == 5:
                return True
        return False

    def pointsWithLineLength(self, mininumLineLength):
        temp = list(reduce(lambda x, y: x + y, [z.available for z in self.lines if z.length() >= mininumLineLength], []))
        if len(temp)>0:
            return mininumLineLength, temp
        return self.pointsWithLineLength(mininumLineLength-1)




