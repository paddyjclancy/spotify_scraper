# This build analyses two Spotify playlists, see playlists_like_dislike.json for URIs:
#       1) Travelling Man (3h6Yw25svhWj5GZvRVGVW0)
from time import sleep

import inline
import matplotlib
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

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

# Getting information of tracks in Spotify playlist
#    URI is split by ':' to get the username and playlist ID
uri = playlist_uri
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]
playlist_title = uri.split(':')[3]
playlist_title_format = str(playlist_title.lower().replace(' ', '_'))

results = sp.user_playlist(username, playlist_id, 'tracks')

# Fetching details of the track like ID’s, Titles and Artists
playlist_tracks_data = results['tracks']
playlist_tracks_id = []
playlist_tracks_titles = []
playlist_tracks_artists = []
playlist_tracks_first_artists = []

# Going over each track of a playlist and adding the track Id, name and artist information to the dataframe of tracks
for track in playlist_tracks_data['items']:
    playlist_tracks_id.append(track['track']['id'])
    playlist_tracks_titles.append(track['track']['name'])
    # Adds a list of all artists involved in the song to the list of artists for the playlist
    artist_list = []
    for artist in track['track']['artists']:
        artist_list.append(artist['name'])
    playlist_tracks_artists.append(artist_list)
    playlist_tracks_first_artists.append(artist_list[0])


# Extracting Audio Features of each track
features = sp.audio_features(playlist_tracks_id)
features_df = pd.DataFrame(data=features, columns=features[0].keys())


# Merging Dataframe with Title / Artist info
features_df['title'] = playlist_tracks_titles
features_df['first_artist'] = playlist_tracks_first_artists
features_df['all_artists'] = playlist_tracks_artists
# features_df = features_df.set_index('id')
features_df = features_df[['id', 'title', 'first_artist', 'all_artists',
                           'danceability', 'energy', 'key', 'loudness',
                           'mode', 'acousticness', 'instrumentalness',
                           'liveness', 'valence', 'tempo',
                           'duration_ms', 'time_signature']]
features_df.tail()

# Data Exploration
# Artist graph
plt.figure(figsize=(12, 12))
sns.countplot(features_df['first_artist'])
plt.xticks(rotation=90)
plt.xlabel('Leading Artist')
plt.ylabel('Appearances in Playlist')

print(f"Analysing playlist: {playlist_title}...")

plt.savefig("output/" + playlist_title_format + "_artists.png")
print("     - Artists")

# Valence graph
plt.figure(figsize=(9,4))
sns.lineplot(x=features_df['id'], y=features_df['valence'])
plt.xticks([])
plt.xlabel(playlist_title)
plt.ylabel('Mood Score')

plt.savefig("output/" + playlist_title_format + "_valence.png")
print("     - Valence")

# Valence graph
plt.figure(figsize=(9,4))
sns.lineplot(x=features_df['id'], y=features_df['energy'])
plt.xticks([])
plt.xlabel(playlist_title)
plt.ylabel('Energy Level Score')

plt.savefig("output/" + playlist_title_format + "_energy.png")
print("     - Energy")

# Track demographic graphs
num_bars = []
num_sections = []
num_segments = []

for i in range(0,len(features_df['id'])):
    analysis = sp.audio_analysis(features_df.iloc[i]['id'])
    num_bars.append(len(analysis['bars'])) # beats/time_signature
    num_sections.append(len(analysis['sections']))
    num_segments.append(len(analysis['segments']))

# Plotting figs
plt.figure(figsize=(16,4))
plt.subplot(1,3,1)
plt.hist(num_bars, bins=20)
plt.xlabel('Number of Bars')

plt.subplot(1,3,2)
plt.hist(num_sections, bins=20)
plt.xlabel('Number of Sections')

plt.subplot(1,3,3)
plt.hist(num_segments, bins=20)
plt.xlabel('Number of Segments')

features_df['num_bars'] = num_bars
features_df['num_sections'] = num_sections
features_df['num_segments'] = num_segments
features_df.head()

# Creating and naming CSV and _figs.PNG
features_df.to_csv("output/" + playlist_title_format + ".csv", encoding='utf-8',index="false")
print("     - Backend Data")

plt.savefig("output/" + playlist_title_format + "_figs.png")
print("     - Technical structure")
sleep(0.5)
print("\nAnalysis complete.")
sleep(0.5)
print(f"See output/{playlist_title_format}_ for visual analysis aids.")