import tkinter as tk
import itertools as IT
import collections

cols, rows =  15 , 15
board = [[None] * cols for _ in range(rows)]    
other = {'green': 'red', 'red': 'green'}

player = 'red'   

def on_click(event, i, j):
    global player
    board[i][j]['bg'] = player
    for ii, jj in IT.product(range(i - 1, i + 2), range(j - 1, j + 2)):
        if ii<0 or ii>=rows or jj<0 or jj>=cols: continue
        neighbor = board[ii][jj]
        if neighbor['bg'] != 'grey' and (ii, jj) != (i, j):
            neighbor['bg'] = other[neighbor['bg']]
    check_for_winner()
    player = other[player]

def check_for_winner():
    s = score()
    if s['red'] + s['green'] == cols*rows:
        # every box filled
        winner = max(s, key=s.get)
        print('Winner is: {}'.format(winner))
        root.after(1, flash_winner, winner, 'blue')

def score():
    return collections.Counter(
        board[i][j]['bg'] for i, j in IT.product(range(rows), range(cols)))

def flash_winner(winner, altcolor):
    for i, j in IT.product(range(rows), range(cols)):
        if board[i][j]['bg'] == winner:
            board[i][j]['bg'] = altcolor
    root.after(250, flash_winner, altcolor, winner)
def select(e,i,j):
    board[i][j]['bg'] = player
root = tk.Tk()
for i, j in IT.product(range(rows), range(cols)):
    board[i][j] = L = tk.Label(root, text='   ', bg='grey')
    L.grid(row=i, column=j, padx=3, pady=3)
    L.bind('<Button-1>', lambda e, i=i, j=j: select(e, i, j))

root.mainloop()
