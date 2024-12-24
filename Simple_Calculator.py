from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.configure(bg="pink")

def button_click(number):
  # screen.delete(0, END)
  current = screen.get()
  screen.delete(0, END)
  screen.insert(0, str(current) + str(number))


def button_clear():
  screen.delete(0, END)

def button_add():
  first_operator = screen.get()
  global f_op
  global operation
  operation = "addition"
  f_op = float(first_operator)
  screen.delete(0, END)

def button_subtract():
  first_operator = screen.get()
  global f_op
  global operation
  operation = "substraction"
  f_op = float(first_operator)
  screen.delete(0, END)


def button_multiply():
  first_operator = screen.get()
  global f_op
  global operation
  operation = "multiplication"
  f_op = float(first_operator)
  screen.delete(0, END)


def button_devide():
  first_operator = screen.get()
  global f_op
  global operation
  operation = "division"
  f_op = float(first_operator)
  screen.delete(0, END)

def button_equal():
  second_operator = screen.get()
  screen.delete(0, END)

  if operation == "addition":
      screen.insert(0, f_op + float(second_operator))
  if operation == "substraction":
      screen.insert(0, f_op - float(second_operator))
  if operation == "multiplication":
      screen.insert(0, f_op * float(second_operator))
  if operation == "division":
      if float(second_operator) == 0:
         screen.insert(0, "Error")
      else:
        screen.insert(0, f_op / float(second_operator))


screen = Entry(window, width=45, borderwidth=5)
screen.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

b9 = Button(window, text="9", bg="pink", padx=40, pady=20, command=lambda: button_click(9))
b9.grid(row=1, column=2, padx=5, pady=5)

b8 = Button(window, text="8", bg="pink", padx=40, pady=20, command=lambda: button_click(8))
b8.grid(row=1, column=1, padx=5, pady=5)

b7 = Button(window, text="7", bg="pink", padx=40, pady=20, command=lambda: button_click(7))
b7.grid(row=1, column=0, padx=5, pady=5)

b6 = Button(window, text="6", bg="pink", padx=40, pady=20, command=lambda: button_click(6))
b6.grid(row=2, column=2, padx=5, pady=5)

b5 = Button(window, text="5", bg="pink", padx=40, pady=20, command=lambda: button_click(5))
b5.grid(row=2, column=1, padx=5, pady=5)

b4 = Button(window, text="4", bg="pink", padx=40, pady=20, command=lambda: button_click(4))
b4.grid(row=2, column=0, padx=5, pady=5)

b3 = Button(window, text="3", bg="pink", padx=40, pady=20, command=lambda: button_click(3))
b3.grid(row=3, column=2, padx=5, pady=5)

b2 = Button(window, text="2", bg="pink", padx=40, pady=20, command=lambda: button_click(2))
b2.grid(row=3, column=1, padx=5, pady=5)

b1 = Button(window, text="1", bg="pink", padx=40, pady=20, command=lambda: button_click(1))
b1.grid(row=3, column=0)

b0 = Button(window, text="0", bg="pink", padx=40, pady=20, command=lambda: button_click(0))
b0.grid(row=4, column=0, padx=5, pady=5)

btn_add = Button(window, text="+", bg="pink", padx=39, pady=20, command=button_add)
btn_add.grid(row=5, column=0, padx=5, pady=5)

btn_subtract = Button(window, text="-", bg="pink", padx=40, pady=20, command=button_subtract)
btn_subtract.grid(row=6, column=0, padx=5, pady=5)

btn_multiply = Button(window, text="×", bg="pink", padx=39, pady=20, command=button_multiply)
btn_multiply.grid(row=6, column=1, padx=5, pady=5)

btn_devide = Button(window, text="÷", bg="pink", padx=40, pady=20, command=button_devide)
btn_devide.grid(row=6, column=2, padx=5, pady=5)

btn_equal = Button(window, text="=", bg="pink", padx=91, pady=20, command= button_equal)
btn_equal.grid(row=5, column=1, padx=5, pady=5, columnspan=2)

  
btn_clear = Button(window, text="Clear", bg="pink", padx=79, pady=20, command=button_clear)
btn_clear.grid(row=4, column=1, padx=5, pady=5, columnspan=2)


window.mainloop()