from src.extract import SpotifyExtractor
from src.transform import SpotifyTransformer
from src.load import SpotifyLoader
import pandas as pd

def main():

    extractor = SpotifyExtractor()
    transformer = SpotifyTransformer()
    
    server = '<SERVER>'
    database = '<DB>'
    username = '<USER>'
    password = '<PWD>'
    
    loader = SpotifyLoader(server, database, username, password)
    
    artist_data = extractor.get_artist("1Xyo4u8uXC1ZmMpatF05PJ")
    artist_df = transformer.json_to_dataframe(artist_data, data_type="artist")
    loader.load_to_sql(artist_df, table_name='Artists')

    album_data = extractor.get_album("4yP0hdKOZPNshxUOjY0cZj")
    album_df = transformer.json_to_dataframe(album_data, data_type="album")
    loader.load_to_sql(album_df, table_name='Albums')

    track_data = extractor.get_track("7MXVkk9YMctZqd1Srtv4MB")
    track_df = transformer.json_to_dataframe(track_data, data_type="track")
    loader.load_to_sql(track_df, table_name='Tracks')

if __name__ == "__main__":
    main()
