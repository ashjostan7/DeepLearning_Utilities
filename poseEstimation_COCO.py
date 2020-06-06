import numpy as np
import xml.etree.ElementTree as ET
from decimal import Decimal
import string
import json

# Opening JSON file 
f = open('E:\\ILP\\Code\\Dataset\\xml\\vid1.json',) 
# returns JSON object as a dictionary 
data = json.load(f) 

#Reading the XML File
xml_file = 'E:\\ILP\\Code\\Dataset\\xml\\video1.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

dict={
    "segmentation":[],
    "num_keypoints":6,
    "isCrowd":0,
    "keypoints":[],
    "image_id":"",
    "bbox":"[]",
    "category_id":1,
    "id":0

}
id=0
for child in root.iter('image'):
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
        li=joints.get(i)
        if not li:
            joints[i]=[0,0,0]
        dict["keypoints"].append(joints[i][0])
        dict["keypoints"].append(joints[i][1])
        dict["keypoints"].append(joints[i][2])
        dict['id']=id
        id=id+1
        data["annotations"].append(dict)
    print(data)
    with open('sample.json', 'w') as json_file:
        json.dump(data, json_file,indent=4)
    

    
