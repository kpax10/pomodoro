from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{remaining_seconds:02}")
    window.after(1000, count_down, seconds - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 143, text='00:00', fill='white', font=(FONT_NAME, 35, "bold italic"))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', command=start_timer, bg='white', highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', bg='white', highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark_label = Label(text='✔', font=(FONT_NAME, 24), bg=YELLOW, fg=GREEN)
checkmark_label.grid(column=1, row=3)


window.mainloop()
