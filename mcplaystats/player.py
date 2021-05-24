import requests
import json

def rank(player_name,token):
    stat_request = requests.get(url = "https://mcplayhd.net/api/player/" + player_name + "/?token=" + token)
    stat_json = stat_request.json()
    data = stat_json["data"]
    rank = data["group"]
    return rank;
