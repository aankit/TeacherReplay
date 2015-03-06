import picamera
import moviepy
import subprocess

class Video(object):

	def __init__(self, resolution=(1280,720)):
		self.camera = picamera.PiCamera()
		self.camera.resolution = resolution

	def record(self, fname, duration):
	    self.camera.start_recording(fname)
	    self.camera.wait_recording(duration)
	    self.camera.stop_recording()

	def startRecording(self, fname):
		self.camera.start_recording(fname)
		return 1

	def stopRecording(self):
		self.camera.stop_recording()
		return 1

	def checkRecording(self):
		return self.camera.wait_recording(2)

if __name__ == '__main__':
	import time
	video = Video()
	start = time.time()
	print start
	recording = 0
	video.startRecording('picam_test.h264')
	while recording < 10:
		print '%d elapsed' %(recording)
		recording = time.time() - start
		video.checkRecording()
	video.stopRecording()
