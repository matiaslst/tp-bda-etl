import os
import requests
import base64
from dotenv import load_dotenv

class SpotifyAuthenticator:

    def __init__(self):
        try:
            load_dotenv('../../.env')
        except:
            print("WARNING - .env file not found")
        self.CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
        self.CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]



    def __get_auth_string(self):
        auth_string = f"{self.CLIENT_ID}:{self.CLIENT_SECRET}"
        return base64.b64encode(auth_string.encode()).decode()
    

    def get_token(self):

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": f"Basic {self.__get_auth_string()}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials"
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            token = response.json().get("access_token")
        else:
            print("Error:", response.status_code)
            print(response.json())

        return token