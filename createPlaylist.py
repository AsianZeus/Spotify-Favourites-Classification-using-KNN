import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import os
import spotipy
import pandas as pd

cid = os.getenv('SPOTIPY_CLIENT_ID')
secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
username = "21k2ivyu64ut7is76vxeknkdq"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-modify playlist-modify-public'

token = util.prompt_for_user_token(username=username,scope=scope,client_id=cid,client_secret=secret,redirect_uri=redirect_uri)
spotify = spotipy.Spotify(auth=token)

excel_file1 = 'C://Users//akroc//Desktop/newtraindata.xlsx'
songs = pd.read_excel(excel_file1)
a= songs[songs['Favourite']=='y']
ids=a.get('id').tolist()
print(ids[0])
res=spotify.user_playlist_add_tracks(username, "4ODTjSw14wrqCaIzFl2qEC", tracks=ids)
print(res)