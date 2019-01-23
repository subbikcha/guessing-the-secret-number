from tkinter import messagebox
import random
import tkinter as tk
messagebox.showinfo("RULES","player is provided with five chances .each chance is  followed by hints")
number = random.randint(1, 99)
guesses = 0
while guesses < 5:
    guess = int(input("Enter an integer from 1 to 99: "))
    guesses +=1
    print("this is your %d guess" %guesses)
    
    if guess < number:
        def write_slogan():
            print("Tkinter is easy to use")
        root=tk.Tk()
        frame=tk.Frame(root)
        frame.pack()
        button=tk.Button(frame,text="QUIT",fg="red",command=quit)
        button.pack(side=tk.LEFT)
        slogan=tk.Button(frame,text="guess is low",command=write_slogan)
        slogan.pack(side=tk.LEFT)
        root.mainloop()
        
        
    elif guess > number:
        def write_slogan():
            print("Tkinter is easy to use")
        root=tk.Tk()
        frame=tk.Frame(root)
        frame.pack()
        button=tk.Button(frame,text="QUIT",fg="red",command=quit)
        button.pack(side=tk.LEFT)
        slogan=tk.Button(frame,text="guess is high",command=write_slogan)
        slogan.pack(side=tk.LEFT)
        root.mainloop()
        
    elif guess == number:
        break
if guess == number:
    guesses = str(guesses)
    print ("You guess it in : ", guesses + " guesses")
if guess != number:
    number = str(number)
    print ("The secret number was",  number)
