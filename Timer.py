from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mytimer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    windows.after_cancel(mytimer)
    canvas.itemconfig(timer_text,text ="00:00")
    title.config(text="Timer")
    check_mark.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="Long Break",fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title.config(text="Work Time", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count > 0:
        global mytimer
        mytimer = windows.after(1000,count_down,count - 1)
        print(count)
    else:
        start_timer()
    marks = ""
    for _ in range(math.floor(reps/2)):
        marks += "✔"
    check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Tomato")
windows.config(padx=100,pady=50,bg = YELLOW)

title = Label(text="Timer",fg= GREEN,font=("Courier",50,"bold"),bg=YELLOW)
title.grid(column=1,row=0)

canvas =Canvas(width=200,height=225,bg= YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,111, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=("Courier",28,"bold"))
canvas.grid(column=1,row=2)
start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=3)
reset_button = Button(text="Reset",highlightthickness=0,bg=YELLOW,command=reset_timer)
reset_button.grid(column=3,row=3)
check_mark=Label(text="✔",fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=4)

windows.mainloop()
