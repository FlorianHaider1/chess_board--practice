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
# queen can move freely diagonal and straigth. collision detection. does capture.
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
    board.add_row(["G"] + chessboard_actual[56:65:])
    print(board)

def turn():
    letter = str(input("Insert letter:\t"))
    number = int(input("Insert number:\t"))
    return convert_coordinate_index(letter, number)

def move():
    print("\nSelect figure field\n")
    start = turn()
    print("\nYou selected\t",chessboard_actual[start])
    print("\nSelect target field\n")
    target = turn()
    print("You moved ", chessboard_actual[start])
    chessboard_actual[target] = chessboard_actual[start]
    display()

def move_legality(piece):
    if piece == "\u2656" or if piece == "\u265C":
        rook_move()
    if piece == "\u2658" or if piece == "\u265E":
        knight_move()
    if piece == "\u2657" or if piece == "\u265D":
        bishop_move()
    if piece == "\u2655" or if piece == "\u265B":
        queen_move()
    if piece == "\u2654" or if piece == "\u265A":
        king_move()
    if piece == "\u2659" or if piece == "\u265F":
        pawn_move()

def knight_move():
    ...

def king_move():
    ...

def queen_move():
    ...

def pawn_move():
    ...

def rook_move():
    ...

def bishop_move():
    ...

def collision_detection():
    ...



move()
