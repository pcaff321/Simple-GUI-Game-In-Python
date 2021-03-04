from tkinter import *
from time import *
import random

player_score = 0
t1 = 0
streak = 0
highest_streak = 0
point = 1
obj1 = None
time_interval = 2  # time for the player to click on the figure
# Initiliazing the starter data which will be updated as the code runs

root = Tk()


def new_pos(event):
    t2 = time()
    global player_score
    global t1
    global obj1
    global streak
    global point
    global highest_streak
    global time_interval
    fill_col = 'blue'

    if (t2 - t1) <= time_interval:
        player_score += point
        streak += 1
        if highest_streak < streak:
            highest_streak = streak  # update your highest streak in this game
    else:
        streak = 0
        point = 1
        # streak resets if you don't click within 2 seconds, which means your figure is reverted back to the blue square

    scoreLabel['text'] = "Score: " + str(player_score) + "; Streak: " + str(streak) + "; Highest streak: " + str(highest_streak)
    t1 = time()
    offset = 60 - (3 * streak)

    if offset < 15:
        offset = 15  # to prevent the size from getting too small
        fill_col = 'gold'
        point = 3
        # gold square awards 3 points
    elif offset < 45:
        fill_col = 'red'
        point = 2
        # red square awards 2 points

    if obj1 is not None:
        canvas.delete(obj1)

    xpos = random.randint(1, 500 - offset)
    ypos = random.randint(1, 450 - offset)

    if streak < 25:
        obj1 = canvas.create_polygon(xpos, ypos, xpos + offset, ypos, xpos + offset, ypos + offset, xpos, ypos + offset, fill=fill_col)
    else:
        fill_col = 'cyan'
        point = 5
        # diamond figure will award 5 points
        obj1 = canvas.create_polygon(xpos, ypos + (offset / 2), xpos + (offset / 4), ypos, xpos + (offset / 2), ypos + (offset / 2), xpos + (offset / 4), ypos + offset, fill=fill_col)

    canvas.tag_bind(obj1, "<ButtonPress-1>", new_pos)


def start_game():
    global startButton
    global canvas
    canvas.pack()
    startButton.destroy()
    new_pos(None)


canvas = Canvas(root, width=500, height=500)
canvas.configure(bg='grey')
startButton = Button(root, text="Start Game", padx=50,pady=20, command=start_game)
startButton.pack()
scoreLabel = Label(root, text="Score: 0; Streak: 0", padx=30, pady=10)
scoreLabel.pack()
root.mainloop()
