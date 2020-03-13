import random
import tkinter as tk

##Change grid size and number of mines
global num_mines
num_mines = 30
global x_length
x_length = 20
global y_length
y_length = 20
global geometry_size
geometry_size = 1000

##Global variables
global mines
mines = []

global buttons
buttons = []

global checked
checked = []

global unpressed
unpressed = (x_length * y_length)

global place_flag
place_flag = False

global difficulty
difficulty = 0

def get_size():
    global geometry_size
    size_string = str(geometry_size) + 'x' + str(geometry_size)
    return size_string

##Initialises Tkinter
size_string = get_size()
main = tk.Tk()
main.title('Minesweeper!')
main.geometry(size_string)

def sel(enter_b,var):
    enter_b.configure(state=tk.NORMAL)
    global difficulty
    print("Selected")
    difficulty = var.get()

def start(top_l):
    global difficulty
    global num_mines
    global x_length
    global y_length
    top_l.destroy()
    if difficulty == 1:
        num_mines = 11
        x_length = 9
        y_length = 9
    elif difficulty == 2:
        num_mines = 54
        x_length = 20
        y_length = 20
    elif difficulty == 3:
        num_mines = 217
        x_length = 40
        y_length = 40
    gen_mines(num_mines)
    build_GUI(x_length,y_length)

##Gets difficulty
def get_difficulty():
    v_int = tk.IntVar()
    t_l = tk.Toplevel(main)
    t_l.geometry('200x200')
    label1 = tk.Label(t_l,text="Please select a difficulty",padx=5)
    label1.grid(column=0,row=0,sticky=tk.W)
    enter = tk.Button(t_l,text="Start game",command=lambda top_l=t_l:start(top_l),padx=5,state=tk.DISABLED)
    enter.grid(column=0,row=4,sticky=tk.W)
    r_b1 = tk.Radiobutton(t_l,text="Easy: 9x9, 11 mines",variable=v_int,value=1,padx=5,command=lambda enter_b=enter,var=v_int:sel(enter_b,var))
    r_b1.grid(column=0,row=1,sticky=tk.W)
    r_b2 = tk.Radiobutton(t_l,text="Medium: 20x20, 54 mines",variable=v_int,value=2,padx=5,command=lambda enter_b=enter,var=v_int:sel(enter_b,var))
    r_b2.grid(column=0,row=2,sticky=tk.W)
    r_b3 = tk.Radiobutton(t_l,text="Hard: 40x40, 217 mines",variable=v_int,value=3,padx=5,command=lambda enter_b=enter,var=v_int:sel(enter_b,var))
    r_b3.grid(column=0,row=3,sticky=tk.W)
    label2 = tk.Label(t_l,text="""Hint: Press F to enter
flag-placing and -removing mode""",justify=tk.LEFT)
    label2.grid(column=0,row=5,sticky=tk.W)

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
    global mines
    global unpressed
    spaces = get_nearby_spaces(row,column)
    zeroes = []
    for i in range(len(spaces)):
        number_mines = get_nearby(spaces[i][1],spaces[i][0])
        if number_mines == 0:
            if [spaces[i][0],spaces[i][1]] not in checked:
                temp = False
            else:
                temp = True
            if (spaces[i][1] < y_length) and (spaces[i][1] >= 0) and (spaces[i][0] >= 0)  and (spaces[i][0] < x_length) and ([spaces[i][0],spaces[i][1]] not in checked) and ([spaces[i][0]],[spaces[i][1]] not in mines):
                buttons[spaces[i][1]][spaces[i][0]].configure(text='0',state=tk.DISABLED,bg='light blue',relief='groove')
                unpressed -= 1
                checked.append([spaces[i][0],spaces[i][1]])
                check_space(spaces[i][1],spaces[i][0])
        else:
            if ([spaces[i][0],spaces[i][1]] not in checked) and (spaces[i][1] < y_length) and (spaces[i][1] >= 0) and (spaces[i][0] >= 0)  and (spaces[i][0] < x_length) and ([spaces[i][0]],[spaces[i][1]] not in mines):
                checked.append([spaces[i][0],spaces[i][1]])
                buttons[spaces[i][1]][spaces[i][0]].configure(text=str(number_mines),state=tk.DISABLED,bg='light blue',relief='groove')
                unpressed -= 1

