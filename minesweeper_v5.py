import random
import tkinter as tk

##Change grid size and number of mines
num_mines = 10
global x_length
x_length = 9
global y_length
y_length = 9

##Global variables
global mines
mines = []

global buttons
buttons = []

global checked
checked = []

def get_size(x_length,y_length):
    xmax = x_length*100
    ymax = y_length*100
    size_string = str(xmax) + 'x' + str(ymax)
    return size_string

##Initialises Tkinter
size_string = get_size(x_length,y_length)
main = tk.Tk()
main.title('Minesweeper!')
main.geometry(size_string)

##Generates mines
def gen_mines(num_mines):
    global mines
    for a in range(num_mines):
        same = True
        while same == True:
            rand_x = random.randint(0,x_length-1)
            rand_y = random.randint(0,y_length-1)
            same = False
            for b in range(len(mines)):
                if mines[b][0] == rand_x:
                    if mines[b][1] == rand_y:
                        same = True
        mines.append([rand_x,rand_y])
    print(mines)

##Gets all nearby spaces
def get_nearby_spaces(row,column):
    spaces = []
    tl = [column-1,row-1]
    spaces.append(tl)
    tm = [column,row-1]
    spaces.append(tm)
    tr = [column+1,row-1]
    spaces.append(tr)
    ml = [column-1,row]
    spaces.append(ml)
    mr = [column+1,row]
    spaces.append(mr)
    bl = [column-1,row+1]
    spaces.append(bl)
    bm = [column,row+1]
    spaces.append(bm)
    br = [column+1,row+1]
    spaces.append(br)
    return spaces

##Gets number of nearby mines
def get_nearby(row,column):
    global mines
    spaces = get_nearby_spaces(row,column)
    number = 0
    for f in range(len(spaces)):
        for g in range(len(mines)):
            if spaces[f][0] == mines[g][0]:
                if spaces[f][1] == mines[g][1]:
                    number += 1
    return number

def check_space(row,column):
    global checked
    global buttons
    global x_length
    global y_length
    spaces = get_nearby_spaces(row,column)
    zeroes = []
    for i in range(len(spaces)):
        number_mines = get_nearby(spaces[i][1],spaces[i][0])
        if number_mines == 0:
            print('y1')
            print(checked)
            print(spaces[i][0])
            print(spaces[i][1])
            if [spaces[i][0],spaces[i][1]] not in checked:
                temp = False
            else:
                temp = True
            print(temp)
            if (spaces[i][1] < y_length) and (spaces[i][1] >= 0) and (spaces[i][0] >= 0)  and (spaces[i][0] < x_length) and ([spaces[i][0],spaces[i][1]] not in checked):
                print('y2')
                buttons[spaces[i][1]][spaces[i][0]].configure(text='0')
                zeroes.append(i)
                checked.append([spaces[i][0],spaces[i][1]])
        else:
            if [spaces[i][0],spaces[i][1]] not in checked:
                checked.append([spaces[i][0],spaces[i][1]])
    if len(zeroes) > 0:
        for j in range(len(zeroes)):
            check_space(spaces[j][1],spaces[j][0])
        

##Reveals if mine is present
def reveal(row,column):
    global mines
    global buttons
    global checked
    mine_spot = False
    ##Checks if mine
    for e in range(len(mines)):
        if column == mines[e][0]:
            if row == mines[e][1]:
                mine_spot = True
    if mine_spot == True:
        main.destroy()
        print("Game over. Try again!")
    else:
        buttons[row][column].configure(state=tk.DISABLED,bg='light blue')
        number_mines = get_nearby(row,column)
        buttons[row][column].configure(text=str(number_mines))
        checked.append([column,row])
        ##If 0, checks nearby to auto-remove 0
        if number_mines == 0:
            check_space(row,column)
                    
                

def build_GUI(x_length,y_length):
    global buttons
    ##In range, generates mine
    for c in range(y_length):
        temp = []
        for d in range(x_length):
            button = tk.Button(main,text='',bg='light grey',command=lambda row=c,column=d: reveal(row,column),width=10,height=5)
            button.grid(column=d,row=c)
            temp.append(button)
        ##Appends to list so can be configured
        buttons.append(temp)

##Runs
gen_mines(num_mines)
build_GUI(x_length,y_length)


##http://usingpython.com/dynamically-creating-widgets/
##https://smallguysit.com/index.php/2017/03/11/tkinter-grid-set-default-grid-size/
##https://stackoverflow.com/questions/37731654/how-to-retrieve-the-row-and-column-information-of-a-button-and-use-this-to-alter
##https://stackoverflow.com/questions/31166542/how-to-get-grid-information-from-pressed-button-in-tkinter?rq=1
##https://stackoverflow.com/questions/44588154/python-tkinter-how-to-config-a-button-that-was-generated-in-a-loop
