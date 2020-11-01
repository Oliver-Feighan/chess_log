import src.recording.recording as logs

def get_input(move, player):
    m_c = input("Move: %s, Player: %s -- move and comment: " % (move, player)).split(" ")

    try:
        assert(len(m_c) == 2 or len(m_c) == 1)
    except:
        print("only input move and comment, like 'b4 !!'")
        exit(1)
    else:
        if len(m_c) == 1:
            return [m_c[0], "-"]
        elif len(m_c) == 2:
            return m_c


def main():
    # open connection to recording
    this_game = logs.GameLog()

    #loop through moves until checkmate or draw
    game_on = True
    move = 1
    players = ["black", "white"]
    player = players[move]
    while(game_on):
        [m, c] = get_input(move, player)

        this_game.add_move(player, m, c)

        if "#" in m or "++" in m:
            game_on = False
            continue

        move += 1
        player = players[move % 2]

    print("%s wins in %s moves" % (player, str(move)))


if __name__ == '__main__':
    main()
    exit(0)