import requests
import json

def fb_leaderboard(gamemode,position,token):
    """
    Get A Leaderboard Position's Player Name and Time, returns a string with the info.
    """
    statRequest = requests.get(url = "https://mcplayhd.net/api/fastbuilder/" + gamemode + "/top/" + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    top = data["top"]
    postion = stats[position]
    p_info = postion["playerInfo"]
    p_stat = postion["stats"]
    p_name = p_info["name"]
    lb_time = p_stat["timeBest"]
    return "Name: " + p_name + ", Time: " + lb_time;
def fb_stats_pb(gamemode,player_name,token):
    """
    Get A PB of a Player For A Certain Mode
    """
    statRequest = requests.get(url = "https://mcplayhd.net/api/fastbuilder/" + gamemode + "/stats/" + player_name + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    stats = data["stats"]
    bestTime = stats["timeBest"]
    return bestTime / 1000;
def fb_stats_avg(gamemode,player_name,token):
    """
    Get The Average Time of a Player For A Certain Mode
    """
    statRequest = requests.get(url = "https://mcplayhd.net/api/fastbuilder/" + gamemode + "/stats/" + player_name + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    stats = data["stats"]
    totalTime = stats["timeTotal"]
    wins = stats["wins"]
    return (totalTime / wins) / 1000;
def fb_stats_attempts(gamemode,player_name,token):
    """
    Get The Attempts of a Player For A Certain Mode
    """
    statRequest = requests.get(url = "https://mcplayhd.net/api/fastbuilder/" + gamemode + "/stats/" + player_name + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    stats = data["stats"]
    sconfirmed = stats["games"]
    return games;
def fb_stats_isVerified(gamemode,player_name,token):
    """
    See If A Player's Time Is Verfied For A Certain Mode
    """
    statRequest = requests.get(url = "https://mcplayhd.net/api/fastbuilder/" + gamemode + "/stats/" + player_name + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    stats = data["stats"]
    confirmed = stats["confirmed"]
    return confirmed;
def fb_stats_isSpeedrunVerified(gamemode,player_name,token):
    """
    See If A Player's Time Is Speedrun.com Verfied For A Certain Mode
    """
    statRequest = requests.get(url = "https://mcplayhd.net/api/fastbuilder/" + gamemode + "/stats/" + player_name + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    stats = data["stats"]
    sconfirmed = stats["speedrunConfirmed"]
    return sconfirmed;
