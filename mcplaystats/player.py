import requests
import json

def rank(player_name,token):
    statRequest = requests.get(url = "https://mcplayhd.net/api/player/" + player_name + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    rank = data["group"]
    return rank;
