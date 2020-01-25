import requests

def api_info(xapi_key):

    info = []
    url = "https://developers.zomato.com/api/v2.1/search?entity_id=4&entity_type=city&q=mumbai&start=80"
    header = {"Accept": "application/json", "user-key": xapi_key, "User-agent": "curl/7.43.0"}
    resp = requests.get(url, headers=header).json()
    for i in range(0, 20):
        rest = resp['restaurants'][i]
        res_id = rest['restaurant']['id']
        name = rest['restaurant']['name']
        locality = rest['restaurant']['location']['locality']
        cuisines = rest['restaurant']['cuisines']
        average_cost_for_two = rest['restaurant']['average_cost_for_two']
        rating = rest['restaurant']['user_rating']['aggregate_rating']
        votes = rest['restaurant']['user_rating']['votes']
        list_ = [res_id, name, locality, cuisines, average_cost_for_two, rating, votes]
        info.append(list_)
    return info
