from tkinter import *
from random import randint

root = Tk()
root.title("Guess The Number")
root.geometry("500x500")
root['background'] = 'light blue'

num_label = Label(root, text="Pick A number\nBetween 1 and 100!", font=("Brush script MT", 30))
num_label.pack(pady=20)

score_label = Label(root, text="Your Score: 0")
score_label.pack(pady=20)
global A
A = []

def guesser():
    if guess_box.get().isdigit():
        count = 0
               
     
        while (count <10):
            guess = guess_box.get()
            guess = int(guess)
            if (guess<num):
                num_label.config(text="Oops you entered a smaller number!!!")
                count=count+1
                break
            elif (guess>num):
                num_label.config(text="Oops you entered a larger number!!!")
                count = count+ 1
                break
            else:
                num_label.config(text="Yeah, you are corret!!!")
                score_label.config(text=f"Your score: {100 - (len(A))*10}")
                break


            count += 1
        A.append(count)

            

    else:
        num_label.config(text="Please Enter the number not a letter!!! ")



def rando():
    global num
    global count
    count = 0
    num = randint(1,100)
    #clear the guess box
    guess_box.delete(0, END)
    print(num)



guess_box = Entry(root, font=("Helvetica", 20), width=2)
guess_box.pack(pady=20)

guess_button =  Button(root, text="Submit", command=guesser)
guess_button.pack(pady=20)

rand_button = Button(root, text="New Number", command=rando)
rand_button.pack(pady=20)


rando()
root.mainloop()
