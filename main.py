#import threading
import datetime
import time
import os
import config
import Video
import Audio

# Functions
def WriteLog(line):
  f = open(os.path.join(config.LOG_PATH,'log.txt'), 'a')
  stamp = time.strftime("[%H:%M:%S %Y-%m-%d] ", time.gmtime())  
  f.write(stamp + line + '\n')
  f.close()

#get today's date
today = datetime.date.today().strftime('%m.%d.%Y')
videos = []
audios = []
recording = False
filename = ''
schoolDay = True

while schoolDay:
	
	while not recording:
		#check class schedule to see if we should be recording
		for k, v in config.CLASS_SCHEDULE.items():
			className = k
			start, end = v

			now = time.time()
			if abs(start-now)<60000:
				filename = className + today
				recording = True
				break
			else:
				print "free time, maybe we can combine, cut and encode some video?"
	print '%s class, %d start, %d end' %(className, start, end)
	#time to record!!!!
	video = Video.Video()
	audio = Audio.Audio('%s.wav' %(filename))
	# audio_ready = threading.Event()
	# video_ready = threading.Event()

	# # launch the parrallel audio thread
	# audiothread = threading.Thread(target=record_audio,
 #    	args = (filename, audio_ready, video_ready))
	# audiothread.start()

	# record_video(filename, audio_ready, video_ready)
	
	# setupTime = now - startTime
	recordingTime = 0
	# video.camera.start_recording('%s.h264' %(filename))
	# audio.start_recording()
	startTime = time.time()
	duration = start - end
	print 'duration is %d' %(duration)
	while recordingTime > duration:
		recordingTime = time.time() - startTime
		print '%d elapsed' %(recordingTime)
	# 	video.camera.wait_recording(2)
	# video.camera.stop_recording()
	# audio.stop_recording()

	#check to see if its still the school day
	check = time.time()
	if check > config.EOD:
		print 'ending the day'
		schoolDay = False




