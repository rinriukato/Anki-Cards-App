from tkinter import *
from tkinter import messagebox
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
PADDING_X = 50
PADDING_Y = 50
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
WORD_BANK_FILEPATH = "data/jp-en.csv"
WORD_BANK_PROGRESS = "data/words-to-learn.csv"
current_card = None
is_front = True

# ------------------------------------ FILE LOADING ------------------------------------ #

# See if the user has a previous record
try:
    df = pandas.read_csv(WORD_BANK_PROGRESS)

# if not, load from the default bank
except FileNotFoundError:
    df = pandas.read_csv(WORD_BANK_FILEPATH)
    print("could not find progress, restore to default.")
else:
    print("found progress file")

finally:
    word_bank = df.to_dict(orient="records")


def create_new_card():
    global current_card
    current_card = random.choice(word_bank)
    set_card_text('jp')
    set_card_side('jp')


def set_card_text(lang: str):
    global is_front
    # Display Japanese
    if lang == 'jp':
        canvas.itemconfig(title_text, text="日本語")
        canvas.itemconfig(word_text, text=current_card["Japanese"])
    # Display English
    else:
        canvas.itemconfig(title_text, text="English")
        canvas.itemconfig(word_text, text=current_card["English"])


def on_key_press(event):
    if event.char == ' ':
        global is_front

        if is_front:
            set_card_side('en')
            is_front = False
        else:
            set_card_side('jp')
            is_front = True


def on_marked_correct():
    word_bank.remove(current_card)
    words_to_learn = pandas.DataFrame(word_bank)
    words_to_learn.to_csv("data/words-to-learn.csv", index=False)

    create_new_card()
    pass

def set_card_side(lang: str):
    if lang == 'jp':
        set_card_text('jp')
        canvas.itemconfig(canvas_image, image=card_front)
    else:
        set_card_text('en')
        canvas.itemconfig(canvas_image, image=card_back)

# ------------------------------------ UI SET-UP ------------------------------------ #

window = Tk()
window.title("Anki Flashcards")
window.config(padx=PADDING_X, pady=PADDING_Y, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
correct_button_image = PhotoImage(file="images/right.png")
incorrect_button_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 265, image=card_front)
canvas.grid(column=1,row=1, columnspan=2)

title_text = canvas.create_text(400, 150, text="日本語", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text="こにちは", font=WORD_FONT)

create_new_card()

hint_text = Label(text="Press 'Space' to flip the card over!", bg=BACKGROUND_COLOR, font=("Ariel", 20, "italic"),pady=20 )
hint_text.grid(column=1,row=3, columnspan=2)

window.bind('<Key>', func=on_key_press)

correct_button = Button(image=correct_button_image, highlightthickness=0, pady=50, command=on_marked_correct)
correct_button.grid(column=2, row=2)

incorrect_button = Button(image=incorrect_button_image, highlightthickness=0, pady=50, command=create_new_card)
incorrect_button.grid(column=1, row=2)


window.mainloop()

