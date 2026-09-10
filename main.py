from user import User
from song import Song

dyana = User("Dyana")
gym = dyana.create_playlist("Gym Playlist")
gym.add_song(Song("Kannathil muthamittal", "Artist 1", 245))
gym.add_song(Song("Kannae Kalaimanae", "Artist 2", 250))
melody = dyana.create_playlist("Melodies Playlist")
melody.add_song(Song("A", "Artist 3", 280))
melody.add_song(Song("B", "Artist 4", 225))
dyana.show_playlists()


gym.show()
melody.show()
print(f"Total duration of {gym.name}: {gym.total_duration()/60} minutes")
