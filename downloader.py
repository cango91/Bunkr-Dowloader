import os
import requests
from album import Album
from video import Video
from tqdm import *

class Downloader:

    def __init__(self):
        pass

    def downloadVideo(self, video: Video, albumName=""):
        url = video.getDownloadUrl()
        with requests.get(url, stream=True) as r :
            r.raise_for_status()
            curr_dir = os.path.dirname(__file__)
            if albumName != '':
                path = os.path.join(curr_dir, f"downloads/{albumName}") 
            else:
                path = os.path.join(curr_dir, "downloads/") 
            if not os.path.isdir(path):
                os.mkdir(path)
            with open(os.path.join(path, video.videoName), "wb") as f:
                pbar = tqdm(total=int(r.headers['Content-Length']), unit='B', unit_scale=True, unit_divisor=1024)
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))
                f.close()

    def downloadAlbum(self, album: Album):
        counter = 0
        for video in album.videos:
            counter += 1
            print(f"{counter}: \t {video}")
            self.downloadVideo(video, album.albumName)

    