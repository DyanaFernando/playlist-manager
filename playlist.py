import random
class PlayList:


    def __init__(self, name, songs = None):
        self.name = name
        if songs is None:
            songs = []
        self.songs = songs

    def add_song(self, song):
        if self.has_song(song):
            return False
        self.songs.append(song)
        return True

    def delete_song(self, song):
        if self.has_song(song):
            self.songs.remove(song)
            return True
        return False

    def __repr__(self):
        count = len(self)
        if count == 1:
            word = "song"
        else:
            word = "songs"
        return f"{self.name} has {count} {word}"

    def show(self):
        if len(self) == 0:
            print("Empty playlist")
            return
        print(f"--- {self.name}'s songs---")
        for number, song in enumerate(self.songs, start=1):
            print(f"{number}. {song}")

    def clear_playlist(self):
        self.songs.clear()

    def shuffle(self):
        random.shuffle(self.songs)

    def play_next(self):
        if len(self) == 0:
            return None
        return self.songs.pop(0)

    def __len__(self):
        return len(self.songs)

    def has_song(self, song):
        return song in self.songs

    def move_song(self, song, new_position):
        if not self.has_song(song):
            return False
        if new_position < 0 or new_position >= len(self):
            return False
        self.songs.remove(song)
        self.songs.insert(new_position, song)
        return True
            
            