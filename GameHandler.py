from Chessboard import Chessboard
from tkinter import *
from tkinter import ttk
from GamePiece import *

class GameHandler:

    def __init__(self):
        self.board_pieces = [["br", "bkn", "bb", "bq", "bk", "bb", "bkn", "br"],
                        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                        ["x", "x", "x", "x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x", "x", "x", "x"],
                        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                        ["wr", "wkn", "wb", "wq", "wk", "wb", "wkn", "wr"]]

        self.board_references = [[0] * 8 for _ in range(8)]

        self.points = {"r": 5, "kn": 3, "b": 3, "q": 9, "p": 1, "k": 100}

        self.classes = {"r": RGamePiece, "q": QGamePiece, "p": PGamePiece, "k": KGamePiece, "b": BGamePiece,
                   "kn": KnGamePiece}

        self.piece_buttons = {}
        # creates the root window
        self.root = Tk()
        # creates a frame with a grid as a child to root.
        # creates a frame with a grid as a child to root.
        self.frm = ttk.Frame(self.root, padding=50)
        self.frm.grid()
        # canvas child of frame, canvas allows me to draw things.
        self.myCanvas = Canvas(self.frm, width=718, height=718, bg="#E493AD", borderwidth=0)

        # Create a new instance of the chessboard class, tldr will actually create double as it only focuses on creating half the squares along the x axis so it is chequered.
        # Y is still the full length as it will colour half the squares FOR each row. So essentially if u have a 8 x 8 grid u put 4x8 or if it is 10 x 20 5x20
        self.cb = Chessboard(x=4, y=8, myCanvas=self.myCanvas)
        self.cb.draw_board()

        self.myCanvas.grid(row=0, column=0)
        self.setUpBoard()
        self.myCanvas.tag_bind('testing', '<ButtonPress-1>', self.piece_clicked)
        print(self.board_references)
        self.root.mainloop()


    def piece_clicked(self, event):
        ref = event.widget.find_withtag("current")
        x = self.piece_buttons.get(ref[0]).get_x()
        y = self.piece_buttons.get(ref[0]).get_y()
        self.remove_piece(x, y)


    def setUpBoard(self):
        for y in range(1, 9):
            for x in range(1, 9):
                if self.board_pieces[y-1][x-1] is not "x":
                    piece = self.board_pieces[y-1][x-1]
                    self.add_piece(piece, x, y)

    def add_piece(self, piece, x, y):
        self.board_pieces[y-1][x-1] = piece
        ref = self.cb.place_piece(piece, x, y)
        self.board_references[y-1][x-1] = ref
        self.piece_buttons[ref] = self.classes[piece[1:]](piece, x, y, self.points[piece[1:]])

    def remove_piece(self, x, y):
        ref = self.board_references[y-1][x-1]
        self.board_pieces[y-1][x-1] = "x"
        self.piece_buttons.pop(ref)
        self.myCanvas.delete(ref)
        self.board_references[y-1][x-1] = 0




