import subprocess
import time
import os
import requests

def check_internet():
	url='https://github.com/aafdarweesh/Auto-Management-Raspberry-pi'
	timeout=5
	try:
		_ = requests.get(url, timeout=timeout)
		return True
	except requests.ConnectionError:
		#print("İnternet bağlantısı yok.")
		return False




if check_internet() == True:
	print(subprocess.getstatusoutput('pkill -f Auto-Management-Raspberry-pi/RaspberryPiInterface.py'))#Stop the execution of the current program
	#remove the current version of it
	print(subprocess.getstatusoutput('rm Auto-Management-Raspberry-pi/*'))
	print(subprocess.getstatusoutput('rm -rf Auto-Management-Raspberry-pi'))

	print(subprocess.getstatusoutput('git clone https://github.com/aafdarweesh/Auto-Management-Raspberry-pi'))

	time.sleep(5) #sleep for 1 min

	try :
		#os.system('python3 Auto-Management-Raspberry-pi/RunProgram.py')
		os.system('python3 Auto-Management-Raspberry-pi/RaspberryPiInterface.py')
		#exec(open("Auto-Management-Raspberry-pi/UpdateRepository.py").read())#Update Repository
		#exec(open("Auto-Management-Raspberry-pi/RunProgram.py").read())#Run python file in the Repository after updating
	finally :
		exit()
else :
	print("Internet is not working")
