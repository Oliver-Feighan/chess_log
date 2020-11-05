import src.recording.recording as logs
import src.game.board as game

def get_input(turn : int, player : str, board : game.Board):
    m_c = input("Turn: %s, Player: %s -- move and comment: " % (turn, player)).split(" ")

    if len(m_c) != 2 or len(m_c) != 1:
        print("only input move and comment, like 'b4 !!'")
        return get_input(turn, player, board)

    move, comment = m_c


    if not board.check_legality(move):
        print("this is not a legal move")
        return get_input(turn, player, board)

    if board.check_for_check(move) and move.count("+") != 1:
        print("incorrect notation for check - this will be fixed")
        move.replace("+", "")
        move += "+"
        print("move is now %s" % move)
        return (move, comment)

    if board.check_for_mate(move) and move.count("+") != 2:
        print("incorrect notation for checkmate - this will be fixed")
        move.replace("+", "")
        move += "++"
        print("move is now %s" % move)
        return (move, comment)


def print_title():
    print("#" * 15)
    print("# Chess Log #")
    print("#" * 15)
    print("\n")


def main():
    print_title()

    game_name = input("name of game?")

    # open connection to recording, and make a board
    this_game = logs.GameLog(game_name)
    this_board = game.Board()

    #loop through moves until checkmate or draw
    game_on = True
    turn = 1
    players = ["black", "white"]
    player = players[turn]
    while(game_on):
        [m, c] = get_input(turn, player, this_board)

        this_game.add_move(player, m, c)

        if "#" in m or "++" in m:
            game_on = False
            continue

        turn += 1
        player = players[turn % 2]

    print("%s wins in %s moves" % (player, str(turn)))

    this_game.conn.close()

if __name__ == '__main__':
    main()
    exit(0)