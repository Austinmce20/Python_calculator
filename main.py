# Trying to recreate a calculator with a GUI from memory.

from tkinter import *

# Creating the main window "root" and adding a title for the main window.
root = Tk()
root.title('Calculator')
root.configure(bg='Gray13')
root.attributes('-alpha', 0.82) # adding transparent effect to the root window.


# Creating an entry box at the top to display input
e = Entry(root, width=40)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Defining the functions that will be used for the button commands.
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def Clear():
    e.delete(0, END)

def Add():
    first_num = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_num)
    e.delete(0, END)

def Sub():
    first_num = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_num)
    e.delete(0, END)

def Mul():
    first_num = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_num)
    e.delete(0, END)

def Div():
    first_num = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_num)
    e.delete(0, END)

def Pow():
    first_num = e.get()
    global f_num
    global math
    math = "power"
    f_num = int(first_num)
    e.delete(0, END)

def Squ():
    first_num = e.get()
    global f_num
    global math
    math = "squared"
    f_num = int(first_num)
    e.delete(0, END)

def Cub():
    first_num = e.get()
    global f_num
    global math
    math = 'cubed'
    f_num = int(first_num)
    e.delete(0, END)

def Mod():
    first_num = e.get()
    global f_num
    global math
    math = "modulus"
    f_num = int(first_num)
    e.delete(0, END)

def Fdi():
    first_num = e.get()
    global f_num
    global math
    math = 'floor_division'
    f_num = int(first_num)
    e.delete(0, END)

def Sqrt():
    first_num = e.get()
    global f_num
    global math
    math = 'square_root'
    f_num = int(first_num)
    e.delete(0, END)

def Conv():
    first_num = e.get()
    global f_num
    global math
    return first_num * -1




def Equals():
    second_num = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + int(second_num))
    elif math == 'subtraction':
        e.insert(0, f_num - int(second_num))
    elif math == 'multiplication':
        e.insert(0, f_num * int(second_num))
    elif math == 'division':
        e.insert(0, f_num / int(second_num))
    elif math == 'power':
        e.insert(0, f_num ** int(second_num))
    elif math == 'squared':
        e.insert(0, f_num * f_num)
    elif math == 'cubed':
        e.insert(0, f_num * f_num * f_num)
    elif math == 'modulus':
        e.insert(0, f_num % int(second_num))
    elif math == 'floor_division':
        e.insert(0, f_num // int(second_num))
    elif math == 'square_root':
        e.insert(0, f_num ** 0.5)



# Making buttons
but1 = Button(root, text='1', width=10, command=lambda: button_click(1), bg='Gray63')
but2 = Button(root, text='2', width=10, command=lambda: button_click(2), bg='Gray63')
but3 = Button(root, text='3', width=10, command=lambda: button_click(3), bg='Gray63')

but4 = Button(root, text='4', width=10, command=lambda: button_click(4), bg='Gray63')
but5 = Button(root, text='5', width=10, command=lambda: button_click(5), bg='Gray63')
but6 = Button(root, text='6', width=10, command=lambda: button_click(6), bg='Gray63')

but7 = Button(root, text='7', width=10, command=lambda: button_click(7), bg='Gray63')
but8 = Button(root, text='8', width=10, command=lambda: button_click(8), bg='Gray63')
but9 = Button(root, text='9', width=10, command=lambda: button_click(9), bg='Gray63')

but0 = Button(root, text='0', width=10, command=lambda: button_click(0), bg='Gray26')
butc = Button(root, text="C", width=10, command=Clear, bg='Gray26')
but_conv = Button(root, text="+/-", width=10, command=Conv, bg='Gray26')

buteq = Button(root, text="=", width=10, command=Equals, bg='Gray26')

but_pls = Button(root, text='+', width=10, command=Add, bg='Gray26')
but_min = Button(root, text='-', width=10, command=Sub, bg='Gray26')
but_mul = Button(root, text='x', width=10, command=Mul, bg='Gray26')
but_div = Button(root, text="/", width=10, command=Div, bg='Gray26')

but_pow = Button(root, text='xʸ', width=10, command=Pow, bg='Gray45')
but_squ = Button(root, text='x²', width=10, command=Squ, bg='Gray45')
but_cub = Button(root, text='x³', width=10, command=Cub, bg='Gray45')

but_mod = Button(root, text='%', width=10, command=Mod, bg='Gray45')
but_fdi = Button(root, text='//', width=10, command=Fdi, bg='Gray45')
but_sqrt = Button(root, text='√', width=10, command=Sqrt, bg='Gray45')


# Placing the buttons
but1.grid(row=4, column=0)
but2.grid(row=4, column=1)
but3.grid(row=4, column=2)

but4.grid(row=3, column=0)
but5.grid(row=3, column=1)
but6.grid(row=3, column=2)

but7.grid(row=2, column=0)
but8.grid(row=2, column=1)
but9.grid(row=2, column=2)

but0.grid(row=1, column=1)
butc.grid(row=1, column=0)
but_conv.grid(row=1, column=2)

buteq.grid(row=5, rowspan=4, column=3)

but_pls.grid(row=1, column=3)
but_min.grid(row=2, column=3)
but_mul.grid(row=3, column=3)
but_div.grid(row=4, column=3)

but_pow.grid(row=5, column=0)
but_squ.grid(row=5, column=1)
but_cub.grid(row=5, column=2)

but_mod.grid(row=6, column=0)
but_fdi.grid(row=6, column=1)
but_sqrt.grid(row=6, column=2)
#


root.mainloop()
