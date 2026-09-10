class Song:


    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist    
        self.duration = duration

    def __repr__(self):
        return f"{self.title} by {self.artist} ({self.duration})"

    def __eq__(self, other):
        if isinstance(other, Song):
            return self.title == other.title and self.artist == other.artist and self.duration == other.duration
        return False

    