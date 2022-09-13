import os
import requests
from tqdm import *

from video import Video

def resumeDownload(url, name, albumName=""):
    curr_dir = os.path.dirname(__file__)
    if albumName != '':
        path = os.path.join(curr_dir, f"downloads/{albumName}") 
    else:
        path = os.path.join(curr_dir, "downloads/") 
    if not os.path.isdir(path):
        os.mkdir(path)
    filePath = os.path.join(path, name)
    resumeBytePos = os.path.getsize(filePath)
    resume_header = {'Range': 'bytes=%d-' % resumeBytePos}
    with requests.get(url, headers=resume_header, stream=True,  verify=False, allow_redirects=True) as r :
        r.raise_for_status()
        with open(filePath, 'ab') as f:
            pbar = tqdm(total=int(r.headers['Content-Length']), unit='B', unit_scale=True, unit_divisor=1024)
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
            f.close()


if __name__ == "__main__" :
    resumeDownload("https://media-files.bunkr.is/2021-04-23,22-58.mp4-7gLxGEhM.mp4",  "2021-04-23,22-58.mp4-7gLxGEhM.mp4", "VixenVirago")