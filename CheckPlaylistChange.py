import twitter
import spotipy


def check_playlist_edited(initial_playlist_snapshot_id: int, spotify_api: spotipy.Spotify, twitter_api: twitter.Api):
    print('In check playlist edited')
    initial_id = initial_playlist_snapshot_id

    playlist = spotify_api.user_playlist('glisto18', '1oH2OFIzRe5mssKmf8X4xm')
    current_id = playlist['snapshot_id']

    if initial_id != current_id:
        print('Playlist has changed.  Attempting to send tweet.')
        twitter_api.PostUpdate("@mmmchisholm @_tropolini No more, no less has been changed.")
        print('Tweet sent!')
        initial_playlist_snapshot_id = current_id
    else:
        print('Playlist has not changed')
