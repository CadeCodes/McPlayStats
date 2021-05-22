import requests
import json

def processingTime(token):
    statRequest = requests.get(url = "https://mcplayhd.net/api/?token=" + token)
    debugJson = statRequest.json()
    p_time = debugJson["processingTime"]
    return p_time;
def is_auth(token):
    statRequest = requests.get(url = "https://mcplayhd.net/api/?token=" + token)
    debugJson = statRequest.json()
    data = debugJson["data"]
    auth_status = data["authenticated"]
    return auth_status;
def rate_limit(token):
    statRequest = requests.get(url = "https://mcplayhd.net/api/?token=" + token)
    debugJson = statRequest.json()
    data = debugJson["data"]
    user = data["user"]
    r_limit = user["rateLimit"]
    return r_limit;
