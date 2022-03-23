from main import logger

import requests
from pprint import pprint

superhero_names = ["Hulk", "Captain America", "Thanos"]
superhero_list = []
TOKEN = '2619421814940190'
url = f'https://superheroapi.com/api/{TOKEN}/'


@logger
def search_hero():
    for name in superhero_names:
        search_url = f'https://superheroapi.com/api/{TOKEN}/search/{name}'
        resp = requests.get(search_url)
        hero_bio = resp.json()
        for key, value in hero_bio.items():
            if key == 'results':
                for items in value:
                    if items['name'] == name:
                        superhero_list.append({'id': items['id']})


@logger
def smartest_hero():
    search_hero()
    hero_stats = []
    for character in superhero_list:
        stats_url = f'https://superheroapi.com/api/{TOKEN}/{character["id"]}/powerstats'
        resp = requests.get(stats_url)
        hero_stats.append(resp.json())
    for hero in hero_stats:
        hero['intelligence'] = int(hero['intelligence'])
    hero_stats.sort(key=lambda hero_stats: int(hero_stats['intelligence']), reverse=True)
    smart_hero = hero_stats[0]
    return (f"Smartest hero is a {smart_hero['name']} with {smart_hero['intelligence']} intelligence!")


print(smartest_hero())


@logger
def summ(a, b):
    return a + b


print(summ(1, 6))
