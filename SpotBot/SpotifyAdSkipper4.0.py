import json
import subprocess
import time
# import applescript
from json import JSONDecodeError
from subprocess import call
import keyboard
import os
from time import sleep
from threading import Thread
import osascript
import SpotifyAdDetector

class AdChecker():
    def playpause(self):
        pause = 1
        minimize = 1
        while True:
            if keyboard.is_pressed('b+n'):
                if pause == 1:
                    #print('pause')
                    subprocess.call(['osascript', '-e', 'tell application "Spotify" to pause'])
                    sleep(0.2)
                    pause = 0
                elif pause == 0:
                    #print('play')
                    subprocess.call(['osascript', '-e', 'tell application "Spotify" to play'])
                    sleep(0.2)
                    pause = 1
            if keyboard.is_pressed('v+b'):
                if minimize == 1:
                    os.system("open -a Spotify")
                    sleep(0.2)
                    minimize = 0
                elif minimize == 0:
                    keyboard.press('command+m')
                    sleep(0.2)
                    minimize = 1
    def check(self):
        # os.system("open -a Spotify")
        Thread(target=self.playpause).start()
        while True: #loop, check for error, which means either auth token broken or ad detected
            SpotifyAdDetector.main()
            try:
                if SpotifyAdDetector.AD_PLAYING:
                    os.system("pkill Spotify")
                    print('killed spotify')
                    sleep(0.3)
                    os.system("open -a Spotify")
                    print('opened spotify')
                    sleep(0.5)
                    keyboard.press('command+m')
                    print('minimized spotify')
                    sleep(0.3)
                    subprocess.call(['osascript', '-e', 'tell application "Spotify" to play'])
                    print('spotify to play')
                    sleep(2)
                    # sleep(0.5)
                    # keyboard.press('command+m')

            except Exception: #this is unnecessary
                print('Catch Error Please')


if __name__ == "__main__":
    a = AdChecker()
    a.check()
