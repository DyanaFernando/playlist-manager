from user import User

dyana = User("Dyana")
gym = dyana.create_playlist("Gym Playlist")
gym.add_song("Kannathil muthamittal")
gym.add_song("Kannae Kalaimanae")
melody = dyana.create_playlist("Melodies Playlist")
melody.add_song("A")
melody.add_song("B")
dyana.show_playlists()

gym.show()
melody.show()
