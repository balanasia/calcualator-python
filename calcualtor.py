from tkinter import *
import random


def button_press(num):
    
    global equation_text
    global equation_label

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():

    try:
        global equation_text

        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text=""

    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text=""

def clear():
    global equation_text

    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calcualtor Program")
window.geometry("500x500")

# this will store the equation text
equation_text=""
equation_label = StringVar()

colors=["black", "red", "yellow", "green", "pink"]

label = Label(window, 
                textvariable=equation_label, 
                font=("Impact", 35), 
                bg="white", fg="black",
                width="22", height=2)
label.pack()


frame = Frame(window)
frame.pack()

# hardcoding the values for now
button1 = Button(frame, text="1", height=2, width=5, fg="#ED0A3F", font=("Impact",25), 
                    command=lambda:button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text="2", height=2, width=5, fg="#FF681F", font=("Impact",25), 
                    command=lambda:button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text="3", height=2, width=5, fg="#F2C649", font=("Impact",25), 
                    command=lambda:button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text="4", height=2, width=5, fg="#3AA655", font=("Impact",25),  
                    command=lambda:button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text="5", height=2, width=5, fg="#4997D0", font=("Impact",25), 
                    command=lambda:button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text="6", height=2, width=5, fg="#3F26BF", font=("Impact",25), 
                    command=lambda:button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text="7", height=2, width=5, fg="#8F47B3", font=("Impact",25), 
                    command=lambda:button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text="8", height=2, width=5, fg="#30BFBF", font=("Impact",25), 
                    command=lambda:button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text="9", height=2, width=5, fg="#FF3399", font=("Impact",25), 
                    command=lambda:button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text="0", height=2, width=5, fg="#665233", font=("Impact",25), 
                    command=lambda:button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text="+", height=2, width=5, fg="black", font=("Impact",25), 
                    command=lambda:button_press("+"))
plus.grid(row=0, column=3)

minus = Button(frame, text="-", height=2, width=5, fg="black", font=("Impact",25), 
                    command=lambda:button_press("-"))
minus.grid(row=1, column=3)

divide = Button(frame, text="/", height=2, width=5, fg="black", font=("Impact",25), 
                    command=lambda:button_press("/"))
divide.grid(row=2, column=3)

multiply = Button(frame, text="*", height=2, width=5, fg="black", font=("Impact",25), 
                    command=lambda:button_press("*"))
multiply.grid(row=3, column=3)

equal = Button(frame, text="=", height=2, width=5, fg="black", font=("Impact",25),  
                    command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text=".", height=2, width=5, fg="black", font=("Impact",25), 
                    command=lambda:button_press("."))
decimal.grid(row=3, column=1)

clear = Button(window, text="CLEAR", height=2, width=13, fg="#E30B5C", font=("Impact",25), 
                    command=clear)
clear.pack()

window.mainloop()