from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
durchläufe = 0
geschaffte_pomodoros = 0
timer = None
# ---
def start_pomodoro():
    global durchläufe
    durchläufe += 1
    print(durchläufe)

    if durchläufe % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED)
        add_checkmark()

    elif durchläufe % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        timer_label.config(text="Short Break", fg=PINK)
        add_checkmark()

    else:
        timer_label.config(text="Working", fg=GREEN)
        count_down(WORK_MIN * 60)


def reset():
    global durchläufe
    durchläufe = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text = 'Timer')

def count_down(count):
    global timer
    global  geschaffte_pomodoros
    count_min = math.floor(count / 60)
    count_sec = count % 60
    count_min_string = str(count_min)
    count_sec_string = str(count_sec)

    #Hört auf zu zählen, wenn 0 erreicht ist
    if count > -1:

        #Wenn 0 erreicht ist, wird ein Checkmark hinzugefügt
        if count_min == 0 and count_sec == 0:
            geschaffte_pomodoros += 1
            start_pomodoro()

        else:

            #WFormatierung, wenn 0 in der Zahl vorkommt
            if count_min == 0:
                count_min_string = "00"
            if count_sec == 0:
                count_sec_string = "00"
            if count_sec < 10:
                count_sec_string = f"0{count_sec}"

            #Gibt die aktuelle Zeit aus
            canvas.itemconfig(timer_text, text=f"{count_min_string}:{count_sec_string}")
            timer = window.after(1000, count_down, count - 1)

def add_checkmark():
    global  geschaffte_pomodoros
    checkmarks = "✔" * geschaffte_pomodoros
    checkmark_label.config(text=checkmarks)


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg= GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
timer_label.grid(row=0, column = 1)

start_button = Button(text="Start", bg=YELLOW, font=(FONT_NAME, 20, "bold"), command = start_pomodoro)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, font=(FONT_NAME, 20, "bold"), command = reset)
reset_button.grid(row=2, column=2)

checkmark_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(row=3, column=1)

window.mainloop()