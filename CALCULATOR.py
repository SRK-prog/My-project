from tkinter import *

root = Tk()
root.title("CALCULATOR")


e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0,columnspan=7, padx=20, pady= 10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    sec_num = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + int(sec_num))
    if math == "multi":
        e.insert(0, f_num * int(sec_num))
    if math == "divide":
        e.insert(0, f_num / int(sec_num))
    if math == "subtraction":
        e.insert(0, f_num - int(sec_num))
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multi"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_clear():
    e.delete(0, END)


button_1 = Button(root, text="1", padx=30, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=10, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=29, pady=10, command=button_add)
button_multiply = Button(root, text="x", padx=30, pady=10, command=button_multiply)
button_divide = Button(root, text="/", padx=31, pady=10, command=button_divide)
button_subtract = Button(root, text="-", padx=31, pady=10, command=button_subtract)
button_equal = Button(root, text="=", padx=29, pady=10, command=button_equal)

button_clear = Button(root, text="C", padx=29, pady=10, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3,column=2)
button_clear.grid(row=1,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_add.grid(row=2,column=3)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_multiply.grid(row=3,column=3)

button_0.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_subtract.grid(row=4,column=0)
button_divide.grid(row=4,column=3)

mainloop()