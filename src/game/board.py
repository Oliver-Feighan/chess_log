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
    '''

    def __init__(self):
        self.board = chess.Board()

    def check_legality(self, move : str):
        try:
            uci_move = self.board.parse_san(move)
        except:
            return False
        else:
            """
            probably likely to be a legal move but still
            good to check
            """
            return uci_move in self.board.legal_moves

    def check_for_check(self, move : str):
        try:

