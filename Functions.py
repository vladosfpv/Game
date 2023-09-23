from Settings import *

font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def add_player(name):
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM scores;")
    users = cursor.fetchall()
    f = False
    for user in users:
        if name == user[0]:
            f = True
    if not f:
        cursor.execute("INSERT INTO scores VALUES(?,?)", (name, 0))
    connection.commit()
    connection.close()


def set_score(name, score):
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM scores;")
    users = cursor.fetchall()
    f = False
    for user in users:
        if name == user[0]:
            if score > user[1]:
                f = True
    if f:
        cursor.execute("UPDATE scores SET score = ? WHERE player = ?", (score, name))
    connection.commit()
    connection.close()


def get_top_users():
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 5")
    users = cursor.fetchall()
    connection.commit()
    connection.close()
    return users


def create_db():
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    listoftables = cursor.execute(''' SELECT count(name) FROM sqlite_master
    WHERE type='table' AND name='scores' ''').fetchall()
    if listoftables == [(0,)]:
        cursor.execute('''CREATE TABLE IF NOT EXISTS scores (player TEXT, score INT)''')
    connection.commit()
    connection.close()


def table_update(table):
    i = 0
    top_players = get_top_users()
    for widget in table.get_widgets():
        widget.set_title(f"{top_players[i][0]} : {top_players[i][1]}")
        i += 1
        if len(top_players) == i:
            break
