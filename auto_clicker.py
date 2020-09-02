from pyautogui import click
from time import sleep
import keyboard

def main():
	key = 'q'
	times = 10

	while True:
		if keyboard.is_pressed(key):
			print('You Pressed A Key!')
			[click() for i in range(times)]
		else:
			sleep(0.01)


if __name__=='__main__':
	main()
