from playlist import PlayList
class User:
    def __init__(self, name):
        self.name = name
        self.playlists = []

    def create_playlist(self, playlist_name):
        new_playlist = PlayList(playlist_name)
        self.playlists.append(new_playlist)
        return new_playlist

    def show_playlists(self):
        print(f"--- {self.name}'s playlists ---")
        for number, playlist in enumerate(self.playlists, start=1):
            print(f"{number}. {playlist}")
