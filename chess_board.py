# The idea is to code a chessboard in multiple ways:
# I) Using a single list, where the indices are a linear representation of a chess board
# II) Possibility to use two list as rows and colums.
#
# to add:
# use of my own modules: 1) Board (could be reused for other games) 2) Pieces (moves, detection, etc.) 
# Turn counter. 
# First pawn move 2 fields is possible
# collision detection pt.II: detect if there are collisions with pieces on the way, not just the endpoint
# GUI where you can click to move the figures
# turns starting with white, then black and only those figues can be moved. display whos turn it is



from prettytable import PrettyTable

# this is the starting formation for a chessboard
chessboard_start = ["\u2656","\u2658","\u2657","\u2655","\u2654","\u2657","\u2658","\u2656",
                     "\u2659","\u2659","\u2659","\u2659","\u2659","\u2659","\u2659","\u2659",
                     "","","","","","","","",
                     "","","","","","","","",
                     "","","","","","","","",
                     "","","","","","","","",
                     "\u265F","\u265F","\u265F","\u265F","\u265F","\u265F","\u265F","\u265F",
                     "\u265C","\u265E","\u265D","\u265B","\u265A","\u265D","\u265E","\u265C"]

# copying the starting chessboard, so that it is unaffected by any changes
chessboard_actual = chessboard_start.copy()


def convert_coordinate_index(let, num):
    if let.upper() == "A":
        num -= 1
    if let.upper() == "B":
        num += 7
    if let.upper() == "C":
        num += 15
    if let.upper() == "D":
        num += 23
    if let.upper() == "E":
        num += 31
    if let.upper() == "F":
        num += 39
    if let.upper() == "G":
        num += 47
    if let.upper() == "H":
        num += 55
    return num

# printing the chessboard in pretty table
def display():
    board = PrettyTable()
    board.field_names = ["","1","2","3","4","5","6","7","8"]
    board.add_row(["A"] + chessboard_actual[0:8:])
    board.add_row(["B"] + chessboard_actual[8:16:])
    board.add_row(["C"] + chessboard_actual[16:24:])
    board.add_row(["D"] + chessboard_actual[24:32:])
    board.add_row(["E"] + chessboard_actual[32:40:])
    board.add_row(["F"] + chessboard_actual[40:48:])
    board.add_row(["G"] + chessboard_actual[48:56:])
    board.add_row(["H"] + chessboard_actual[56:65:])
    print(board)

# input of field that is affected
def field_select():
    letter = str(input("Insert letter:\t"))
    number = int(input("Insert number:\t"))
    return convert_coordinate_index(letter, number)

# basic turn mechanism, that is the core game mechanism
def turn():
    display()                                           #1 display chessboard
    print("\nSelect figure field\n")                
    start = field_select()                              #2 select field with chess piece you want to move
    piece_start = chessboard_actual[start]              #3 store the piece that is selected
    print("\nYou selected\t",piece_start)
    print("\nSelect target field\n")
    target = field_select()                             #4 select field where you want to move chess piece
    piece_target = chessboard_actual[target]            #5 store the piece in the target field
    if move_legality(piece_start, start, target):       #6 check if the desired move is legal for the selected piece
        #basic collision detection: if same color don't move
        if (piece_start in black and piece_target in black) or (piece_start in white and piece_target in white): 
            print("Move not valid. Please try again.")
        else:
            # collision_detection(piece, start, target)
            print ("You moved ", piece_start)
            chessboard_actual[target] = piece_start     #7 if move is legal, repalace the target piece by selected piece
            chessboard_actual[start] = ""
    else:
        print("Move not valid. Please try again.")

    turn()                                              #8 next turn

#funtion to fork into the moving patterns of the different pieces
def move_legality(piece, start, target):
    if piece == "\u2656" or piece == "\u265C":
        return rook_move(start, target)
    if piece == "\u2658" or piece == "\u265E":
        return knight_move(start, target)
    if piece == "\u2657" or piece == "\u265D":
        return bishop_move(start, target)
    if piece == "\u2655" or piece == "\u265B":
        return queen_move(start, target)
    if piece == "\u2654" or piece == "\u265A":
        return king_move(start, target)
    if piece == "\u2659" or piece == "\u265F":
        return pawn_move(start, target)

# legal rook movements
def rook_move(start, target):
    delta = abs(target - start)
    if delta %8 == 0:                                                   #vertikal movement
        return True
    elif delta >= 1 - ((start//8)+1) and delta <= 8 - ((start//8)+1):   #treat horizontal as row 1 and compare to outer borders
        return True 

# legal knight movements
def knight_move(start, target):
    delta = abs(target - start)
    if delta in (6, 10, 15, 17):                                        #knight can only access 8 symmetric fields (4 'negative')
        return True

# legal king movements
def king_move(start, target):
    delta = abs(target - start)
    if delta in (1, 8, 7, 9):                                           #king can only access 8 symmetric fields (4 'negative')
        return True

# legal queen movements
def queen_move(start, target):
    delta = abs(target - start)
    if delta %8 == 0:                                                   #vertical movement
        return True
    elif delta >= 1 - ((start//8)+1) and delta <= 8 - ((start//8)+1):   #treat horizontal as row 1 and compare to outer borders
        return True 
    if delta % 7 == 0 or delta % 9 == 0:                                #diagonal movement
        return True 

# legal pawn movements
def pawn_move(start, target):
    delta = abs(target - start)
    if delta == 8:                                                      #one horizontal move
        return True
    elif delta in (7,9) and (start in white and target in black) or (start in black and target in white): #one diagonal move
        return True

# legal bishop movements
def bishop_move(start, target):
    delta = abs(target - start)
    if delta % 7 == 0 or delta % 9 == 0:                                #diagonal movements
        return True 

# fork into collision patterns of diferent pieces
def collision_detection(piece, start, target):
    if piece == "\u2656" or piece == "\u265C":
        return rook_collision(start, target)
    if piece == "\u2658" or piece == "\u265E":
        return knight_collision(start, target)
    if piece == "\u2657" or piece == "\u265D":
        return bishop_collision(start, target)
    if piece == "\u2655" or piece == "\u265B":
        return queen_collision(start, target)
    if piece == "\u2654" or piece == "\u265A":
        return king_collision(start, target)
    if piece == "\u2659" or piece == "\u265F":
        return pawn_collision(start, target)


def rook_collision(start, target):
    ...
def knight_collision(start, target):
    ...
def king_collision(start, target):
    ...
def queen_collision(start, target):
    ...
def bishop_collision(start, target):
    ...
def pawn_collision(start, target):
    ...

white = "\u265F","\u265C","\u265E","\u265D","\u265B","\u265A"
black = "\u2656","\u2658","\u2657","\u2655","\u2654","\u2659"

turn()
