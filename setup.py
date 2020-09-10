import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

from spotify_scraper.secrets import client_id, client_secret


credentials = json.load(open('authorization.json'))


playlist_index = 0

playlists = json.load(open('playlists_like_dislike.json'))
playlist_uri = playlists[playlist_index]['uri']
like = playlists[playlist_index]['like']

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
