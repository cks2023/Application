from tkinter import*
import math

# Initialize the calculator window
root = Tk()
root.title("Calculator")


# Create a function to add elements to the display
def button_click(number):
  current = display.get()
  display.delete(0, END)
  display.insert(0, str(current) + str(number))


# Create a function to delete one element from the display
def button_delete():
  current = display.get()
  if len(current) > 0:
    display.delete(len(current) - 1, END)


# Create a function to handle decimal input
def button_decimal():
  current = display.get()
  if "." not in current:
    display.insert(END, ".")


# Create a function to clear the display
def button_clear():
  display.delete(0, END)


# Create a function to add the % operator to the display
# Create a function to calculate percentages
def button_percent():
  equation = display.get()
  try:
    result = str(eval(equation + "/100"))
    display.delete(0, END)
    display.insert(0, result)
  except:
    display.delete(0, END)
    display.insert(0, "Error")


# Create a function to calculate square roots
def button_sqrt():
  equation = display.get()
  try:
    result = str(math.sqrt(float(equation)))
    display.delete(0, END)
    display.insert(0, result)
  except:
    display.delete(0, END)
    display.insert(0, "Error")


# Create a function to evaluate the equation
def button_equal():
  equation = display.get()
  try:
    result = str(eval(equation))
    display.delete(0, END)
    display.insert(0, result)
  except:
    display.delete(0, END)
    display.insert(0, "Error")


# Create the calculator display
display = Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=6, padx=10, pady=20)

# Create the calculator buttons
button_1 = Button(root,
                  text="1",
                  padx=40,
                  pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root,
                  text="2",
                  padx=40,
                  pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root,
                  text="3",
                  padx=40,
                  pady=20,
                  command=lambda: button_click(3))
button_4 = Button(root,
                  text="4",
                  padx=40,
                  pady=20,
                  command=lambda: button_click(4))
button_5 = Button(root,
                  text="5",
                  padx=40,
                  pady=20,
                  command=lambda: button_click(5))
button_6 = Button(root,
                  text="6",
                  padx=40,
                  pady=20,
                  command=lambda: button_click(6))
button_7 = Button(root,
                  text="7",
                  padx=40,
                  pady=20,
                  command=lambda: button_click(7))
button_8 = Button(root,
                  text="8",
                  padx=40,
                  pady=20,
                  command=lambda: button_click(8))
button_9 = Button(root,
                  text="9",
                  padx=40,
                  pady=20,
                  command=lambda: button_click(9))
button_0 = Button(root,
                  text="0",
                  padx=45,
                  pady=20,
                  command=lambda: button_click(0))
button_add = Button(root,
                    text="+",
                    padx=40,
                    pady=20,
                    command=lambda: button_click("+"))
button_percent = Button(root,
                        text="%",
                        padx=40,
                        pady=20,
                        command=button_percent)
button_subtract = Button(root,
                         text="-",
                         padx=40,
                         pady=20,
                         command=lambda: button_click("-"))
button_multiply = Button(root,
                         text="*",
                         padx=45,
                         pady=20,
                         command=lambda: button_click("*"))
button_divide = Button(root,
                       text="/",
                       padx=40,
                       pady=20,
                       command=lambda: button_click("/"))
button_equal = Button(root, text="=", padx=45, pady=20, command=button_equal)
button_clear = Button(root, text="Clr", padx=40, pady=20, command=button_clear)
button_delete = Button(root,
                       text="del",
                       padx=40,
                       pady=20,
                       command=button_delete)
button_sqrt = Button(root, text="sqrt", padx=40, pady=20, command=button_sqrt)
button_decimal = Button(root,
                        text=".",
                        padx=45,
                        pady=20,
                        command=button_decimal)
# Put the buttons on the screen
button_clear.grid(row=1, column=0)
button_add.grid(row=1, column=1)
button_subtract.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)
button_divide.grid(row=1, column=0)
button_clear.grid(row=1, column=0)
button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_0.grid(row=3, column=3)
button_delete.grid(row=2, column=3)
button_equal.grid(row=4, column=3)
button_percent.grid(row=1, column=4)
button_sqrt.grid(row=2, column=4)
button_decimal.grid(row=3, column=4)
