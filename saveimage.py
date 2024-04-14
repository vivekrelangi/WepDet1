import cv2
#from tracker import *
from datetime import datetime
import os
def imgwrite(img):
    now = datetime.now()
    current_time = now.strftime("%d_%m_%Y_%H_%M_%S")
    filename = '%s.png' % current_time
    cv2.imwrite(os.path.join(r"/home/ghostprime/FinalYearProject/Weapon-Detection-with-yolov3-master/weapon_detection/savedimages",filename),img)
    return filename