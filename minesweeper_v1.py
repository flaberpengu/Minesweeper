import random
import tkinter as tk

num_mines = 10
x_length = 9
y_length = 9

mines = []

main = tk.Tk()
main.title('Minesweeper!')
main.geometry('500x500')


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

def build_GUI(x_length,y_length,mines):
    for c in range(y_length):
        for d in range(x_length):
            button = tk.Button(main,text='',command=reveal,bg='light grey')
            button.pack(side=tk.LEFT,row=c)

build_GUI(x_length,y_length,mines)
