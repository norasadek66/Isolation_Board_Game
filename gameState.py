class GameState:
    """
    Attributes
    ----------
    """

    def __init__(self):
        self._board = [[0] * 3 for _ in range(2)]
        self._board[-1][-1] = 1
        self._players_locations = [None, None]
        self._takeTurn = 0  # player 1 => 0, Player 2 => 1
        pass

