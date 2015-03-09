#import threading
import datetime
import time
import os
import config
import Video
import Audio
import subprocess

# Functions
def WriteLog(line):
  f = open(os.path.join(config.LOG_PATH,'log.txt'), 'a')
  stamp = time.strftime("[%H:%M:%S %Y-%m-%d] ", time.gmtime())  
  f.write(stamp + line + '\n')
  f.close()

#get today's date & create content folders
today = datetime.date.today().strftime('%m.%d.%Y')
subprocess.call(['mkdir', today])

#processing queues
video_encode_queue = []
audio_combine_queue = []

recording = False
filename = ''

schoolDay = True

while schoolDay:
	# recordingDuration = 60
	while not recording:
		#check class schedule to see if we should be recording
		for k, v in config.CLASS_SCHEDULE.items():
			className = k
			start, end = v
			recordingDuration = end - start
			now = time.time()
			if abs(start-now)<5:
				filename = className + today
				recording = True
				break
			else:
				print "free time"

	# print '%s class, %d start, %d end' %(className, start, end)
	#time to record!!!!
	video = Video.Video()
	
	# audio = Audio.Audio('%s/raw/output_cd_main.wav' %(config.PATH))
	# # audio = Audio.Audio('%s.wav' %(filename))
	video.camera.vflip = True
	video.camera.start_recording('%s/%s/%s.h264' %(className, today, filename))
	subprocess.call(['arecord', '--duration=%d' (recordingDuration), '--format=cd', 
		'%s/%s/%s.wav' %(className, today, filename)])
	print 'recorded!!'
	# audio.alsa_record(30)
	# x = 0
	# while x < 10:
	# 	x += 1
	# 	print x
	# 	# video.camera.wait_recording(2)
	# 	time.sleep(2)
	# audio.stop_recording()
	# audio.close()
	video.camera.stop_recording()
	video.camera.close()
	schoolDay = False

	
# #this is the threading code, test with it later.
# 	# audio_ready = threading.Event()
# 	# video_ready = threading.Event()

# 	# # launch the parrallel audio thread
# 	# audiothread = threading.Thread(target=record_audio,
#  #    	args = (filename, audio_ready, video_ready))
# 	# audiothread.start()

# 	# record_video(filename, audio_ready, video_ready)
	
# 	# setupTime = now - startTime


# 	recordingTime = 0
# 	# video.camera.start_recording('%s.h264' %(filename))
# 	# audio.start_recording()
# 	startTime = time.time()
# 	print 'duration is %d' %(recordingDuration)
# 	while recordingTime > recordingDuration:
# 		recordingTime = time.time() - startTime
# 		print '%d elapsed' %(recordingTime)
	# 	video.camera.wait_recording(2)
	# video.camera.stop_recording()
	# audio.stop_recording()

	#

	#check to see if its still the school day
	# check = time.time()
	# if check > config.EOD:
	# 	print 'ending the day'
	# 	schoolDay = False




