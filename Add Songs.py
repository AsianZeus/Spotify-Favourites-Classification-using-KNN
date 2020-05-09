import sys
import os
import spotipy
import pandas as pd
import spotipy.util as util
from pprint import pprint


def get_top_songs_for_artist(artist, song_count=1):
    song_ids = []
    artist_results = sp.search(q='artist:' + artist, type='artist', limit=1)
    # pprint(artist_results)

    if artist_results['artists']['total']:
        artist_id = artist_results['artists']['items'][0]['id']
        # pprint(artist_id)
        artist_top_tracks = sp.artist_top_tracks(artist_id)
        artist_top_tracks_length = len(artist_top_tracks['tracks'])

        for x in range(0, artist_top_tracks_length if song_count > artist_top_tracks_length else song_count ):
            song_ids.append(artist_top_tracks['tracks'][x]['id'])
            # pprint(artist_top_tracks['tracks'][x])
            print(str(len(song_ids)) + ' songs found - ' + artist)
    else:
        print('Artist not found - ' + artist)
    # pprint(song_ids)
    return song_ids

def get_wacken_tracks():
    excel_file1 = 'C://Users//akroc//Desktop/newtraindata.xlsx'
    songs = pd.read_excel(excel_file1)
    a= songs[songs['Favourite']=='y']
    ids=a.get('id').tolist()

    artists = [
        '2Cellos',
        'Acoustic Steel',
        'Act of Defiance',
        'Aephanemer',
        'Alestorm',
        'Xenoblight',
        'Zeal & Ardor']
    all_track_ids = []
    for i, current_artist in enumerate(artists):
        api_track_add_limit = 10
        top_song_limit_per_artist = 1
        top_artist_songs = get_top_songs_for_artist(current_artist, top_song_limit_per_artist)
        if len(top_artist_songs):
            all_track_ids.extend(top_artist_songs)
        if len(all_track_ids)+ top_song_limit_per_artist > api_track_add_limit or (i == len(artists)-1 and len(all_track_ids)):
                sp.user_playlist_add_tracks(username, playlist_id="4ODTjSw14wrqCaIzFl2qEC", tracks=ids[990:1089])
                all_track_ids = []


if __name__ == '__main__':
    
    cid = os.getenv('SPOTIPY_CLIENT_ID')    
    secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
    username = "21k2ivyu64ut7is76vxeknkdq"
    scope = 'user-library-read playlist-read-private'
    global sp
    token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public', client_id=cid, client_secret=secret, redirect_uri=redirect_uri)
    if token:
        sp = spotipy.Spotify(auth=token)
        get_wacken_tracks()
    