import pyttsx3
import requests
from bs4 import BeautifulSoup

def temp():
    url='https://www.google.co.in/search?source=hp&ei=AlgdWqqgHMf6vgTh7IPYBg&q=temperature&oq=tem&gs_l=psy-ab.3.0.35i39k1l2j0i131k1j0l7.1914.2097.0.3441.4.3.0.0.0.0.216.216.2-1.1.0....0...1.1.64.psy-ab..3.1.216.0...0.V9bOE-0TiP8'
    source_code=requests.get(url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text,"html.parser")
    for link in soup.findAll('span',attrs={'class':'wob_t'}):
        link=link.string
        break

    for second in soup.findAll('div',attrs={'class':'vk_c card section'}):
        print(1)

    print("The current temperature is "+ link)

    engine = pyttsx3.init()
    engine.say("The current temperature is " + link )
    engine.runAndWait()


temp()

