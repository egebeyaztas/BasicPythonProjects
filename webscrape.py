import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://dizilla.net/dizi/friends/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")



episode_links = []
episode_names = []
episode_ = {}
#for ep in ep_link:
#    episode_links.append(ep.get("href"))
 #   episode_names.append(ep.get_text().strip())


#print(episode_links)
#print(episode_names)

for i in range(2,10):
    season = soup.find(id="season-"+ str(i) + "-episodes")

    ep_link = season.findAll("a", {"class":"hoverDarker text-white text-xbold text-small"})
    for ep in ep_link:

        episode_[ep.get_text().strip()] = ep.get("href")

#        episode_links.append(ep.get("href"))
#        episode_names.append(ep.get_text().strip())


