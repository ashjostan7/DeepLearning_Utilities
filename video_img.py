import cv2
import argparse

#Input Arguments
ap=argparse.ArgumentParser()
ap.add_argument("--pv","--path1",required="true",help="path to videoFile") 
ap.add_argument("--pi","--path2",required="true",help="path to save extracted images")
args= vars(ap.parse_args())

#Reading the input file
vid=cv2.VideoCapture(args["pv"])

#Checking if video is read
if(vid.isOpened()==False):
    print("Error Opening File")

frame_num=0
#Looping through frames to write in destination
while(vid.isOpened()):

    ret,frame=vid.read()

    if ret==True:
        filename=args["pi"]
        file="\\{0}.jpg".format(frame_num)
        filename=filename+file
        cv2.imwrite(filename,frame)
    else:
        break
    frame_num+=1

vid.release()



