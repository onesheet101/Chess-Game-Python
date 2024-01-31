class GamePiece:
    directions = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]

    def __init__(self, piece, x, y, points):
        self.piece = piece
        self.x = x
        self.y = y
        self.points = points

    def __str__(self):
        return f"{self.piece} {self.x} {self.y} {self.points} {self.__class__}"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class QGamePiece(GamePiece):

    def can_move(self):
        movable_tiles = []
        for i in range(0,8):
            temp_x = self.x + self.directions[i][0]
            temp_y = self.y + self.directions[i][1]
            while 8 >= temp_x >= 1 and 8 >= temp_y >= 1:
                movable_tiles.append([temp_x, temp_y])
                temp_x += self.directions[i][0]
                temp_y += self.directions[i][1]
        return movable_tiles


class KGamePiece(GamePiece):

    def can_move(self):
        movable_tiles = []
        for i in range(0,8):
            temp_x = self.x + self.directions[i][0]
            temp_y = self.y + self.directions[i][1]
            if 8 >= temp_x >= 1 and 8 >= temp_y >= 1:
                movable_tiles.append([temp_x, temp_y])
        return movable_tiles

class KnGamePiece(GamePiece):
    pass

class PGamePiece(GamePiece):
    pass

class BGamePiece(GamePiece):
    pass

class RGamePiece(GamePiece):
    pass