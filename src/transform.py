import pandas as pd

class SpotifyTransformer:

    def __init__(self):
        pass

    def json_to_dataframe(self, json_data, data_type):

        if not json_data:
            print("JSON Empty")
            return pd.DataFrame()

        if data_type == 'artist':
            return self._transform_artist_to_dataframe(json_data)
        elif data_type == 'album':
            return self._transform_album_to_dataframe(json_data)
        elif data_type == 'track':
            return self._transform_track_to_dataframe(json_data)
        elif data_type == 'user':
            return self._transform_user_to_dataframe(json_data)
        elif data_type == 'search':
            return self._transform_search_to_dataframe(json_data)
        elif data_type == 'playlist':
            return self._transform_playlist_tracks(json_data)
        else:
            print("Tipo de dato no soportado")
            return pd.DataFrame()

    def _transform_artist_to_dataframe(self, artist_json):

        data = {
            'id': [artist_json.get('id')],
            'name': [artist_json.get('name')],
            'genres': [", ".join(artist_json.get('genres', []))],
            'popularity': [artist_json.get('popularity')],
            'followers': [artist_json['followers'].get('total')] if artist_json.get('followers') else [None]
        }
        return pd.DataFrame(data)

    def _transform_album_to_dataframe(self, album_json):

        data = {
            'id': [album_json.get('id')],
            'name': [album_json.get('name')],
            'release_date': [album_json.get('release_date')],
            'total_tracks': [album_json.get('total_tracks')],
            'popularity': [album_json.get('popularity')]
        }
        return pd.DataFrame(data)

    def _transform_track_to_dataframe(self, track_json):

        data = {
            'id': [track_json.get('id')],
            'name': [track_json.get('name')],
            'album_id': [track_json['album'].get('id')] if track_json.get('album') else [None],
            'duration_ms': [track_json.get('duration_ms')],
            'popularity': [track_json.get('popularity')]
        }
        return pd.DataFrame(data)

    def _transform_user_to_dataframe(self, user_json):

        data = {
            'id': [user_json.get('id')],
            'display_name': [user_json.get('display_name')],
            'followers': [user_json['followers'].get('total')] if user_json.get('followers') else [None],
            'country': [user_json.get('country')],
            'product': [user_json.get('product')]
        }
        return pd.DataFrame(data)

    def _transform_search_to_dataframe(self, search_json):

        results = []
        if 'tracks' in search_json:
            for track in search_json['tracks']['items']:
                results.append({
                    'type': 'track',
                    'id': track.get('id'),
                    'name': track.get('name'),
                    'popularity': track.get('popularity'),
                    'duration_ms': track.get('duration_ms')
                })
        elif 'artists' in search_json:
            for artist in search_json['artists']['items']:
                results.append({
                    'type': 'artist',
                    'id': artist.get('id'),
                    'name': artist.get('name'),
                    'popularity': artist.get('popularity'),
                    'genres': ", ".join(artist.get('genres', []))
                })
        elif 'albums' in search_json:
            for album in search_json['albums']['items']:
                results.append({
                    'type': 'album',
                    'id': album.get('id'),
                    'name': album.get('name'),
                    'release_date': album.get('release_date')
                })

        return pd.DataFrame(results)
    
    def _transform_playlist_tracks(self, playlist_json):
        track_list = []
        for item in playlist_json.get('items', []):
            track = item['track']
            track_data = {
                'track_id': track.get('id'),
                'track_name': track.get('name'),
                'album_name': track['album']['name'] if track.get('album') else None,
                'artist_names': ", ".join([artist['name'] for artist in track['artists']]),
                'popularity': track.get('popularity'),
                'duration_ms': track.get('duration_ms')
            }
            track_list.append(track_data)

        return pd.DataFrame(track_list)
