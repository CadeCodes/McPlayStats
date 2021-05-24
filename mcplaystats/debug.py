import requests
import json

def processing_time(token):
    stat_request = requests.get(url = "https://mcplayhd.net/api/?token=" + token)
    debug_json = stat_request.json()
    p_time = debug_json["processingTime"]
    return p_time;
def is_auth(token):
    stat_request = requests.get(url = "https://mcplayhd.net/api/?token=" + token)
    debug_json = stat_request.json()
    data = debug_json["data"]
    auth_status = data["authenticated"]
    return auth_status;
def rate_limit(token):
    stat_request = requests.get(url = "https://mcplayhd.net/api/?token=" + token)
    debug_json = stat_request.json()
    data = debug_json["data"]
    user = data["user"]
    r_limit = user["rateLimit"]
    return r_limit;
