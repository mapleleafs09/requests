from pprint import pprint

import requests


from yadisc import YandexDisk

TOKEN = ""
TOKEN_HERO = "2619421814940190"

def hero_request_id(name_list):
    hero_intelligence_dict = {}
    for name in name_list:
        url = f'https://superheroapi.com/api/{TOKEN_HERO}/search/{name}'
        response = requests.get(url)

        for intelligence in response.json()["results"]:
            if intelligence["name"] == name:
                hero_intelligence = intelligence["powerstats"]["intelligence"]
                print(f"{name} intelligence = {hero_intelligence}")
                hero_intelligence_dict[name] = hero_intelligence

    sorted(hero_intelligence_dict, reverse=True)
    print(f'Самый умный супергерой - {sorted(hero_intelligence_dict, reverse=True)[0]}')
if __name__ == '__main__':

    hero_list = ["Hulk", "Captain America", "Thanos"]
    hero_request_id(hero_list)

    ya = YandexDisk(TOKEN)
    # # ya._get_upload_link('\ ')
    ya.upload_file_to_disk("/Users/boksha/Desktop/NHL-Pittsburgh-Penguins-baseball-cap.jpeg")
