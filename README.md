# :notes: Spotify Scraper Project :musical_note:


This project aims to utilise a web API of _Spotify_ in order to scrape data from the platform.

The primary goal is to fetch all information relevant to tracks within **ANY** playlist provided.

This project allows access to some data Spotify usually doesn't show to the average consumer. There are quantified values for particular characteristics of almost every song - such as _danceability_, _energy_, and _liveness_. This additional data allows for the well known accuracies that Spotify algorithms produce for music listeners, and this utility can be applied in multiple directions.

With a tool such as this, we can gain significant insight into the listening habits of users. Whilst this is a personal project build - planned for practice and enjoyment - the scope for scrapers in general is vast. Outputted data may thus be applied in an array of sectors; from targeted marketing and advertising, to academic and medical research into more serious matters such as mental health in specific demographics.

###### NB: You can fetch data of up to 99 songs in a single connection session. If you will try to fetch information of more than this in a single session, then you will encounter an error and you will not be able to fetch the data, as per Spotify’s policy.


#### Tools / Dependencies

[Reference guide here](https://machinelearningknowledge.ai/tutorial-how-to-use-spotipy-api-to-scrape-spotify-data/#Data_Exploration)

- **Spotify for Developers** - Web API allowing for any developer to integrate Spotify content into their own web applications.
  - Upon logging in to the Dev API (with standard Spotify account details), an application can be created by filling out a simple form - acknowledging that monetization on this level is strictly forbidden.
  - Once created, the app will be assigned a **Client ID** and **Client Secret**

- **Spotipy** - Lightweight Python library for the Spotify Web API. With Spotipy you get full access to all of the music data provided by the Spotify platform.


## Current Status


~~**1)** More pseudocode required for personal clarity~~

**2)** When running the _setup.py_ file, a CSV file is created with all collated data relating to the FIRST ONLY playlist URI provided within _playlists_like_dislike.json_.
  - Need to incorporate For Loop in order to make multiple CSV files.
  - Final lines of _setup.py_

**3)** Visual aids? Histograms, bar charts etc...
  - ~~Code creates these, would be appealing to present~~
    - **Error found to be due to '%matplotlib inline' being of incorrect format for PyCharm - Now fixed - 18/09**
  - More exploration with graphical data - give it a stronger sense of purpose / insight
    - Mode, valance, key
    - Valence, energy, tempo


  - **Available track analytics:**
    - _mode:_ maj = 1. min = 0
    - _key_
    - _valence:_ general positivity
    - _loudness_
    - _danceability_
    - _energy_
    - _acousticness_
    - _instrumentalness_
    - _liveness_
    - _tempo_
    - _time_signature_


**4)** Like / Dislike element has been somewhat lost, find out what caused this abstraction

### Future Improvements

- Lyrics
- Songwriters
- Producers
- Label
- Geographical data, _eg_ place of
- Trends
