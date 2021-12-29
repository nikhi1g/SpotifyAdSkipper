import subprocess
# from pynput.keyboard import Key, Controller
import atexit
import requests
import time
import os
from pprint import pprint
import keyboard
import pyautogui as p
from threading import Thread
from subprocess import call
from time import sleep
# import pyperclip as pyp

#link below
# https://developer.spotify.com/console/get-user-player/?market=&additional_types=

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
K = "Gonna Gonna Get My Key"#enter key here
ACCESS_TOKEN = K

t = True
f = False
keyon = t

SPOTIFYisON = False

# def onstartup():
#     print('Get_Key')
#     print(K)
#     os.system("open https://developer.spotify.com/console/get-user-player/?market=&additional_types=")
#     sleep(1.5)
#     p.moveTo(733,834,0.2)
#     p.click()
#     p.moveTo(463, 453,0.2)
#     p.click()
#     sleep(0.3)
#     p.scroll(-30)
#     p.moveTo(727, 829, 0.5)
#     p.click()
#     sleep(0.4)
#     p.moveTo(353, 829, 0.5)
#     p.mouseDown()
#     p.moveTo(860, 829, 0.5)
#     p.hotkey('command','x')
#     sleep(0.4)
#     p.hotkey('command', 'w')
#     sleep(0.5)
#     os.system("open -a PyCharm")
#     sleep(0.5)
#     s = pyp.paste()
#     global ACCESS_TOKEN
#     ACCESS_TOKEN = s
#     print("Get_Key_Complete","\n" + s)
#     sleep(1)
#     #KEY = input("Just Blank or Find Key: "), dont use this as it will just lead to wait errors

#don't abuse this too much or you will get ratelimited ;( or token limited, not sure which
def exit():
    os.system("pkill Spotify")
    # subprocess.call(['osascript', '-e', 'tell application "System Events" to sleep']) #useful sleep function


atexit.register(exit)  # quits spotify on exit


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

            # break

        time.sleep(1)


count = 0

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
        track_uri = json_resp['item']['uri']

        link = json_resp['item']['external_urls']['spotify']

        artist_names = ', '.join([artist['name'] for artist in artists])

        current_track_info = {
            "id": track_id,
            "track_name": track_name
            # "artists": artist_names,
            # "link": link
        }

        return current_track_info

    except Exception as e:
        print(e, 'in get_current_track')
        # global SPOTIFYisON
        # SPOTIFYisON = False
        close()
        open()
        play()
        time.sleep(0.4)#idk, maybe this will work. something with active focus?
        minimize()
        # SPOTIFYisON = True
        time.sleep(
            5)  # 5 seconds before main? maybe this will fix the error that Spotify notifies with, "The Application Spotify Quit Unexpectedly"
        main()


def close():
    os.system("pkill Spotify")
    # time.sleep(0.4)


def open():
    os.system("open -a Spotify")
    # while SPOTIFYisON == False:
    #     try:
    #         os.system("open -a Spotify")
    #     except Exception as e:
    #         print(e,"in Spotify open")
    #     time.sleep(0.2)


def play():
    subprocess.call(['osascript', '-e', 'tell application "Spotify" to play'])


def pause():
    subprocess.call(['osascript', '-e', 'tell application "Spotify" to pause'])


def minimize():
    time.sleep(0.3)
    keyboard.press('command+m')


# keyboardshortcuts

# def Keyboard_Update():
#     counter = 1
#     minimizecounter = 1
#     while True:
#         if keyboard.is_pressed('n+m'):
#             print('n+m pressed')
#             if counter == 1:
#                 subprocess.call(['osascript', '-e', 'tell application "Spotify" to pause'])
#                 counter = 0
#                 time.sleep(0.2)
#             elif counter == 0:
#                 subprocess.call(['osascript', '-e', 'tell application "Spotify" to play'])
#                 counter = 1
#                 time.sleep(0.2)
#         if keyboard.is_pressed('b+n'):
#             if minimizecounter == 1:
#                 os.system('open -a Spotify')
#                 minimizecounter = 0
#                 time.sleep(0.2)
#             elif minimizecounter == 0:
#                 keyboard.press('command+m')
#                 minimizecounter = 1
#                 time.sleep(0.2)


if __name__ == '__main__':
    # onstartup()
    main()
#HTTPSConnectionPool(host='api.spotify.com', port=443): Max retries exceeded with url: /v1/me/player/currently-playing (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x11fd28520>: Failed to establish a new connection: [Errno 60] Operation timed out')) in get_current_track
#what?&&^^
