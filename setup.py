# This build analyses two Spotify playlists, see playlists_like_dislike.json for URIs:
#       1) Travelling Man (3h6Yw25svhWj5GZvRVGVW0)
#       2) The COVID Project (0HL8G71TzGQXOjo81WSP5j)


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import numpy as np
import pandas as pd


# Personal client credentials abstracted into 'authorization.json'
credentials = json.load(open('authorization.json'))
client_id = credentials['client_id']
client_secret = credentials['client_secret']

# Multiple playlists can be used in the single 'playlists_like_dislike.json' file
# Indexing is required and declared here:
playlist_index = 0

playlists = json.load(open('playlists_like_dislike.json'))
playlist_uri = playlists[playlist_index]['uri']
like = playlists[playlist_index]['like']

# Spotipy setup
client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# URI is split by ':' to get the username and playlist ID
uri = playlist_uri
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

results = sp.user_playlist(username, playlist_id, 'tracks')

playlist_tracks_data = results['tracks']
playlist_tracks_id = []
playlist_tracks_titles = []
playlist_tracks_artists = []
playlist_tracks_first_artists = []

for track in playlist_tracks_data['items']:
    playlist_tracks_id.append(track['track']['id'])
    playlist_tracks_titles.append(track['track']['name'])
    # Adds a list of all artists involved in the song to the list of artists for the playlist
    artist_list = []
    for artist in track['track']['artists']:
        artist_list.append(artist['name'])
    playlist_tracks_artists.append(artist_list)
    playlist_tracks_first_artists.append(artist_list[0])


features = sp.audio_features(playlist_tracks_id)
features_df = pd.DataFrame(data=features, columns=features[0].keys())
