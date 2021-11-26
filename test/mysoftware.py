import pyttsx3
import os

pyttsx3.speak("Hello! Welcome here")

print("******CHAT WITH ME******")

while True:
	print("WHAT CAN I DO FOR YOU: ", end = " ")
	x = input()
	if (("open" in x) or ("run" in x) or ("execute" in x)) and (("notepad" in x) or ("text" in x) or ("editor" in x)):
		os.system("notepad")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("chrome" in x) or ("google" in x)):
		os.system("chrome")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("paint" in x) or ("mspaint" in x) or ("drawing" in x) or ("draw" in x)):
		os.system("mspaint")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("word" in x) or ("msword" in x) or ("document" in x) or ("WINWORD" in x)):
		os.system("WINWORD")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("ppt" in x) or ("powerpoint" in x) or ("mspowerpoint" in x) or ("POWERPNT" in x) or ("pnt" in x)):
		os.sysem("POWERPNT")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("excel" in x) or ("sheet" in x) or ("msexcel" in x) or ("sheets" in x) or ("EXCEL" in x)):
		os.system("EXCEL")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("note" in x) or ("notes" in x) or ("onenote" in x) or ("one note" in x) or ("ONENOTE" in x)):
		os.system("ONENOTE")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and  (("wmplayer" in x) or ("media" in x) or ("player" in x) or ("music" in x) or ("songs" in x) or ("song" in x)):
		os.system("wmplayer")
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and (("control" in x) or ("panel" in x)):
		os.system("control panel")
	elif (("quit" in x) or ("stop" in x) or ("close" in x) or ("bye" in x) or ("exit" in x)):
		pyttsx3.speak("Bye, See you soon")
		break
	else:
		pyttsx3.speak("Sorry This Program is not Supported, Try something else.")

