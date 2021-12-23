import keyboard
import os


Looping = True


while True:
	if Looping:
		if keyboard.is_pressed('m+n'):
			os.system("open -a spotify")
		elif keyboard.is_pressed('b+n'):
			keyboard.press('command+m')

