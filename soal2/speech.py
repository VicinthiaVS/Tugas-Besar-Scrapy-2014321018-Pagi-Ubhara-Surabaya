
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup as bs


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
}

DOMAIN = 'https://www.wavsource.com'
URL = 'https://www.wavsource.com/people/women1.htm'
FILETYPE = '.wav'

def get_soup(url):
    return bs (requests.get(url, headers=headers).text, 'html.parser')

for link in get_soup(URL).find_all('a'):
     wav_link = link.get('href')
     if FILETYPE in wav_link:
         print(wav_link)

# Saya menghadapi kendala pak, yang mana saya punya tujuan untuk mengambil data url file wav nya akan tetapi ketika dirun 
# code diatas itu dia tidak mengeluarkan output sama-sekali (apkah ada kesalahan pada code saya pak ? karena menurut saya 
# kodenya sudah benar






