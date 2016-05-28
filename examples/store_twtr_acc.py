import twitter
import sqlite3


acc = twitter.BasketballTwitterMatch()
acc.gen_player_twitters()
data = [(None, name, handle) for name, handle in acc.players_.iteritems()]

DB_PATH = 'twtr.db'
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute('CREATE TABLE twitteraccounts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, handle TEXT)')
cursor.executemany('INSERT INTO twitteraccounts VALUES (?,?,?)', data)
conn.commit()
conn.close()
