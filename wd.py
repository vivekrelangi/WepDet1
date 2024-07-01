import cv2
import numpy as np
from saveimage import imgwrite
from mailcode import send_emails
from mailcode import email_to_list
#mail code
"""import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('yourmail@abc.com','password')

server.sendmail('yourmail@abc.com','yourmail@abc.com','Mail sent from python code')
print('Mail sent')"""
"""from email.message import EmailMessage
#from maildm import password
import ssl
import smtplib

email_sender = 'yourmail@abc.com'
email_password = 'your password'

email_receiver = 'yourmail@abc.com'

subject = "Mail from python code"
body=""""Wep det msg.""""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

"""
#mail code

# Load Yolo
net = cv2.dnn.readNet("trainedfile.weights", "configfile.cfg")
classes = ["Weapon"]
# with open("coco.names", "r") as f:
#     classes = [line.strip() for line in f.readlines()]

# layer_names = net.getLayerNames()
# output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
output_layer_names = net.getUnconnectedOutLayersNames()
colors = np.random.uniform(0, 255, size=(len(classes), 3))


# Loading image

# Enter file name for example "abc.mp4" or press "Enter" to start webcam
def value():
    val = input("Enter file name or press enter to start webcam : \n")
    if val == "":
        val = 0
    return val


# for video capture
cap = cv2.VideoCapture(value())

# val = cv2.VideoCapture()
while True:
    _, img = cap.read()
    if not _:
        print("Error: Failed to read a frame from the video source.")
        break
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layer_names)

    # Showing information on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    print(indexes)
    if indexes == 0: 
        print("weapon detected in frame")
        """with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())"""

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
            fname=imgwrite(img)
            send_emails(email_to_list,fname)


    # frame = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    cv2.imshow("Image", img)
    #imgwrite(img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
