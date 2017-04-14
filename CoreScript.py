import configparser, os, time, sys
from src.BaseInit import BaseInit

config = configparser.ConfigParser()
config.read('src/config.ini')
loop_menu = True

print('''
┌──────────────────────────────────────────────────┐
│                                                  │
│                CoreScript v{0}                   │
│                                                  │
└──────────────────────────────────────────────────┘'''.format(config.get("config", "version")))

while loop_menu:
	project_name = input("[{0}] Project name: ".format(time.strftime('%H:%M:%S')))
	if project_name == "":
		pass
	else:
		project_location = "projects/"+project_name
		if os.path.isdir(project_location):
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			with open("logs/latest_log.txt", "r") as Logger:
				print(Logger.read())
			BaseInit(project_name, project_location)
			
			time.sleep(1000000)
		else:
			print("[{0}] Project with name '{1}' not exist!".format(time.strftime('%H:%M:%S'), project_name))
input()
