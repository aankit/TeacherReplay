import threading
import datetime
import time


while True:
	
	while not recording:
		#check class schedule to see if we should be recording
		for k, v in config.CLASS_SCHEDULE.items():
			start, end = v
			now = time.time()
			if abs(start-now)<60000:
				filename = className + date
				recording = True
				break
			else:
				print "free time, maybe we can combine, cut and encode some video?"

	audio_ready = threading.Event()
	video_ready = threading.Event()

	# launch the parrallel audio thread
    audiothread = threading.Thread(target=record_audio,
                              args = (filename, audio_ready, video_ready))
    audiothread.start()

    record_video(filename, audio_ready, video_ready)

    while 