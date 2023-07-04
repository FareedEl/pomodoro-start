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
marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    canvas.itemconfig(timer_text, text = "00:00")
    reps = 0







# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    long_break_sec = LONG_BREAK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    work_sec = WORK_MIN*60


    reps += 1


    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text = "Work", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global marks

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1) #method that after  amount of time, calls fn w it's arguments (time,fn,*args)
    else:
        start_timer()
        work_sessions = reps//2
        for i in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#creating the canvas (the tomato in this case)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)


#Labels
title = Label(text="Timer", bg=YELLOW, font=("Courier", 55), fg=GREEN)
title.grid(column=1, row=0)

checkmark = Label(text="", bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

#buttons
start_button = Button(text="Start", font=("Arial", 14), highlightbackground=YELLOW, width=3, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=("Arial", 14), highlightbackground=YELLOW, width=3, command=reset_timer)
reset_button.grid(column=2, row=2)










window.mainloop()