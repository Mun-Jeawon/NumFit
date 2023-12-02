from tkinter import *
import random

answer = random.randint(1, 100)

def guessing():
    guess = int(guessField.get())
    
    if guess > answer:
        msg = "높음!!"
    elif guess < answer:
        msg = "낮음!!"
    else:
        msg = "정답!!"
    
    resultLabel["text"] = msg
    guessField.delete(0, END)  

def reset(): 
    global answer
    answer = random.randint(1, 100)
    resultLabel["text"] = "다시 한번 하세요!"

def clicked():
    clicked.counter += 1
    label['text'] = '시도 횟수: ' + str(clicked.counter)

clicked.counter = 0

window = Tk()
window.configure(bg="white")
window.title("숫자를 맞춰보세요!")

canvas = Canvas(window, width=650, height=100, bg='#afeeee')
canvas.create_text(325, 50, fill="darkblue", font="Times 30 italic bold",
                   text="분반:3 학번:20201267 이름:문재원")
canvas.pack()

label = Label(window, text="아직 눌려지지 않음")
label.pack()
guessField = Entry(window)
guessField.pack(side="left")

tryButton = Button(window, text="시도", fg="green", bg="white",
                   command=guessing)  
tryButton.pack(side="left")

resetButton = Button(window, text="초기화", fg="red", bg="white",
                     command=reset)
resetButton.pack(side="left")
resultLabel = Label(window, text="1부터 100사이의 숫자를 입력하시오.",
                    bg="white")
resultLabel.pack(side="left")

canvas = Canvas(window, width=70, height=70)
canvas.pack(side="left")

img = PhotoImage(file="C:/numfit/snowman.png")  
canvas.create_image(20, 20, anchor=NW, image=img)

clicked.counter = 0

window.mainloop()

