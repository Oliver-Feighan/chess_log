import datetime
import sqlite3
import os

class GameLog:
    '''
    >>> import time
    >>> test_log = GameLog("test_table")

    >>> time.sleep(1)
    >>> test_log.add_move("white", "a4")

    >>> test_log.drop_game("test_table_0")

    >>> test_log.conn.close()

    '''

    def connect_to_db(self):
        assert(os.path.exists("chess_games_log.db"))
        return sqlite3.connect("chess_games_log.db")

    def make_new_table(self, table_name):
        '''
        take the current date and time and make a new table.

        Due to SQL injection attacks (probably not an issue here tbf)
        it is better to use parameter subsitution rather than using
        python string operations

        Turns out table names cannot use parameter substitution. Previous
        code left here for notes:

        start_time = (datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),)
        c = self.conn.cursor()

        c.execute("CREATE TABLE ? (move time comment)", start_time)


        Turns out using the date as the name of a table is also a bad
        idea.

        '''
        c = self.conn.cursor()

        if not table_name:
            game_no = c.execute("SELECT count(*) FROM sqlite_master WHERE type = 'table'")

            game_name = "game_%s" % game_no.fetchone()[0]
        else:
            all_games = c.execute("SELECT name FROM sqlite_master WHERE type = 'table'")

            all_similar_games = [x for x in all_games.fetchall() if table_name in x[0]]

            game_no = len(all_similar_games)

            game_name = "%s_%s" % (table_name, str(game_no))

        table_command = "CREATE TABLE %s (player text, move text, time text, comment text)" % game_name

        c.execute(table_command)

        self.conn.commit()

        return game_name


    def __init__(self, table_name = ""):
        self.date = datetime.datetime.today()
        self.conn = self.connect_to_db()

        self.game_name = self.make_new_table(table_name)


    def add_move(self, player, move_string, comment_string = "-",):
        allowed_comments = ["-", "!", "!!", "?", "??", "?!", "!?"]
        assert(comment_string in allowed_comments)

        time_diff = datetime.datetime.today() - self.date

        c = self.conn.cursor()

        parameters = (player, move_string, time_diff.seconds, comment_string)

        command = "INSERT INTO %s VALUES (?, ?, ?, ?)" % self.game_name

        c.execute(command, parameters)

        self.conn.commit()


    def drop_game(self, name : str):

        c = self.conn.cursor()

        command = "DROP TABLE %s" % name

        c.execute(command)

        self.conn.commit()
