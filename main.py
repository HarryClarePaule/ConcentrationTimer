import tkinter
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer_start():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_secs)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# create window
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# create canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="/Users/harry/PycharmProjects/day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# add countdown function
#count_down(5)

# create label
title_label = tkinter.Label(text="Timer", font=("Arial", 35, "bold"))
title_label.grid(column=1, row=0)
title_label.config(padx=5, pady=5, fg=GREEN, bg=YELLOW)
check_label = tkinter.Label(font=("Arial", 35, "bold"))
check_label.grid(column=1, row=3)
check_label.config(padx=5, pady=5, fg=GREEN, bg=YELLOW)

# create button
button_start = tkinter.Button(text="Start", command=timer_start)
button_start.grid(column=0, row=2)
button_start.config(padx=5, pady=5)
button_reset = tkinter.Button(text="Reset", command=timer_reset)
button_reset.grid(column=2, row=2)
button_reset.config(padx=5, pady=5)


# keep window on screen
window.mainloop()
