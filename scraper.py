import requests
import json
import lxml.html as html

leaderboards = [
    "https://fie.org/athletes"
]
data = {}


def get_page(url):
    return html.fromstring(requests.get(url).text)

def parse_fencer(obj, player_data){
    return
}