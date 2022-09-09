import sys
from parser import Parser
from downloader import Downloader

def main(url: str):

    print(url)
    
    parser = Parser(url)
    album = parser.getAlbum()

    album.printAlbumsList()

    downloader = Downloader()
    downloader.downloadAlbum(album)
        
    print()

if __name__ == '__main__' :
    args = sys.argv
    if len(args) == 1:
        print("Please provide the url:\n\tExample: python bunkr.py \"https://bunkr.is/a/xxxxxxxxx\"")
        exit(1)
    main(args[1])

