from collections import *
from functools import reduce


class Line:
    def __init__(self, points):
        self.available = points[:]
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

    def go(self, point):
        for l in self.lines:
            l.update(point)

    def receive(self, point):
        for l in self.lines[:]:
            if point in l.available: self.lines.remove(l)

    def win(self):
        for l in self.lines:
            if len(l.occupied) == 5:
                return True
        return False

    def getWeight(self, point):
        return tuple(map(lambda l: len([x for x in self.lines if x.length()==l and point in x.available]), range(4,0,-1)))
    def getPoint(self):
        points = set(reduce(lambda x, y: x + y, [z.available for z in self.lines], []))
        return max(map(lambda p: (p, self.getWeight(p)), points), key=lambda x:x[1])

    def mostcommon(self, points):
        c = Counter(points)
        maxvalue = max(c.values())
        ret = dict([a for a in c.items() if a[1] == maxvalue])
        return list(ret.keys())

    def getlines(self, point, n):
        return len(list(reduce(lambda x, y: x + y, [z.available for z in self.lines if z.length() >= n and point in z.available], [])))
    def pointsWithLineLength(self, mininumLineLength=4):
        temp = list(reduce(lambda x, y: x + y, [z.available for z in self.lines if z.length() >= mininumLineLength], []))
        if len(temp)==0:
            mininumLineLength -=1
            print('minLength', mininumLineLength)
            return self.pointsWithLineLength(mininumLineLength)
        if len(temp)==1:
            return mininumLineLength, temp[0]
        if len(temp)>1:
            temp = self.mostcommon(temp)
            m = max(temp,key= lambda x: self.getlines(x,mininumLineLength-1))
            return mininumLineLength, m





