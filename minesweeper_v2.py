import random
import tkinter as tk

num_mines = 10
x_length = 9
y_length = 9

global mines
mines = []

global buttons
buttons = []

main = tk.Tk()
main.title('Minesweeper!')
main.geometry('500x500')

def gen_mines(num_mines):
    global mines
    for a in range(num_mines):
        same = True
        while same == True:
            rand_x = random.randint(0,x_length)
            rand_y = random.randint(0,y_length)
            same = False
            for b in range(len(mines)):
                if mines[b][0] == rand_x:
                    if mines[b][1] == rand_y:
                        same = True
        mines.append([rand_x,rand_y])

def reveal(row,column):
    global mines
    global buttons
    mine_spot = False
    for e in range(len(mines)):
        if column == mines[e][0]:
            if row == mines[e][1]:
                mine_spot = True
    if mine_spot == True:
        main.destroy()
        print("Game over. Try again!")
    else:
        buttons[row][column].configure(state=tk.DISABLED,bg='black')
    

def build_GUI(x_length,y_length):
    global buttons
    for c in range(y_length):
        temp = []
        for d in range(x_length):
            button = tk.Button(main,text='',bg='light grey',command=lambda row=c,column=d: reveal(row,column),width=5,height=3)
            button.grid(column=d,row=c)
            temp.append(button)
        buttons.append(temp)

gen_mines(num_mines)
build_GUI(x_length,y_length)
