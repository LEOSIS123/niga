from microbit import *

# Initialize the chessboard
board = [[' ' for _ in range(5)] for _ in range(5)]
# Place a pawn at the starting position
board[4][2] = 'P'  # Pawn for player 1

# Function to display the board on the micro:bit
def display_board():
    for y in range(5):
        for x in range(5):
            if board[y][x] == 'P':
                display.set_pixel(x, y, 9) # Brightness for pawn
            else:
                display.set_pixel(x, y, 0)  # Clear pixel

# Initial display
display_board()

# Starting position of the pawn
pawn_x, pawn_y = 2, 4

while True:
    if button_a.is_pressed() and pawn_x > 0:  # Move left
        board[pawn_y][pawn_x] = ' '  # Clear current position
        pawn_x -= 1
        board[pawn_y][pawn_x] = 'P'  # Move pawn left
        display_board()
        sleep(500)  # Debounce delay

    elif button_b.is_pressed() and pawn_x < 4:  # Move right
        board[pawn_y][pawn_x] = ' '  # Clear current position
        pawn_x += 1
        board[pawn_y][pawn_x] = 'P'  # Move pawn right
        display_board()
        sleep(500)  # Debounce delay

    if accelerometer.was_gesture("up") and pawn_y > 0:  # Move up
        board[pawn_y][pawn_x] = ' '  # Clear current position
        pawn_y -= 1
        board[pawn_y][pawn_x] = 'P'  # Move pawn up
        display_board()
        sleep(500)  # Debounce delay

    elif accelerometer.was_gesture("down") and pawn_y < 4:  # Move down
        board[pawn_y][pawn_x] = ' '  # Clear current position
        pawn_y += 1
        board[pawn_y][pawn_x] = 'P'  # Move pawn down
        display_board()
        sleep(500)  # Debounce delay

