import random
import webscrape
import webbrowser
import time



def choose_episode():

    random_episode = random.choice(list(webscrape.episode_.items()))
    random_episode_name, random_episode_link = random_episode

    print(random_episode_name + "\n" + random_episode_link)
    ans = input("Bölümü izlemek istiyor musunuz?: Y/N")

    if ans == "N" or ans == "n":
        return "İyi günler dileriz.."

    elif ans == "Y" or ans == "y":
        print("Bölüm açılıyor..")
        time.sleep(0.6)
        webbrowser.open(random_episode_link)

    else:
        input("Lütfen Y veya N'ye basınız.")


choose_episode()


