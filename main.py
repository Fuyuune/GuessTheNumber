from tkinter import *
from tkinter import ttk
import random

randomNumber = random.randrange(1,100)
print("DEBUG: " + str(randomNumber))

def convert():
    input_value = int(guess_entry.get())
    return input_value

def getHint():
  result_content.set("")
  guess_value = convert()
  if guess_value == 0:
     hint_content.set("Please enter a number first!")
  elif guess_value < randomNumber:
    hint_content.set("The number you're looking for is greater than your number.")
  elif guess_value > randomNumber:
    hint_content.set("The number you're looking for is lesser than your number.")

def check():
  try:
    hint_content.set("")
    guess_value = convert()
    triesCount.set(triesCount.get() + 1)
    triesCount_label['text'] = f"Tries: {triesCount.get()}"
    if guess_value != randomNumber:
        result_content.set("Your number is not correct. Try again!")
        result_label['foreground'] = "red"
    else:
        result_content.set("Congratulations! You guessed the right number!")
        result_label['foreground'] = "green"
  except Exception as err:
     result_content.set(f"Unexpected {err=}, {type(err)=}")
     result_label['foreground'] = "red"

#sets up the main application window
root = Tk()
root.title("Guess the number")
root.geometry("400x200")

#create a frame widget 
#optionally pass additional parameters to override default options
mainframe = ttk.Frame(root, padding=(10))
mainframe.grid() #inserting the frame into the user interface

#creating the entry widget
title_label = ttk.Label(mainframe, text="Guess a number between 1 and 100:")
title_label.pack()

guess_entry = ttk.Entry(mainframe, width=15)
guess_entry.pack()

triesCount = IntVar(value=0)
triesCount_label = ttk.Label(mainframe, text=f"Tries: {triesCount.get()}")
triesCount_label.pack()

check_button = ttk.Button(mainframe, text="Check", command=check)
check_button.pack()

hint_button = ttk.Button(mainframe, text="Get Hint", command=getHint)
hint_button.pack()

hint_content = StringVar()
hint_label = ttk.Label(mainframe, textvariable=hint_content)
hint_label.pack()

result_content = StringVar()
result_label = ttk.Label(mainframe, textvariable=result_content)
result_label.pack()

guess_entry.focus()
root.mainloop()