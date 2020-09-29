#Welcome to my docker assistant
#Written by Pulkit Vaish
#This is the client sided program (meaning could be distributed among clients).

"""
Advantage of using client sided program:
1. Dynamic updation of currently available OS Images.
2. Option of deleting user created os.
3. Option to pull images from docker hub if image not available locally on server.(provides user more flexibility)
4. More more interactive than the server sided program..

Disadvantage of using client sided program:
1. Manipulation prone(code can be misused)
2. Excessive piling of images on server..
3. Invalide images could get piled up causing the server to slow down!
"""

import webbrowser					#To provide links to various html pages.
import time							#To create pauses at specific turns in the program.
import os							#Give Docker Assistant wings..
import pyttsx3						#To bring Docker Assistant to life.	
import speech_recognition as sr		#To be able to listen and process speech.
voiceEngine = pyttsx3.init()		#change voice and speech rate of Docker Assistant
done=i=0							#looping constraints
oslist=[-1]							#container names remembered during runtime and reminded during exit.
vrgn=0								#meeting assistant for the first time
stop1=0								#cannot close containers if u never started any...
newosn=[-1,-1,-1]					#updates names of OS Images and included names of images pulled during lifetime of the program.
newosv=[-1,-1,-1]					#updates version of OS Images and included version of images pulled during lifetime of the program.
other=len(newosn)+1					#updates option number of "Other OS Image" when new images downloaded by user..
nos = len(oslist)-1					#helps in closing OS launched in this session
curi=[-1]							#image names used for each os
cur =[-1]							#os + image name
help=0								#Help user incase it receives more than 2 tries

#setting up voice recognition feature
r=sr.Recognizer()


newVoiceRate=170#Rate of speaking words has been decremented.
voiceEngine.setProperty('rate', newVoiceRate)
voice_id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
voice_id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
voiceEngine.setProperty('voice', voice_id2)

print("_________________________________________________________________________________________________________________")
print("--------------------------------->>> Welcome To Docker Assistant version1 <<<------------------------------------",end='')
print("_________________________________________________________________________________________________________________")
pyttsx3.speak("Welcome To Docker Assistant version 1")
pyttsx3.speak("This is a voice controlled program.")
pyttsx3.speak("Hi, what is your name?")
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("\nStart speaking please...")
	audio = r.listen(source)
cmd=r.recognize_google(audio)
y=cmd.split()
j=0
if("name" in y[0:]):
	while ((y[j]!="name") and (j<len(y)-1)):
		j=j+1
	cmd=y[j+2:]
else:
	while ((y[j]!="am") and (j<len(y)-1)):
		j=j+1
	cmd=y[j+1:]
pyttsx3.speak("Nice to meet you {}\n".format(cmd))

