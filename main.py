from tkinter import * #imports everything
from tkinter import ttk #imports the submodule ttk
import random
import math

#sets up the main application window
root = Tk()
root.title("Guess the number")

#create a frame widget 
#optionally pass additional parameters to override default options
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #inserting the frame into the user interface

#creating the entry widget
guess = StringVar()
ttk.Label(mainframe, text="Guess a number between 1 and 100").grid(column=2, row=1, sticky=N)
guess_entry = ttk.Entry(mainframe, width=7, textvariable=guess)
guess_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate").grid(column=2, row=3, sticky=W)

randomNumber = random.randrange(1,101)
print("DEBUG: " + str(randomNumber))

def getHint(*args):
  if guess < randomNumber:
    print("The number you're looking for is greater than your number.")
  elif guess > randomNumber:
    print("The number you're looking for is lesser than your number.")

while guess != randomNumber:
    print("Your number is not correct. Try again!")
    getHint()
    guess = int(input("Number: "))
else:
    print("Concrats! You guessed the right number")