import requests
from bs4 import BeautifulSoup
import webbrowser

url = "https://en.wikipedia.org/wiki/Special:Random"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

title = soup.find(class_= "firstHeading").text
print("Would you like to read this article?: {}, Y/N".format(title))
ans = input("")
if ans == "Y" or ans == "y":
    url1 = "https://en.wikipedia.org/wiki/" + title
    webbrowser.open(url1)
if ans == "n" or "N":
    print("Have a good day!")
else:
    print("have a good day!")