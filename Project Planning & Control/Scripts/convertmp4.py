import cv2

vidcap = cv2.VideoCature("/tmp/video2.mp4")
success,image = vidcap.read()

count = 0

while success:
    cv2.imwrite("frame%d.jpg" % count, image)
    success,image = vidcap.read()
    print('Read a new frame', success)
    count += 1