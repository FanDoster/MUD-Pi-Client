import requests
import json
from pprint import pprint


root = 'http://7b0174a0.ngrok.io'
players = '/players'

def createPlayer():
	url = root + players

	name = input('what is your name?')
	hometown = input('where do youc come from?')

	payload = {'name':name, 'hometown':hometown}
	r = requests.put(url, data=payload)
	print(r)

def listPlayers():
	print('Getting player list!')
	url = root + players
	r = requests.get(url)
	pprint(r.json())
	

userInput = input('Do you want to create a user? Y/N')
if userInput.lower() == 'y':
	createPlayer()
listPlayers()