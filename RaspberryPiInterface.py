import os
from picamera import PiCamera
from time import sleep
from bottle import request, Bottle, abort, static_file, template, redirect
app = Bottle()

@app.route('/')
def TEST():
        return {'TEST'}

#start a mission http request (will run startRecording program, that is responsible for the videos, with the given details)
@app.route('/startMission/<videoDuration>/<numberOfVideos>')
def startMission(videoDuration, numberOfVideos):
        try:
                os.system('python ./startRecording.py ' + str(videoDuration) + ' ' + str(numberOfVideos))
                return {'True'}
        except:
                return {'False'}

#return the meta data of the trip (each video details start time, end time, GPS location, ...) It is important to trace that 
#information received is accurate
@app.route('/tripMetaData')
def tripMetaData():
        return static_file('tripMetaData.txt', root='./')

#return an exact video to the main server
@app.route('/video/<videoNumber>')
def sendVideo(videoNumber):
        return static_file('video' + str(videoNumber) + '.h264', root='./videoBuffer')

#delete video from local buffer (and confirm the operation)
@app.route('/deleteVideo/<videoNumber>')
def deleteVideo(videoNumber):
        try :
                os.system('rm ./videoBuffer/video' + str(videoNumber) + '.h264')
                if os.path.exists('./videoBuffer/video' + str(videoNumber) + '.h264') == True:
                        return {'False'}
                return {'True'}
        except :
                return {'False'}



#delete all videos in the local buffer (and confirm the operation)
@app.route('/AfterTripDeletion')
def deleteAllVideos():
        try :
                os.system('rm ./videoBuffer/*.*')
                os.system('echo -n > ./tripMetaData.txt') #delete the content of the current metaData file
                return {'True'}
        except :
                return {'False'}



#Mainly for testing
@app.route('/specificVideo')
def specificVideo():
        return static_file('specificVideo.mov', root='./')


from gevent.pywsgi import WSGIServer

server = WSGIServer(("0.0.0.0", 1234), app)
print ("access @ http://0.0.0.0:1234/")


server.serve_forever()

