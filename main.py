from tkinter import * #imports everything
from tkinter import ttk #imports the submodule ttk
import random

randomNumber = random.randrange(1,100)
print("DEBUG: " + str(randomNumber))

def convert():
    input_value = int(guess_entry.get())
    return input_value

def getHint():
  guess_value = convert()
  if guess_value == 0:
     hint_content.set("Please enter a number first!")
  elif guess_value < randomNumber:
    hint_content.set("The number you're looking for is greater than your number.")
  elif guess_value > randomNumber:
    hint_content.set("The number you're looking for is lesser than your number.")

def calculate():
  try:
    guess_value = convert()
    if guess_value != randomNumber:
        result_content.set("Your number is not correct. Try again!")
        result_label['foreground'] = "red"
    else:
        result_content.set("Concrats! You guessed the right number")
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
ttk.Label(mainframe, text="Guess a number between 1 and 100:").grid(column=1, row=1)

guess_entry = ttk.Entry(mainframe, width=10)
guess_entry.grid(column=1, row=2, sticky=W)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="Get Hint", command=getHint).grid(column=2, row=3, sticky=W)

hint_content = StringVar()
hint_label = ttk.Label(mainframe, textvariable=hint_content)
hint_label.grid(column=1, row=5)

result_content = StringVar()
result_label = ttk.Label(mainframe, textvariable=result_content)
result_label.grid(column=1, row=4)

guess_entry.focus()
root.mainloop()