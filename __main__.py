import Authentication
import threading

initial_playlist_snapshot_id = 0
twitter_client = Authentication.get_twitter_api_client()
spotify_client = Authentication.get_spotify_api_client()


def main():
    global initial_playlist_snapshot_id
    playlist = spotify_client.user_playlist('username_here', 'playlist_id_here')
    initial_playlist_snapshot_id = playlist['snapshot_id']
    print('Created clients and retrieved initial playlist snapshot id.')

    check_playlist_edited()
    while True:
        pass


def check_playlist_edited():
    print('In check playlist edited')
    global initial_playlist_snapshot_id

    playlist = spotify_client.user_playlist('username_here', 'playlist_id_here')
    current_id = playlist['snapshot_id']

    if initial_playlist_snapshot_id != current_id:
        print('Playlist has changed.  Attempting to send tweet.')
        twitter_client.PostUpdate("@mmmchisholm @_tropolini @taythorn @ljay_6 No more, no less has been changed.")
        print('Tweet sent!')
        initial_playlist_snapshot_id = current_id
    else:
        print('Playlist has not changed')

    timer = threading.Timer(600, check_playlist_edited)
    timer.daemon = True
    timer.start()
    print('Started thread')


if __name__ == "__main__":
    main()
