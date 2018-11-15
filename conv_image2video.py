#!/usr/local/bin/python3
# Modified after "http://tsaith.github.io/combine-images-into-a-video-with-python-3-and-opencv-3.html"
# Author: Utpal Kumar
import cv2
import argparse
import os

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ext", "--extension", required=False, default='png', help="extension name. default is 'png'.")
ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
ap.add_argument("-loc", "--location", required=False, default='.', help="path location of the images")
ap.add_argument("-fr", "--framerate", required=False, default='5', help="specify the frame rate for video output")
args = vars(ap.parse_args())

# Arguments
dir_path = args['location']
ext = args['extension']
output = args['output']
framerate = args['framerate']
def make_video(dir_path,ext,output,framerate):
    images = []
    for f in sorted(os.listdir(dir_path)):
        if f.endswith(ext):
            images.append(f)
    # Determine the width and height from the first image
    image_path = os.path.join(dir_path, images[0])
    frame = cv2.imread(image_path)
    # cv2.imshow('video',frame)
    height, width, channels = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    out = cv2.VideoWriter(output, fourcc, int(framerate), (width, height))

    for image in images:
        image_path = os.path.join(dir_path, image)
        # print(image_path)
        frame = cv2.imread(image_path)
        resized=cv2.resize(frame,(width, height))
        print(image_path)
        out.write(resized) # Write frame to video

    # Release everything if job is finished
    out.release() #closes video file and capturing device
    #cv2.destroyAllWindows()

    print("The output video is {}".format(output))

if __name__=="__main__":
    make_video(dir_path,ext,output,framerate)
