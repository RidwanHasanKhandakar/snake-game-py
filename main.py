from tkinter import*
import random
GAME_WIDTH=600
GAME_HEIGHT=600
SPEED=50
SPACE_SIZE=50
BODY_PARTS=3
SNAKE_COLOR="#00ff00"
FOOD_COLOR="#ff0000"
BACKGROUND_COLOR="#000000"
class snake:
    pass
class food:
    pass
def next_tuen():
    pass
def change_dir(new_dir):
    pass
def check_coll():
    pass
def game_over():
    pass
window=Tk()
window.title("Snake game")
window.resizable(False,False)
scr=0
dir='down'
label=Label(window,text="SCORE{}".format(scr),font=("impact",40))
label.pack()
canvas=Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window.mainloop()