import chess

class Board():
    '''
    wrapper for python-chess API. Needed to validate chess moves, otherwise
    anything could be written in. Needs to check for checks and mates.
    >>> board = Board()
    >>> board.check_legality("a4")
    True
    >>> board.check_legality("a6")
    False
    >>> board.board.push_san("e4")
    Move.from_uci('e2e4')
    >>> board.board.push_san("e5")
    Move.from_uci('e7e5')
    >>> board.board.push_san("Qh5")
    Move.from_uci('d1h5')
    >>> board.board.push_san("Nc6")
    Move.from_uci('b8c6')
    >>> board.board.push_san("Bc4")
    Move.from_uci('f1c4')
    >>> board.board.push_san("Nf6")
    Move.from_uci('g8f6')
    >>> print(board.board)
    r . b q k b . r
    p p p p . p p p
    . . n . . n . .
    . . . . p . . Q
    . . B . P . . .
    . . . . . . . .
    P P P P . P P P
    R N B . K . N R
    >>> board.check_for_mate("Qxf7")
    True
    >>> print(board.board)
    r . b q k b . r
    p p p p . p p p
    . . n . . n . .
    . . . . p . . Q
    . . B . P . . .
    . . . . . . . .
    P P P P . P P P
    R N B . K . N R
    >>> board.check_for_check("Qxf7+")
    True
    >>> board.check_for_mate("Qxf7++")
    True

    '''

    def __init__(self):
        self.board = chess.Board()

    def clean(self, move : str):
        cleaned = move.replace("+", "")
        return cleaned

    def check_legality(self, move : str):
        try:
            uci_move = self.board.parse_san(self.clean(move))
        except:
            return False
        else:
            """
            probably likely to be a legal move but still
            good to check
            """
            return uci_move in self.board.legal_moves


    def check_for_check(self, move : str):

        temp_copy = self.board.copy()
        temp_copy.push_san(self.clean(move))
        return temp_copy.is_check()

    def check_for_mate(self, move : str):

        temp_copy = self.board.copy()
        temp_copy.push_san(self.clean(move))
        return temp_copy.is_checkmate()




