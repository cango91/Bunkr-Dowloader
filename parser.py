import requests
from bs4 import BeautifulSoup
import json
from album import Album
from video import Video

class Parser:
    
    def __init__(self, url):
        self.url = url

    def getAlbum(self) -> Album:
        html = requests.get(self.url)
        if html.status_code != 200 :
            print(f"Error: Status code {html.status_code}")
            return

        soup = BeautifulSoup(html.content, 'html.parser')
        element = soup.select_one("script#__NEXT_DATA__")

        obj = json.loads(element.contents[0])

        files = obj['props']['pageProps']['album']['files']
        name = obj['props']['pageProps']['album']['name']

        videos = []

        for el in files :
            size = int(float(el['size']))
            video = Video(el['name'], el['cdn'], size)
            videos.append(video)

        videos.sort(key=lambda x: x.size, reverse=True)

        album = Album(name, len(videos), videos)

        return album
