import lyricsgenius
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import os
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from textblob import TextBlob

cid = os.getenv('SPOTIPY_CLIENT_ID')
secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
username = "21k2ivyu64ut7is76vxeknkdq"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private'

token = util.prompt_for_user_token(username=username,scope=scope,client_id=cid,client_secret=secret,redirect_uri=redirect_uri)
spotify = spotipy.Spotify(auth=token)

genius = lyricsgenius.Genius("7YUAyHUaYyHelUqAtgqET1OLr66wTxAO5wESTsjk9we0tzDQFh2TnvBoKcOTYLV4")

sourcePlaylist = sp.user_playlist(cid, "3OAvr4wTFE19gT9xQvQHv6")
tracks = sourcePlaylist["tracks"]
songs = tracks["items"] 

while tracks['next']:
    tracks = sp.next(tracks)
    for item in tracks["items"]:
        songs.append(item)

song_name=[]
artist_name=[]
lyrics=[]
print(len(songs))

for i in range(len(songs)):
    song_name.append(songs[i]['track']['name'])
    artist_name.append([x['name'] for x in songs[i]['track']['artists']])

for i in range(len(songs)):
    print(song_name[i],artist_name[i])

for i in range(len(songs)):
    song = genius.search_song(song_name[i], artist_name[i][0])
    if(song==None):
        lyrics.append("")
    else:
        lyrics.append(song.lyrics)

polarity=[]

for x in range(len(songs)):
    if(lyrics[x]!=""):
        sentence=lyrics[x].split("\n")
        csent=""
        for i in sentence:
            if(not i.startswith("[")):
                csent=csent+" "+i
        blob = TextBlob(csent)
        polarity.append(blob.sentiment.polarity)    
    else:
        polarity.append(0)
print(polarity)

features = []
for i in range(len(songs)):
    audio_features = sp.audio_features(songs[i]['track']['id'])
    for track in audio_features:
        features.append(track)
        features[-1]['target'] = 1
trainingData = pd.DataFrame(features)
trainingData.insert(0, "Name", pd.Series(song_name))
trainingData=trainingData.drop(['mode','type','uri','target','duration_ms','track_href','analysis_url','time_signature'], axis=1)
trainingData.insert(11, "Polarity", polarity)
trainingData.insert(13,"Artists",artist_name)
trainingData.to_excel("C://Users//akroc//Desktop//trainingdatanew.xlsx")