while(done!=1):
	if(vrgn==0):
		pyttsx3.speak("What can i do for you?\n")
		print("What can i do for you?")
		vrgn=vrgn+1
	else:
		pyttsx3.speak("What else can i do for you?\n")
		print("\nWhat else can i do for you?")
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print("\nStart speaking please...")
		audio = r.listen(source)
		print("Message received!\n")
	cmd=r.recognize_google(audio)
	if ((("run" in cmd) or ("launch" in cmd) or ("start" in cmd) or ("create" in cmd) or ("initiate" in cmd) or ("open" in cmd)) and (("container" in cmd) or ("a os" in cmd) or ("an os" in cmd)or ("operating system" in cmd))):
		pyttsx3.speak("Please enter the name of OS you want to launch")
		print("Please enter the name of OS you want to launch:",end='')
		osn=input()
		if(osn in oslist[1:]):
			print("OS name already used,please use a different name!")
			pyttsx3.speak("OS name already used before, please use a different name")
			pyttsx3.speak("List of already used up names is displayed below")
			print("List of already used up names is displayed below:")
			print("-> "+oslist[1:]+" <-")
			print()
			pyttsx3.speak("Please enter a different name of OS you want to launch")
			print("Please enter the name of OS you want to launch:",end='')
			osn=input()
		oslist.append(osn)
		pyttsx3.speak("Please select the number corres ponding to desired OS image to be used ")
		print("Please select the number corresponding to desired OS image to be used:")
		print("O.S. IMAGE\tVERSION\n")
		print("1. Centos\tlatest")
		print("2. Centos\t7")
		print("3. Ubuntu\t14.04")
		if(len(newosn)>3):
			f=3
			while f<len(newosn):
				print("{0}. {1}\t{2}".format(f+1,newosn[f],newosv[f]))
				f=f+1
		print("{}. Other O.S. Image\n".format(other))
		print("Enter the desired option:",end='')
		osi=input()
		osi=int(osi)
		print()
		if(osi == 1):
			curi.append('centos:latest')
			webbrowser.open("http://192.168.1.3/cgi-bin/dockerun.py?x={}&y=centos%3Alatest".format(osn))
		elif(osi == 2):
			curi.append('centos:7')
			webbrowser.open("http://192.168.1.3/cgi-bin/dockerun.py?x={}&y=centos%3A7".format(osn))
		elif(osi == 3):
			curi.append('ubuntu:14.04')
			webbrowser.open("http://192.168.1.3/cgi-bin/dockerun.py?x={}&y=ubuntu%3A14.04".format(osn))
		elif(osi == other):
			pyttsx3.speak("It seems that we do not possess your required OS image with us right now")
			pyttsx3.speak("We will install the image for you.")
			pyttsx3.speak("Please enter your required OS image name")
			print("Please enter your required OS image name :",end='')
			wishos=input()
			newosn.append(wishos)
			pyttsx3.speak("Please enter a valid version of the OS image you require")
			print("\nPlease enter a valid version of the OS image you require :",end='')
			wishv=input()
			newosv.append(wishv)
			wish=wishos+":"+wishv
			curi.append(wish)
			other=other+1
			webbrowser.open("http://192.168.1.3/cgi-bin/dockerun.py?x={}&y={}%3A{}".format(osn,wishos,wishv))
			pyttsx3.speak("Sometimes it may show Gateway timeout error after some time in the webpage opened")
			pyttsx3.speak("Don't worry about it. Your OS will be launched perfectly!")
			
		else:
			wish=newosn[osi-1]+":"+newosv[osi-1]
			curi.append(wish)
			webbrowser.open("http://192.168.1.3/cgi-bin/dockerun.py?x={}&y={}%3A{}".format(osn,newosn[osi-1],newosv[osi-1]))
		nos=len(oslist)-1
			
	elif ((("stop" in cmd) or ("terminate" in cmd) or ("end" in cmd) or ("close" in cmd)) and (("container" in cmd) or ("os" in cmd) or ("operating system" in cmd))):
		if(nos<0):
			pyttsx3.speak("Sorry there seem to be no currently running containers present!")
			pyttsx3.speak("Please proceed by launching your first container by using this program")
		else:	
			pyttsx3.speak("You will be soon redirected to a webpage, please enter os name which has to be stopped to continue")
			nos=nos-1
			webbrowser.open("http://192.168.1.3/dstop.html")
	
	elif((("interact" in cmd) or ("work" in cmd) or ("execute" in cmd) or ("connect" in cmd)) and (("container" in cmd) or ("OS" in cmd) or ("operating system" in cmd))):
		if(nos==0):
			pyttsx3.speak("Sorry there seem to be no currently running containers present!")
			pyttsx3.speak("To interact with an operating system, you have to first launch one")
		else:
			pyttsx3.speak("I will list the previously launched containers for you")
			print("List of previously launched containers:")
			print("O.S. Name\tImage Used")
			w=1
			while w<len(oslist):
				print("{} \t{}".format(oslist[w],curi[w]))
				w=w+1
			print()
			pyttsx3.speak("Please enter name of desired O.S. and desired command you want to interact with in the webpage that follows")
			webbrowser.open("http://192.168.1.3/dint.html")
			pyttsx3.speak("If the output seems to be distorted, please right click on the browser and select view page source!")
			
		
	elif (("nothing" in cmd) or ("done" in cmd) or ("nope" in cmd)):
		pyttsx3.speak("Thank you for using Docker Assistant")
		pyttsx3.speak("Do you want to delete all the containers that were created during this session?")
		pyttsx3.speak("Please note all your saved work will be lost upon choosing yes")
		pyttsx3.speak("Please respond with yes or no")
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			print("\nStart speaking please...")
			audio = r.listen(source)
			print("Message received!\n")
		ch = r.recognize_google(audio)
		if(ch == "yes"):
			pyttsx3.speak("All the OS launched during this session have been removed!")
			nos=len(oslist)-1
			webbrowser.open("http://192.168.1.3/cgi-bin/dockerclean.py?x={}".format(nos))
		else:	
			pyttsx3.speak("Please note all the containers will continue to exist and your work is saved.")
			pyttsx3.speak("In future you must take care to not use a name present in the list below to launch an os")
			print(">>> ",end='')
			print(oslist[1:],end='')
			print(" <<<")
			pyttsx3.speak("Please take a note of existing container names to live in a error ,free future!")
			time.sleep(5)
		done=1
	else:
		help=help+1
		if(help>2):
			help=0
			pyttsx3.speak("It seems you are having bit of trouble using this program")
			pyttsx3.speak("Do you want me to show the available list of commands and their usage")
			pyttsx3.speak("Please respond with yes or no")
			with sr.Microphone() as source:
				r.adjust_for_ambient_noise(source)
				print("\nStart speaking please...")
				audio = r.listen(source)
				print("Message received!\n")
			adele=r.recognize_google(audio)
			if(adele =="yes"):
				pyttsx3.speak("Here is the list of all the available commands as of version 1 and their correct usage!")
				print("Commands\t\t\t\tUsage(Say the following to the assistant when promptd)")
				print()
				print("New Container(O.S.)\t\t\tCan you launch a new container for me?")
				print("Stop Container(O.S.)\t\t\tCan you stop a container for me?")
				print("Executed command in a Container(O.S.)\tPlease connect me to a container.")
				print("Exit the program\t\t\tI am done!.")
			
			else:
				continue
		else:
			pyttsx3.speak("Sorry i didn't get you!")
			pyttsx3.speak("Would you like to try again?")
			pyttsx3.speak("Please respond with yes or no")
			with sr.Microphone() as source:
				r.adjust_for_ambient_noise(source)
				print("\nStart speaking please...")
				audio = r.listen(source)
				print("Message received!\n")
			choice=r.recognize_google(audio)
			if(choice =="yes"):
				continue
			elif(choice == "no"):
				done=1
				continue
			else:
				pyttsx3.speak("Invalid Choice!")
		
		