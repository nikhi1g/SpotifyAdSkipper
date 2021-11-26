import subprocess
from pynput.keyboard import Key, Controller
import atexit
import requests
import time
import os
from pprint import pprint
import keyboard
from threading import Thread
from subprocess import call

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
KEY = 'BQCyH67q-aeGN6j1JwuzOF339gYMac0fj8jm24W68Vs11El4vFlIKjmmqzm10ZWBHVx_eoYw0IwKw0zAysarUZMWA-Ax0TohKFmf0mBEfVQzKNIR8zidpiNPAhjSof9Megb_Uj7OQNSxeWjjmMWYI62JtXwVWnANP8DbxmT_rNk2e8EXxwtf'
ACCESS_TOKEN = KEY

def exit():
    os.system("pkill Spotify")

atexit.register(exit)#quits spotify in exit

def get_current_track(access_token):
    try:
        response = requests.get(
            SPOTIFY_GET_CURRENT_TRACK_URL,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )
        json_resp = response.json()

        track_id = json_resp['item']['id']
        track_name = json_resp['item']['name']
        artists = [artist for artist in json_resp['item']['artists']]

        link = json_resp['item']['external_urls']['spotify']

        artist_names = ', '.join([artist['name'] for artist in artists])

        current_track_info = {
            "id": track_id,
            "track_name": track_name,
            "artists": artist_names,
            "link": link
        }

        return current_track_info

    except Exception as e:
        print(e, 'in get_current_track')
        close()
        open()
        play()
        minimize()
        time.sleep(1)
        main()




def main():
    current_track_id = None
    while True:
        current_track_info = get_current_track(ACCESS_TOKEN)

        try:
            if current_track_info['id'] != current_track_id:
                pprint(
                    current_track_info,
                    indent=40,
                )

                print(' ')
                current_track_id = current_track_info['id']
        except Exception as e:
            print(e, 'in main')
            main()
            #break

        time.sleep(1)


def close():
    os.system("pkill Spotify")
    #time.sleep(0.4)


def open():
    os.system("open -a Spotify")
    #time.sleep(0.4)


def play():
    subprocess.call(['osascript', '-e', 'tell application "Spotify" to play'])

def pause():
    subprocess.call(['osascript', '-e', 'tell application "Spotify" to pause'])

def minimize():
    time.sleep(0.3)
    keyboard.press('command+m')
if __name__ == '__main__':
    main()
