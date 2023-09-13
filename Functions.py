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
    top_users = []
    top_user = ["", 0]
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM scores;")
    users = cursor.fetchall()
    if len(users) >= 5:
        for i in range(5):
            for user in users:
                if user[1] >= top_user[1]:
                    top_user = user
            top_users.append(top_user)
            users.remove(top_user)
            top_user = ["", 0]
    else:
        top_users = users
    connection.commit()
    connection.close()
    return top_users
