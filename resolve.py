from itertools import groupby
from functools import reduce
from collections import *

def mostcommon(points):
    c = Counter(points)
    maxvalue = max(c.values())
    ret = dict([a for a in c.items() if a[1]==maxvalue])
    return ret

def resolveN(myself, opponent, n, start=None):
    mylevel, mypoints =myself.pointsWithLineLength(n)
    yourlevel, yourpoints = opponent.pointsWithLineLength(n)
    if yourlevel>mylevel:
        return mostcommon(yourpoints)
    return mostcommon(mypoints)

    if len(mypoints)>0:
        mycounter = mostcommon(mypoints)
    for ii, jj in mycounter:
        if jj+n>=5:
            return ii
    print('r',mycounter)

    hispoints = getpoints(opponent, n, start)
    hiscounter = Counter(mostcommon(hispoints))
    for ii, jj in hiscounter:
        if jj + n >= 5:
            return ii
    print('r', mycounter)

    if n == 1 or len(r) == 1:
        print('pick 0, 0', n, len(r))
        return r.most_common(1)[0][0]
    print('next')
    return resolveN(myself, opponent, n-1, r.keys())
    '''
    my = myself.points(n) or None
    his = opponent.points(n) or None
    # if togo is not None and len(togo) > 0:
    # temp1 = [(key, len(list(group))) for key, group in groupby(togo)]
    temp1 = Counter(mostcommon(my))
    temp2 = Counter(mostcommon(his))
    return (temp1+temp2).most_common(1)
    #return max(temp1+temp2, key=lambda x:x[1], default=None)
    '''
def resolvePoints(points, myself, opponent):
    if len(points)==1:
        return points[0]


def resolve(myself, opponent):
    return resolveN(myself, opponent, 4, None)
    '''
    togo = myself.pointsWithLineLength(4)
    if togo is not None and len(togo)>0:
        return togo[0]
    
    togo = opponent.pointsWithLineLength(4)
    if togo is not None and len(togo)>0:
        return togo[0]
    togo = resolveN(myself,opponent, 3)
    if togo is not None and len(togo) > 0:
        return togo[0]
    togo = resolveN(myself, opponent, 2)
    if togo is not None and len(togo) > 0:
        return togo[0]
    togo = resolveN(myself, opponent, 1)
    if togo is not None and len(togo) > 0:
        #print('resolve1 return', togo)
        return togo[0]
    '''
    return None
