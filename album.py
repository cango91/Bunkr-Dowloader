from video import Video, sizeReadable

class Album:

    def __init__(self, albumName: str, videosCount: int, videos: list[Video]):
        self.albumName = albumName
        self.videosCount = videosCount
        self.videos = videos

    def printAlbumsList(self):
        print(f"Album Name: {self.albumName} (Total videos: {self.videosCount}) (TotlaSize: {sizeReadable(self.getAlbumTotalSize())})")
        print("-------------------------------------------------------------------------------------------------------------------------------")
        counter = 0
        for video in self.videos :
            counter += 1
            print(f"{counter}\t->\t{video.getDownloadUrl()}\t{sizeReadable(video.size)}")

    def getAlbumTotalSize(self):
        return sum(video.size for video in self.videos)