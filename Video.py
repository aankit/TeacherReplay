import picamera
import moviepy
import subprocess

class Video(object):
	
	def __init__(self, fname, resolution):
		self.fname = fname
		self.resolution = resolution	


	def record(self, duration):
		with picamera.PiCamera() as camera:
		    camera.resolution = self.resolution
		    camera.start_recording(self.fname)
		    camera.wait_recording(duration)
		    camera.stop_recording()

	def convert(self):
		