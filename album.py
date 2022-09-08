from video import Video

class Album:

    def __init__(self, albumName: str, videosCount: int, videos: list[Video]):
        self.albumName = albumName
        self.videosCount = videosCount
        self.videos = videos

