from tkinter import *
import tkinter.messagebox

# Initialize Tkinter window
root = Tk()
root.title('Tic Tac Toe')
root.resizable(False, False)
try:
    root.iconbitmap('tictactoe.ico')
except:
    pass  # Ignore if icon file is missing

# Game state variables
click = True  # X starts first
count = 0  # Move counter
Xmove = []
Omove = []
move_all = []

# Load images for X and O
try:
    xPhoto = PhotoImage(file='X.png')
    oPhoto = PhotoImage(file='O.png')
    # Create a blank image for empty buttons
    emptyPhoto = PhotoImage(width=100, height=100)
except Exception as e:
    print(f"Error loading images: {e}")
    # Fallback to text if images fail to load
    xPhoto = None
    oPhoto = None
    emptyPhoto = None

# Store button references
btn = {}  # Dictionary to store button references

# Winning conditions
winning_positions = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
    [1, 5, 9], [3, 5, 7]  # Diagonals
]

# Function to check if a player has won
def check_win(moves):
    return any(all(pos in moves for pos in line) for line in winning_positions)

# Function to check for a draw
def check_draw():
    return count == 9

# Function to handle button presses
def press(num):
    global click, count

    if num not in move_all:  # Ensure the button is not already taken
        if click:  # X's Turn
            if xPhoto:
                btn[num].config(image=xPhoto)
            else:
                btn[num].config(text='X')
            btn[num].config(state=DISABLED)
            Xmove.append(num)
            move_all.append(num)
            count += 1

            if check_win(Xmove):
                tkinter.messagebox.showinfo("Game Over", "X Wins!")
                disable_buttons()
                return
            
            if check_draw():
                tkinter.messagebox.showinfo("Game Over", "It's a Draw!")
                disable_buttons()
                return

            click = False  # Switch turn
            root.after(500, ai_move)  # Delay AI move slightly for better UX

# AI's move (O) - Never loses
def ai_move():
    global count, click

    # --- Win if possible ---
    for move in range(1, 10):
        if move not in move_all:
            temp_moves = Omove + [move]
            if check_win(temp_moves):
                place_o(move)
                return

    # --- Block X if it's about to win ---
    for move in range(1, 10):
        if move not in move_all:
            temp_moves = Xmove + [move]
            if check_win(temp_moves):
                place_o(move)
                return
    
    # --- Handle special cases ---
    # Detect the opposite corners strategy (when player has two opposite corners)
    opposite_corners = [[1, 9], [3, 7]]
    for corners in opposite_corners:
        if all(corner in Xmove for corner in corners) and count == 3:
            # If player has opposite corners and we have the center,
            # we must take an edge (2, 4, 6, or 8) to prevent a fork
            edges = [2, 4, 6, 8]
            for edge in edges:
                if edge not in move_all:
                    place_o(edge)
                    return
    
    # Handle the case where player might create a fork with a corner and an edge
    if count == 3 and 5 in Omove:
        # Check for potential fork setups
        corner_edge_forks = [
            ([1, 6], 3), ([3, 4], 1), ([7, 2], 9), ([9, 8], 7),  # Corner + adjacent edge
            ([1, 8], 7), ([3, 8], 9), ([7, 6], 1), ([9, 4], 3)   # Corner + opposite edge
        ]
        
        for moves, block in corner_edge_forks:
            if all(move in Xmove for move in moves) and block not in move_all:
                place_o(block)
                return

    # --- Play the best strategic move ---
    best_moves = [5, 1, 3, 7, 9, 2, 4, 6, 8]  # Prioritize center > corners > edges
    for move in best_moves:
        if move not in move_all:
            place_o(move)
            return

    # If we get here and no move was made, check for draw
    if check_draw():
        tkinter.messagebox.showinfo("Game Over", "It's a Draw!")
        disable_buttons()

# Helper function to place 'O' (AI Move)
def place_o(move):
    global count, click
    
    Omove.append(move)
    move_all.append(move)
    if oPhoto:
        btn[move].config(image=oPhoto)
    else:
        btn[move].config(text='O')
    btn[move].config(state=DISABLED)
    count += 1

    if check_win(Omove):
        tkinter.messagebox.showinfo("Game Over", "O Wins!")
        disable_buttons()
        return
    
    if check_draw():
        tkinter.messagebox.showinfo("Game Over", "It's a Draw!")
        disable_buttons()
        return

    click = True  # Switch turn back to X

# Disable all buttons when the game ends
def disable_buttons():
    for i in range(1, 10):
        btn[i].config(state=DISABLED)

# Reset game function (for future use)
def reset_game():
    global click, count, Xmove, Omove, move_all
    click = True
    count = 0
    Xmove = []
    Omove = []
    move_all = []
    for i in range(1, 10):
        if emptyPhoto:
            btn[i].config(image=emptyPhoto)
        else:
            btn[i].config(text='')
        btn[i].config(state=NORMAL)

# Add a reset button
reset_btn = Button(root, text="New Game", command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

# Create buttons for the Tic-Tac-Toe board
positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
for i, (row, col) in enumerate(positions, start=1):
    if xPhoto:  # If images are available, use them
        btn[i] = Button(root, image=emptyPhoto, width=100, height=100, command=lambda i=i: press(i))
    else:  # Otherwise use text
        btn[i] = Button(root, text='', width=10, height=5, command=lambda i=i: press(i))
    btn[i].grid(row=row, column=col)

# Start the game loop
root.mainloop()
