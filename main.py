from user import User
from song import Song

dyana = User("Dyana")
gym = dyana.create_playlist("Gym Playlist")
gym.add_song(Song("Kannathil muthamittal", "Artist 1", "3:45"))
gym.add_song(Song("Kannae Kalaimanae", "Artist 2", "4:10"))
melody = dyana.create_playlist("Melodies Playlist")
melody.add_song(Song("A", "Artist 3", "3:20"))
melody.add_song(Song("B", "Artist 4", "3:50"))
dyana.show_playlists()


gym.show()
melody.show()
