# The idea is to code a chessboard in multiple ways:
# I) Using a single list, where the indices are a linear representation of a chess board
# II) Possibility to use two list as rows and colums.
#
# Chessboard is 8x8 => abcdefgh X 12345678
# white_king = '\u2654'     white_queen = '\u2655'    white_rook = '\u2656'
# white_bishop = '\u2657'   white_knight = '\u2658'   white_pawn = '\u2659'
# black_king = '\u265A'     black_queen = '\u265B'    black_rook = '\u265C'
# black_bishop = '\u265D'   black_knight = '\u265E'   black_pawn = '\u265F'
# Chessboard starts from A1 to H8, so lower left corner to upper right corner
# bishop can move freely diagonal. collision detection. does capture.
# queen can move freely diagonal and straigth. collision detection. does capture.wwwwww
# king can move 1 field in every directon. collision detection. does capture.
# pawn can move 1 field up. collision detection, but does not capture. capture diagonal
# rook can move freely straigth. collision detection. does capture.
# knight special move, threatens 8 fields. no collision detection. captures only on those 8 fields.

from prettytable import PrettyTable

chessboard_reference = []
chessboard_start = ["\u2656","\u2658","\u2657","\u2655","\u2654","\u2657","\u2658","\u2656",
                     "\u2659","\u2659","\u2659","\u2659","\u2659","\u2659","\u2659","\u2659",
                     "","","","","","","","",
                     "","","","","","","","",
                     "","","","","","","","",
                     "","","","","","","","",
                     "\u265F","\u265F","\u265F","\u265F","\u265F","\u265F","\u265F","\u265F",
                     "\u265C","\u265E","\u265D","\u265B","\u265A","\u265D","\u265E","\u265C"]

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

def turn():
    letter = str(input("Insert letter:\t"))
    number = int(input("Insert number:\t"))
    return convert_coordinate_index(letter, number)

def move():
    display()
    print("\nSelect figure field\n")
    start = turn()
    piece_start = chessboard_actual[start]
    print("\nYou selected\t",piece_start)
    print("\nSelect target field\n")
    target = turn()
    piece_target = chessboard_actual[target]
    if move_legality(piece_start, start, target):
        if piece_start is black and piece_target is black or piece_start is white and piece_target is white:
            print("Move not valid. Please try again.")
        else:
            # collision_detection(piece, start, target)
            print ("You moved ", piece_start)
            chessboard_actual[target] = piece_start
            chessboard_actual[start] = ""
    else:
        print("Move not valid. Please try again.")
        move()
    move()

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

def rook_move(start, target):
    delta = abs(target - start)
    if delta %8 == 0:
        return True
    elif delta >= 1 - ((start//8)+1) and delta <= 8 - ((start//8)+1):
        return True 

def knight_move(start, target):
    delta = abs(target - start)
    if delta in (6, 10, 15, 17):
        return True

def king_move(start, target):
    delta = abs(target - start)
    if delta in (1, 8, 7, 9):
        return True

def queen_move(start, target):
    delta = abs(target - start)
    if delta %8 == 0:
        return True
    elif delta >= 1 - ((start//8)+1) and delta <= 8 - ((start//8)+1):
        return True 

def pawn_move(start, target):
    delta = abs(target - start)
    if delta == 8:
        return True
    elif delta in (7,9) and (start in white and target in black or start in black and target in white):
        return True

def bishop_move(start, target):
    delta = abs(target - start)
    if delta % 7 == 0 or delta % 9 == 0:
        return True 

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


# def rook_collision(start, target):
#     ...
        
# def knight_collision(start, target):
#         ...
# def king_collision(start, target):
#         ...
# def queen_collision(start, target):
#         ...
# def bishop_collision(start, target):
#         ...
# def pawn_collision(start, target):
#         ...

white = "\u265F","\u265C","\u265E","\u265D","\u265B","\u265A"
black = "\u2656","\u2658","\u2657","\u2655","\u2654","\u2659"

move()
