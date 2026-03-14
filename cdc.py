#TIC TAC TOE -  [ GUI ]

import tkinter as tk

root = tk.Tk()
root.title("TIC TAC TOE")

buttons = []
board = [""]*9
current_player = "X"
def disable_buttons():
    for button in buttons:
        button.config(state="disabled")
def check_winner(player):
    win_conditions = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False
def reset_game():
    global current_player

    current_player = "X"

    for i in range(9):
        board[i] = ""
        buttons[i].config(text="",state="normal")

def click(position):

    global current_player

    if current_player == "X":
        buttons[position].config(bg="blue",fg="white")
    else:
        buttons[position].config(bg="yellow",fg="black")

    if board[position] == "":
        board[position] = current_player
        buttons[position]["text"] = current_player

        if check_winner(current_player) == True:
            result_label.config(text=f"Winner = {current_player}")
            disable_buttons()
            #print("Winner - ",current_player)
        else:
            if current_player == "X":
                current_player = "O"
                result_label.config(text="Current Player = O")
            else:
                current_player = "X"
                result_label.config(text="Current Player = X")
    #print("Button Clicked", position)
    
for i in range(3):
    for j in range(3):
        button = tk.Button(root,
                           text="",
                           height=3,
                           width=10,
                           command=lambda pos =i*3+j : click(pos))
        button.grid(row=i,column=j)
        buttons.append(button)
        
result_label = tk.Label(root,text="Current Player - X")
result_label.grid(row=3,column=0,columnspan=3)
reset_button=tk.Button(root,text="Reset",command=reset_game)
reset_button.grid(row=4,column=0,columnspan=3)

root.mainloop()
