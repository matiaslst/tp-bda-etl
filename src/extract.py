import requests
from src.auth_utils.api_auths import SpotifyAuthenticator


class SpotifyExtractor:
    
    def __init__(self):
        self.auth_token = SpotifyAuthenticator().get_token()
        self.BASE_URL = "https://api.spotify.com/v1/"

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.auth_token}"
        }

    def get_artist(self, artist_id):
        url = f"{self.BASE_URL}artists/{artist_id}"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            return response.json()
        else:
            print("Error: ", response.status_code, response.json())
            return None

    def get_album(self, album_id):
        url = f"{self.BASE_URL}albums/{album_id}"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            return response.json()
        else:
            print("Error: ", response.status_code, response.json())
            return None

    def get_track(self, track_id):
        url = f"{self.BASE_URL}tracks/{track_id}"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            return response.json()
        else:
            print("Error: ", response.status_code, response.json())
            return None

    def get_user(self, user_id):
        url = f"{self.BASE_URL}users/{user_id}"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            return response.json()
        else:
            print("Error: ", response.status_code, response.json())
            return None
        
    def get_playlist_tracks(self, playlist_id, limit=10):

        url = f"{self.BASE_URL}playlists/{playlist_id}/tracks"
        headers = self._get_headers()
        params = {
            "limit": limit
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error: ", response.status_code, response.json())
            return None

    def search(self, query, search_type="track", limit=10):

        url = f"{self.BASE_URL}search"
        params = {
            "q": query,
            "type": search_type,
            "limit": limit
        }
        response = requests.get(url, headers=self._get_headers(), params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print("Error: ", response.status_code, response.json())
            return None
