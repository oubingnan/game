import tkinter as tk
from itertools import product
from tkinter import messagebox

from game import Game

'''
if __name__ == "__main__":
    root = tk.Tk()
    board = gameboard.GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    player1 = tk.PhotoImage(data=gameboard.imagedata)
    #board.addpiece("player1", player1, 0,0)
    root.mainloop()

'''


cols, rows=15,15
board= [[None]* cols for _ in range(rows)]
other= {'green': 'red',   'red':       'green'}

player ='red'
game = Game()

def play(e, i, j):
    global player
    global game
    if (game.invalidmove((i,j))):
        tk.messagebox.showinfo('Invalid Move', 'Invalid Move '+str((i, j)))
    else:

        board[i][j]['bg'] = player
        game.accept((i,j))
        if (game.black.win()):
            tk.messagebox.showinfo('Information', player+' win')
            exit()
        player = other[player]
        togo = game.response()
        board[togo[0]][togo[1]]['bg'] = player
        if (game.white.win()):
            tk.messagebox.showinfo('Information', player+' win')
            exit()
        player = other[player]
        tk.messagebox.showinfo('Information', 'Now it is ' + player + '\'s turn')
root = tk.Tk()

for i, j in product(range(rows),range(cols)):
    board[i][j] = L  = tk.Label(root, text='  ',  bg = 'grey')
    L.grid(row=i, column=j,padx=3, pady=3)
    L.bind('<Button-1>',lambda e,i=i, j=j: play(e, i, j))
root.mainloop()



