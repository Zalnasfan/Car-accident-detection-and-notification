import subprocess
import os
from glob import glob
import csv

# Function to make shots
def make_shots(var):
    try:
        os.mkdir("VideoClips")
    except FileExistsError:
        pass
    subprocess.run(["scenedetect", "-i", var,        "-o", "./VideoClips", "detect-content",
                    "-t", "27", "split-video"])


if __name__ == '__main__':

    try:
        os.remove("feature_vector.csv")
        os.remove("label_vector.csv")
    except OSError:
        pass

    labelvector = []

    # Running algorithm for Accident Videos
    for var in glob("./RoadAccidents/*.mp4"):
        print(var)
        make_shots(var)
        os.system("python FrameExtract.py")
        os.system("python KeyFrameExtract.py")
        os.system("python GaborFeatureExtraction.py")
        labelvector.append(1) # 1 -> accident

    # Running algorithm for Non-Accident Videos
    for var in glob("./NonAccidents/*.mp4"):
        print(var)
        make_shots(var)
        os.system("python FrameExtract.py")
        os.system("python KeyFrameExtract.py")
        os.system("python GaborFeatureExtraction.py")
        labelvector.append(0)  # 0 -> non-accident

    # Making label_vector.csv
    with open("label_vector.csv", 'a') as outfile:
        writer = csv.writer(outfile, delimiter=' ')
        writer.writerow(labelvector)

    # Reading feature_vector.csv file for checking purpose
    # readlist = []
    # with open("feature_vector.csv", 'r') as my_file:
    #     reader = csv.reader(my_file, delimiter=' ')
    #     readlist = list(reader)
    #
    # new_list = [list(map(float, lst)) for lst in readlist]
    # print(new_list)
