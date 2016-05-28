import requests
from bs4 import BeautifulSoup


class BasketballTwitterMatch():
    def __init__(self):
        uri_base = 'http://www.basketball-reference.com/friv/twitter.cgi'
        rv = requests.get(uri_base)
        self.soup = BeautifulSoup(rv.text)

    def gen_player_twitters(self):
    	twitter_list = self.soup.find('div', {'id': 'div_stats'})
    	headers = [th.text for th in twitter_list.find_all('th')]
        rows = [row for row in twitter_list.tbody.find_all('tr')]

        self.players_ = {}
        for player in rows:
            player = [i.text for i in player.find_all('td')]
            player = dict(zip(headers, player))
            self.players_[player['Player']] = player['Twitter'].replace('@', '')
    