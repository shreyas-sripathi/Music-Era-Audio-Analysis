import pandas as pd
import numpy as np
# Load datasets

alltime_top100 = pd.read_csv("/Users/shreyas/PycharmProjects/Spotify/Data/spotify_alltime_top100_songs.csv")
artists = pd.read_csv("/Users/shreyas/PycharmProjects/Spotify/Data/spotify_wrapped_2025_top50_artists.csv")
wrapped_2025 = pd.read_csv("/Users/shreyas/PycharmProjects/Spotify/Data/spotify_wrapped_2025_top50_songs.csv")

# Inspect structure
print("=== WRAPPED 2025 ===")
print(f"Shape: {wrapped_2025.shape}")
print(f"\nColumns:\n{wrapped_2025.columns.tolist()}")
print(f"\nFirst few rows:\n{wrapped_2025.head()}")
print(f"\nData types:\n{wrapped_2025.dtypes}")
print(f"\nMissing values:\n{wrapped_2025.isnull().sum()}")
print("=== ALLTIME TOP 100 ===")
print(alltime_top100.info())
print("\n" + alltime_top100.head(3).to_string())
print("\n=== ARTISTS ===")
print(artists.info())
print("\n" + artists.head(3).to_string())