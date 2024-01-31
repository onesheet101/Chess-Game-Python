from tkinter import *
from PIL import Image, ImageTk


class Chessboard:
    pieceImages = {"bb": r'C:\Users\narut\PycharmProjects\Chess\pieces\blackBishop.png',
                   "bk": r'C:\Users\narut\PycharmProjects\Chess\pieces\blackKing.png',
                   "bkn": r'C:\Users\narut\PycharmProjects\Chess\pieces\blackKnight.png',
                   "bp": r'C:\Users\narut\PycharmProjects\Chess\pieces\blackPawn.png',
                   "bq": r'C:\Users\narut\PycharmProjects\Chess\pieces\blackQueen.png',
                   "br": r'C:\Users\narut\PycharmProjects\Chess\pieces\blackRook.png',
                   "wb": r'C:\Users\narut\PycharmProjects\Chess\pieces\whiteBishop.png',
                   "wk": r'C:\Users\narut\PycharmProjects\Chess\pieces\whiteKing.png',
                   "wkn": r'C:\Users\narut\PycharmProjects\Chess\pieces\whiteKnight.png',
                   "wp": r'C:\Users\narut\PycharmProjects\Chess\pieces\whitePawn.png',
                   "wq": r'C:\Users\narut\PycharmProjects\Chess\pieces\whiteQueen.png',
                   "wr": r'C:\Users\narut\PycharmProjects\Chess\pieces\whiteRook.png'}

    boardCoords = {1: 0, 2: 90, 3: 180, 4: 270, 5: 360, 6: 450, 7: 540, 8: 630}

    def __init__(self, x, y, myCanvas):
        self.x = x
        self.y = y
        self.myCanvas = myCanvas
        self.image_references = {}
        self.coord_ref = {}

    def draw_board(self):
        for i in range(0, self.y):
            y1 = 0
            y2 = 90
            y1 += i * 90
            y2 += i * 90
            for k in range(0, self.x):
                x1 = 0 if i % 2 == 0 else 90
                x2 = 90 if i % 2 == 0 else 180
                x1 += k * 180
                x2 += k * 180
                print(f'x1: {x1} y1: {y1} x2: {x2} y2: {y2}')
                self.myCanvas.create_rectangle(x1, y1, x2, y2, fill="white", width=0)

    def place_piece(self, piece, x, y):
        img = Image.open(self.pieceImages.get(piece)).resize((90, 90))
        photo = ImageTk.PhotoImage(img)
        self.image_references[(x, y)] = photo
        ref = self.myCanvas.create_image(self.boardCoords.get(x), self.boardCoords.get(y), anchor="nw", image=photo, tags="testing")
        self.coord_ref[(x, y)] = ref
        return ref

    def remove_piece(self, x, y):
        self.myCanvas.delete(self.coord_ref.get((x, y)))





