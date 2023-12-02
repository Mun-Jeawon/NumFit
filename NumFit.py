from tkinter import *
import random
import json
from tkinter import simpledialog, messagebox

class ClickCounter:
    def __init__(self):
        self.counter = 0

answer = random.randint(1, 100)
clicked = ClickCounter()

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
        save_ranking()
    
    resultLabel["text"] = msg
    guessField.delete(0, END)
    increment_counter()

def reset(): 
    global answer
    answer = random.randint(1, 100)
    resultLabel["text"] = "다시 한번 하세요!"
    clear_arrow()
    reset_clicked_counter()

def update_arrow(image_path):
    img = PhotoImage(file=image_path)
    arrow_canvas.img = img  
    arrow_canvas.create_image(20, 20, anchor=NW, image=img)

def clear_arrow():
    arrow_canvas.delete("all")

def increment_counter():
    clicked.counter += 1
    label['text'] = '시도 횟수: ' + str(clicked.counter)
    save_last_attempt(clicked.counter)

def reset_clicked_counter():
    clicked.counter = 0

def save_last_attempt(attempt_count):
    with open("last_attempt.txt", "w") as file:
        file.write(str(attempt_count))

def load_last_attempt():
    try:
        with open("last_attempt.txt", "r") as file:
            content = file.read().strip()
            return int(content) if content else 0
    except FileNotFoundError:
        return 0

def save_ranking():
    player_name = simpledialog.askstring("랭킹 저장", "이름을 입력하세요:")
    if player_name is not None:
        ranking_data = load_ranking()
        ranking_data.append({"name": player_name, "attempts": clicked.counter})
        ranking_data.sort(key=lambda x: x["attempts"])
        save_ranking_data(ranking_data)
        show_ranking()

def load_ranking():
    try:
        with open("ranking.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_ranking_data(data):
    with open("ranking.json", "w") as file:
        json.dump(data, file)

def show_ranking():
    ranking_data = load_ranking()
    if ranking_data:
        ranking_text = "랭킹:\n"
        for i, player in enumerate(ranking_data, start=1):
            ranking_text += f"{i}. {player['name']} - {player['attempts']} 시도\n"
        messagebox.showinfo("랭킹", ranking_text)
    else:
        messagebox.showinfo("랭킹", "랭킹이 비어 있습니다.")

def reset_ranking():
    if messagebox.askokcancel("랭킹 초기화", "랭킹을 초기화하시겠습니까?"):
        save_ranking_data([])
        show_ranking()

def delete_selected_ranking():
    ranking_data = load_ranking()
    selected_ranking = simpledialog.askinteger("랭킹 삭제", "삭제할 랭킹 번호를 입력하세요:")
    if selected_ranking is not None and 1 <= selected_ranking <= len(ranking_data):
        del ranking_data[selected_ranking - 1]
        save_ranking_data(ranking_data)
        show_ranking()

clicked.counter = load_last_attempt()

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

resetRankingButton = Button(window, text="랭킹 초기화", fg="blue", bg="white",
                            command=reset_ranking)
resetRankingButton.pack(side="left")

deleteRankingButton = Button(window, text="선택 랭킹 삭제", fg="purple", bg="white",
                             command=delete_selected_ranking)
deleteRankingButton.pack(side="left")

resultLabel = Label(window, text="1부터 100사이의 숫자를 입력하시오.",
                    bg="white")
resultLabel.pack(side="left")

arrow_canvas = Canvas(window, width=70, height=70)
arrow_canvas.pack(side="left")

# 마지막 시도 횟수 로드
label['text'] = '시도 횟수: ' + str(clicked.counter)

window.mainloop()



