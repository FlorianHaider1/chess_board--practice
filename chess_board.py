# The idea is to code a chessboard in multiple ways:
# I) Using a single list, where the indices are a linear representation of a chess board
# II) Possibility to use two list as rows and colums.
#
# Chessboard is 8x8 => abcdefgh X 12345678
# white_king = '\u2654'
# white_queen = '\u2655'
# white_rook = '\u2656'
# white_bishop = '\u2657'
# white_knight = '\u2658'
# white_pawn = '\u2659'
# black_king = '\u265A'
# black_queen = '\u265B'
# black_rook = '\u265C'
# black_bishop = '\u265D'
# black_knight = '\u265E'
# black_pawn = '\u265F'
# Chessboard starts from A1 to H8, so lower left corner to upper right corner

from prettytable import PrettyTable

chessboard_reference = []
chessboard_actual = ["\u2656","\u2658","\u2657","\u2655","\u2654","\u2657","\u2658","\u2656",
                     "\u2659","\u2659","\u2659","\u2659","\u2659","\u2659","\u2659","\u2659",
                     "","","","","","","","",
                     "","","","","","","","",
                     "","","","","","","","",
                     "","","","","","","","",
                     "\u265F","\u265F","\u265F","\u265F","\u265F","\u265F","\u265F","\u265F",
                     "\u265C","\u265E","\u265D","\u265B","\u265A","\u265D","\u265E","\u265C"]

board = PrettyTable()
board.field_names = ["","A","B","C","D","E","F","G","H"]
board.add_row(["1"] + chessboard_actual[0:8:])
board.add_row(["2"] + chessboard_actual[8:16:])
board.add_row(["3"] + chessboard_actual[16:24:])
board.add_row(["4"] + chessboard_actual[24:32:])
board.add_row(["5"] + chessboard_actual[32:40:])
board.add_row(["6"] + chessboard_actual[40:48:])
board.add_row(["7"] + chessboard_actual[48:56:])
board.add_row(["8"] + chessboard_actual[56:65:])
print(board)