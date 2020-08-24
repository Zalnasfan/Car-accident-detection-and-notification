import cv2
import os
import shutil
from glob import glob

folderCounter = 1
folderBase = "FrameFolder"
num = 0


# Function to extract frames from videos
def FrameCapture(path):
    global folderCounter, num
    vidObj = cv2.VideoCapture(path)

    # fps = vidObj.get(cv2.CAP_PROP_FPS)
    # print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    success = 1
    count = 0
    folderName = folderBase + str(folderCounter)
    os.mkdir(folderName)
    folderCounter += 1
    while success:
        success, image = vidObj.read()
        if(success is True):  # confirm that image is not None
            pathname = folderName + "/frame" + str(count) + '.jpg'
            cv2.imwrite(pathname, image)
        count += 1
    num += count


if __name__ == '__main__':
    for var in glob("./VideoClips/*.mp4"):
        print(var)
        FrameCapture(var)
    # FrameCapture("./RoadAccident1.mp4")
    print('FE:', num)
    shutil.rmtree("VideoClips")
