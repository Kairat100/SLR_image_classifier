import numpy as np
import cv2
import cv2.cv as cv
import time
import argparse

# argument parser run as [python video_to_frames.py -v ./videos/sing.webm -f 1]
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--video", required=True, help="path to video file [required]")
parser.add_argument("-s", "--scale", help="scale size", type = int)
parser.add_argument("-t", "--time", help="time slow", type = int)
parser.add_argument("-f", "--show", help="show video in frame", type = int)
args = parser.parse_args()

# default values for scale and time parameters
_show = 0;
if args.show:
	_show = args.show

scale = 1;
if args.scale:
	scale = args.scale

_time = 1;
if args.time:
	_time = args.time

# Capture video file
cap = cv2.VideoCapture(args.video)

if(_show == 1):
	cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('frame', int(cap.get(cv.CV_CAP_PROP_FRAME_WIDTH) * scale), int(cap.get(cv.CV_CAP_PROP_FRAME_HEIGHT) * scale))	

i = -1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == False:
    	break
    
    i += 1

    cv2.imwrite('./frames/frame' + str(i) + '.png', frame)

    if(_show == 1):
	 	# Display the resulting frame
	    cv2.imshow('frame',frame)
	    time.sleep(0.033 * _time)	    
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()