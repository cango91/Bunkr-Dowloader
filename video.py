def sizeReadable(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

class Video:

    def __init__(self, videoName, cdn, size):
        self.videoName = videoName
        self.cdn = cdn
        self.size = size
    
    def getUrl(self) -> str :
        return "{}/{}".format(self.cdn, self.videoName)

    def getDownloadUrl(self, replacement="media-files") -> str:
        return self.getUrl().replace("cdn", replacement)

    def __str__(self):
        return f"{self.getDownloadUrl()} -> \t\t {sizeReadable(self.size)}"
