import os
from imutils.video import FileVideoStream
from imutils.video import VideoStream
import cv2
import time

import pylab
import imageio
imageio.plugins.ffmpeg.download()


filedir = 'F:/test/1.mp4'
videos_save_path = 'C:/Users/Young/Desktop/tenp/video/1'




#!/usr/bin/env python  

vc=cv2.VideoCapture(filedir)  
c=1  
if vc.isOpened():  
    rval,frame=vc.read()  
else:  
    rval=False  
while rval:  
    if c<100:
        
        rval,frame=vc.read()  
        cv2.imwrite(videos_save_path + "/" +str(c)+'.jpg',frame)  
        c=c+1  
#    cv2.waitKey(1)  
vc.release()  

#
#
#
#filename = 'F:/test/1.mp4'
##可以选择解码工具
#vid = imageio.get_reader(filename,  'ffmpeg')
#for im in enumerate(vid):
#    #image的类型是mageio.core.util.Image可用下面这一注释行转换为arrary
#    #image = skimage.img_as_float(im).astype(np.float32)
#    fig = pylab.figure()
#    fig.suptitle('image #{}'.format(num), fontsize=20)
#    pylab.imshow(image)
#pylab.show()
#
#
#
#



#
# 
#cap = cv2.VideoCapture('filedir') #创建一个视频获取对象  
#flag = 0  
#while (cap.isOpened()):  
##    cap.set(cv2.CAP_PROP_POS_MSEC,flag)#设置时间标记  
#    cap.set(cv2.CAP_PROP_POS_FRAMES,flag) #设置帧数标记  
#    ret,im = cap.read()#获取图像  
#    #cv2.waitKey(2000)#延时  
#    cv2.imshow('a',im)#显示图像，用在循环中可以播放视频  
#    cv2.imwrite('filedir：\\test{}.jpg'.format(flag),im)#保存图片  
#    fr+=10#设置间隔  
#    if not ret:  
#        break  
#    
#    
    
video = 'F:/test/1.mp4'
vs = FileVideoStream(video).start()

#fileStream = True
#vs = VideoStream(src=0).start()
#vs = VideoStream(usePiCamera=True).start()
#fileStream = False
#time.sleep(1.0)

# loop over frames from the video stream
while True:
	# if this is a file video stream, then we need to check if
	# there any more frames left in the buffer to process
#	if fileStream and not vs.more():
#		break

	# grab the frame from the threaded video file stream, resize
	# it, and convert it to grayscale
	# channels)
	frame = vs.read()

	# show the frame
	cv2.imshow("Frame", frame)
    