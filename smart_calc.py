from tkinter import *
import math

def btnClick(number):
  global operator
  operator = operator + str(number)
  text_Input.set(operator)


def btnClearDisplay():
  global operator
  operator = ""
  text_Input.set("")


def btnEqualsInput():
  global operator
  sumup = str(eval(operator))
  text_Input.set(sumup)
  operator = ""


def button_delete():
  current = textDisplay.get()
  if len(current) > 0:
    textDisplay.set(len(current) - 1)


cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar(0)
textDisplay = Entry(cal,
                    font=("arial", 30, "bold"),
                    textvariable=text_Input,
                    bd=20,
                    insertwidth=4,
                    bg="powder blue",
                    justify="right").grid(columnspan=5)

b7 = Button(cal,
            padx=16,
            pady=16,
            bd=8,
            fg="black",
            font=("arial", 20, "bold"),
            text="7",
            bg="powder blue",
            command=lambda: btnClick(7)).grid(row=1, column=0)

b8 = Button(cal,
            padx=16,
            pady=16,
            bd=8,
            fg="black",
            font=("arial", 20, "bold"),
            text="8",
            bg="powder blue",
            command=lambda: btnClick(8)).grid(row=1, column=1)

b9 = Button(cal,
            padx=16,
            pady=16,
            bd=8,
            fg="black",
            font=("arial", 20, "bold"),
            text="9",
            bg="powder blue",
            command=lambda: btnClick(9)).grid(row=1, column=2)

add = Button(cal,
             padx=16,
             pady=16,
             bd=8,
             fg="black",
             font=("arial", 20, "bold"),
             text="+",
             bg="powder blue",
             command=lambda: btnClick("+")).grid(row=1, column=3)
#row 2
b6 = Button(cal,
            padx=16,
            pady=10,
            bd=8,
            fg="black",
            font=("arial", 20, "bold"),
            text="6",
            bg="powder blue",
            command=lambda: btnClick(6)).grid(row=2, column=0)

b5 = Button(cal,
            padx=10,
            pady=10,
            bd=8,
            fg="black",
            font=("arial", 20, "bold"),
            text="5",
            bg="powder blue",
            command=lambda: btnClick(5)).grid(row=2, column=1)

b4 = Button(cal,
            padx=10,
            pady=10,
            bd=8,
            fg="black",
            font=("arial", 20, "bold"),
            text="4",
            bg="powder blue",
            command=lambda: btnClick(4)).grid(row=2, column=2)

sub = Button(cal,
             padx=20,
             pady=16,
             bd=8,
             fg="black",
             font=("arial", 20, "bold"),
             text="-",
             bg="powder blue",
             command=lambda: btnClick("-")).grid(row=2, column=3)
# row 3
b3 = Button(cal,
            padx=16,
            pady=16,
            bd=8,
            fg="black",
            font=("arial", 20, "bold"),
            text="3",
            bg="powder blue",
            command=lambda: btnClick(3)).grid(row=3, column=0)

b2 = Button(cal,
            padx=16,
            pady=16,
            bd=8,
            fg="black",
            font=("arial", 20, "bold"),
            text="2",
            bg="powder blue",
            command=lambda: btnClick(2)).grid(row=3, column=1)

b1 = Button(cal,
            padx=16,
            pady=16,
            bd=8,
            fg="black",
            font=("arial", 20, "bold"),
            text="1",
            bg="powder blue",
            command=lambda: btnClick(1)).grid(row=3, column=2)

mul = Button(cal,
             padx=16,
             pady=16,
             bd=8,
             fg="black",
             font=("arial", 18, "bold"),
             text="×",
             bg="powder blue",
             command=lambda: btnClick("*")).grid(row=3, column=3)

clear = Button(cal,
               padx=16,
               pady=16,
               bd=8,
               fg="black",
               font=("arial", 20, "bold"),
               text="C",
               bg="powder blue",
               command=btnClearDisplay).grid(row=4, column=0)

b0 = Button(cal,
            padx=16,
            pady=16,
            bd=8,
            fg="black",
            font=("arial", 20, "bold"),
            text="0",
            bg="powder blue",
            command=lambda: btnClick(0)).grid(row=4, column=1)

equal = Button(cal,
               padx=16,
               pady=16,
               bd=8,
               fg="black",
               font=("arial", 20, "bold"),
               text="=",
               bg="powder blue",
               command=btnEqualsInput).grid(row=4, column=2)

divi = Button(cal,
              padx=16,
              pady=16,
              bd=8,
              fg="black",
              font=("arial", 20, "bold"),
              text="÷",
              bg="powder blue",
              command=lambda: btnClick("/")).grid(row=4, column=3)

dot = Button(cal,
             padx=22,
             pady=16,
             bd=8,
             fg="black",
             font=("arial", 20, "bold"),
             text=".",
             bg="powder blue",
             command=lambda: btnClick(".")).grid(row=4, column=4)

p = Button(cal,
           padx=16,
           pady=16,
           bd=8,
           fg="black",
           font=("arial", 20, "bold"),
           text="%",
           bg="powder blue",
           command=lambda: btnClick("%")).grid(row=3, column=4)

d = Button(cal,
           padx=16,
           pady=16,
           bd=8,
           fg="black",
           font=("arial", 20, "bold"),
           text="del",
           bg="powder blue",
           command=lambda: button_delete).grid(row=2, column=4)
cal.mainloop()