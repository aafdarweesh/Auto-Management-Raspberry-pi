import subprocess
import time

print(subprocess.getstatusoutput('pkill -f Auto-Management-Raspberry-pi/Streaming.py'))#Stop the execution of the current program
#remove the current version of it
print(subprocess.getstatusoutput('rm Auto-Management-Raspberry-pi/*'))
print(subprocess.getstatusoutput('rm -rf Auto-Management-Raspberry-pi'))

print(subprocess.getstatusoutput('git clone https://github.com/aafdarweesh/Auto-Management-Raspberry-pi'))

time.sleep(5) #sleep for 1 min

try :
	#exec(open("Auto-Management-Raspberry-pi/UpdateRepository.py").read())#Update Repository
	exec(open("Auto-Management-Raspberry-pi/RunProgram.py").read())#Run python file in the Repository after updating
finally :
	exit()
