import os
import cv2
'''尺寸为读取图片的尺寸'''

img_root = 'C:/Users/Young/Desktop/tenp/video/1'#这里写你的文件夹路径，比如：/home/youname/data/img/,注意最后一个文件夹要有斜杠
fps = 24    #保存视频的FPS，可以适当调整

img_path = 'C:/Users/Young/Desktop/tenp/video/lonly.jpeg'
#img_path = 'C:/Users/Young/Desktop/tenp/video/1/start/71.jpg'
#可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videoWriter = cv2.VideoWriter('lonely.avi',fourcc,fps,(600,621))#最后一个是保存图片的尺寸

'''一张图片'''
for i in range(99):
    frame = cv2.imread(img_path)
    videoWriter.write(frame)
videoWriter.release()

#imshow("video", frame)




'''多张图片,保存地址为右上方'''
img_root = 'C:/Users/Young/Desktop/tenp/video/1/start'
fps = 24    

#可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videoWriter = cv2.VideoWriter('teat1.avi',fourcc,fps,(1280,720))#最后一个是保存图片的尺寸
for i in range(71,97):
    frame = cv2.imread(img_root + "/" + str(i+1)+'.jpg')
    videoWriter.write(frame)
for j in range(0,10):
    
    for i in range(86,97):
        frame = cv2.imread(img_root + "/" + str(i+1)+'.jpg')
        videoWriter.write(frame)
    
videoWriter.release()





#
#
#
#test ="test"
#imgs2video(img_path,test)
#
#def imgs2video(imgs_dir, save_name):
#    fps = 24
#    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#    video_writer = cv2.VideoWriter(save_name, fourcc, fps, (1920, 1080))
#    # no glob, need number-index increasing
#    imgs = os.path.join(imgs_dir, '*.jpg')
#
#    for i in range(len(imgs)):
#        imgname = os.path.join(imgs_dir, 'core-{:02d}.jpg'.format(i))
#        frame = cv2.imread(imgname)
#        video_writer.write(frame)
#
#    video_writer.release()
