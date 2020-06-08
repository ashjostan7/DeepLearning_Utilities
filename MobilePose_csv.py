import numpy as np
import xml.etree.ElementTree as ET
from decimal import Decimal
import string
import csv


    

#Reading the XML File
xml_file = 'E:\\ILP\\Code\\Dataset\\xml\\video1.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

with open('./dataset/data.csv',newline='',mode='w') as data_csv:
    data_writer = csv.writer(data_csv, delimiter=',', quoting=csv.QUOTE_MINIMAL) 
    id=0
    for child in root.iter('image'):
        array=[]
        filename="{}.jpg".format(id)
        array.append(filename)
        id=id+1
        joints={"L_ankle":[],
        "L_MTP":[],
        "L_toe":[],
        "R_ankle":[],
        "R_MTP":[],
        "R_toe":[]
        }
        for child2 in child:
            #Getting the keypoint & occlusion of current joint - stored as string in xml
            keypoint=child2.get('points')
            occlusion=child2.get('occluded')
            if occlusion == '0':
                v=2
            else:
                v=1

            #Converting keypoints to list of float values:
            index=keypoint.find(',',0)
            pt=float(keypoint[0:index])
            pt1=float(keypoint[index+1:len(keypoint)])
            keypoint=[pt,pt1,v]

            #Accessing the joint name
            for child3 in child2:
                j_name=child3.text
            if keypoint!=None:
                #print("Joint:{0} , Coord:{1}".format(j_name,keypoint))
                joints[j_name]=keypoint
            
        for i in joints:
            #Get the values of joint coordinates stored in current joint (key)
            li=joints.get(i)
            #If the list of coordinates are empty then skip. 
            if not li:
                continue
            array.append(li[0])
            array.append(li[1])
        
        data_writer.writerow(array)