##Reveals if mine is present
def reveal(row,column):
    global mines
    global buttons
    global checked
    global unpressed
    global num_mines
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
        buttons[row][column].configure(state=tk.DISABLED,bg='light blue',relief='groove')
        number_mines = get_nearby(row,column)
        buttons[row][column].configure(text=str(number_mines))
        checked.append([column,row])
        unpressed -= 1
        ##If 0, checks nearby to auto-remove 0
        if number_mines == 0:
            check_space(row,column)
        if unpressed == num_mines:
            main.destroy()
            root = tk.Tk()
            root.title('Winner!')
            root.geometry('200x200')
            text = tk.Label(root,text='Winner!\nCongratulations!',bg='light blue')
            text.grid(column=0,row=0,sticky=tk.NW)

def flag(row,column):
    global buttons
    nums = ['0','1','2','3','4','5','6','7','8']
    if buttons[row][column].cget('text') == 'F':
        buttons[row][column].configure(text='')
    elif buttons[row][column].cget('text') in nums:
        pass
    elif buttons[row][column].cget('text') not in nums and buttons[row][column].cget('text') != 'F':
        buttons[row][column].configure(text='F')

def switch_commands(self):
    global buttons
    global place_flag
    if place_flag == False:
        place_flag = True
        for j in range(len(buttons)):
            for k in range(len(buttons[j])):
                buttons[j][k].configure(command=lambda row=j,column=k: flag(row,column))
    elif place_flag == True:
        place_flag = False
        for l in range(len(buttons)):
            for m in range(len(buttons[l])):
                buttons[l][m].configure(command=lambda row=l,column=m: reveal(row,column))

def build_GUI(x_length,y_length):
    global buttons
    global geometry_size
    global photo_img
    ##In range, generates mine
    for c in range(y_length):
        temp = []
        for d in range(x_length):
            frame = tk.Frame(main,width=20,height=20)
            frame.grid(column=d,row=c)
            frame.grid_propagate(False)
            frame.rowconfigure(c,weight=1)
            frame.columnconfigure(d,weight=1)
            button = tk.Button(frame,text='',bg='light grey',command=lambda row=c,column=d: reveal(row,column))
            button.grid(column=d,row=c,sticky="NESW")
            temp.append(button)
        ##Appends to list so can be configured
        buttons.append(temp)
    main.bind('<f>',switch_commands)

##Runs
get_difficulty()

##http://usingpython.com/dynamically-creating-widgets/
##https://smallguysit.com/index.php/2017/03/11/tkinter-grid-set-default-grid-size/
##https://stackoverflow.com/questions/37731654/how-to-retrieve-the-row-and-column-information-of-a-button-and-use-this-to-alter
##https://stackoverflow.com/questions/31166542/how-to-get-grid-information-from-pressed-button-in-tkinter?rq=1
##https://stackoverflow.com/questions/44588154/python-tkinter-how-to-config-a-button-that-was-generated-in-a-loop
##https://realpython.com/python-thinking-recursively/
##https://www.reddit.com/r/learnpython/comments/8xxkez/tkinter_why_cant_i_create_a_square_button/
##https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
##https://stackoverflow.com/questions/26765218/get-the-text-of-a-button-widget
##https://stackoverflow.com/questions/18884782/typeerror-worker-takes-0-positional-arguments-but-1-was-given
##https://www.python-course.eu/tkinter_radiobuttons.php
##https://effbot.org/tkinterbook/tkinter-application-windows.htm
