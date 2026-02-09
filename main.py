from tkinter import *
import pandas as pd
import time



BACKGROUNDCOLOR = "#B1DDC6"
TEXT_BG_GREEN = "#91C2AF"


# ------------------ Logic ------------------ #
def show_polish(word):
    canvas.itemconfig(image_canvas, image=back_img)
    canvas.itemconfig(word_text, text=word)
    canvas.itemconfig(title_text, text="Polski")


def random_word():
    canvas.itemconfig(image_canvas, image=front_img)
    data = pd.read_csv('RU_PL - Arkusz1.csv')
    row = data.sample(n=1).iloc[0]
    row_ru = row["Rosyjski"]
    row_pl = row["Polski"]
    canvas.itemconfig(word_text, text=row_ru)
    canvas.itemconfig(title_text, text="Rosyjski")
    canvas.after(5000, lambda : show_polish(row_pl))

def wrong_button():
    random_word()

def coorect_button():
    random_word()


# --- UI SETUP ---
window = Tk()
window.config(height=800, width=600)
window.title("Słownik Polsko Rosyjski")
window.config(pady=50, padx=50, bg=BACKGROUNDCOLOR)

# --- CONTENT ---
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUNDCOLOR)
front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
image_canvas = canvas.create_image(400,263,  image=front_img)
title_text = canvas.create_text(400, 125, text="Title", font=('Arial', 48, "italic"),fill="black")
word_text = canvas.create_text(400, 256, text="Word", font=('Arial', 60, "bold"), fill="black")
canvas.grid(column=1, row=1)


#------------ Button's --------------- #
correct_button_img = PhotoImage(file='right.png')
right_button = Button(image=correct_button_img, highlightthickness=0, command=coorect_button)
right_button.grid(column=1, row=4,padx=(500, 0) )

incorrect_button_img = PhotoImage(file='wrong.png')
wrong_button = Button(image=incorrect_button_img, highlightthickness=0,command=wrong_button)
wrong_button.grid(column=1, row=4, padx=(0, 500))


# --- CENTER WINDOW ---
window.update_idletasks()
w = window.winfo_width()
h = window.winfo_height()
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()
x = (sw - w) // 2
y = (sh - h) // 2
window.geometry(f"{w}x{h}+{x}+{y}")
# --- FOCUS / TOPMOST (macOS + PyCharm) ---
window.lift()
window.attributes("-topmost", True)
window.after(200, lambda: window.attributes("-topmost", False))
window.focus_force()
# ----- Function Callout ----- #
random_word()
# --- Main Loop --- #
window.mainloop()
