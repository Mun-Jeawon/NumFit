from tkinter import *
import random

answer = random.randint(1, 100)

def guessing():
    guess = int(guessField.get())
    
    if guess > answer:
        msg = "높음!!"
        update_arrow("C:/numfit/row_arrow.png")
    elif guess < answer:
        msg = "낮음!!"
        update_arrow("C:/numfit/high_arrow.png")
    else:
        msg = "정답!!"
        update_arrow("C:/numfit/snowman.png")
    
    resultLabel["text"] = msg
    guessField.delete(0, END)  

def reset(): 
    global answer
    answer = random.randint(1, 100)
    resultLabel["text"] = "다시 한번 하세요!"
    clear_arrow()

def update_arrow(image_path):
    img = PhotoImage(file=image_path)
    arrow_canvas.img = img  
    arrow_canvas.create_image(20, 20, anchor=NW, image=img)

def clear_arrow():
    arrow_canvas.delete("all")

def clicked():
    clicked.counter += 1
    label['text'] = '시도 횟수: ' + str(clicked.counter)

clicked.counter = 0

window = Tk()
window.configure(bg="white")
window.title("숫자를 맞춰보세요!")

info_canvas = Canvas(window, width=650, height=100, bg='#afeeee')
info_canvas.create_text(300, 50, fill="darkblue", font="Times 30 italic bold",
                   text="분반:3 학번:20201267 이름:문재원")
info_canvas.pack()

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

arrow_canvas = Canvas(window, width=70, height=70)
arrow_canvas.pack(side="left")

clicked.counter = 0

window.mainloop()

