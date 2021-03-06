import cv2, numpy as np, pyrebase
from datetime import datetime
from twilio.rest import Client

video = cv2.VideoCapture(0)
image_frame = 0
called = 0

# Firebase Storage Connectivity
config = {
        "apiKey": "AIzaSyB0QxPtqRbAvbb0bZshtdPh_5PYuvMIkeE",
        "authDomain": "theft-detector-iot.firebaseapp.com",
        "databaseURL": "https://theft-detector-iot.firebaseio.com",
        "projectId": "theft-detector-iot",
        "storageBucket": "theft-detector-iot.appspot.com",
        "messagingSenderId": "1060700333231",
        "appId": "1:1060700333231:web:f4be0b491e6451c074e05a",
        "measurementId": "G-Q1GW9RH818"}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# Twilio call & message connectivity
TWILIO_PHONE_NUMBER = "+12243026503"
DIAL_NUMBERS = ["+918608550403"]
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"
client = Client("ACbf7167e386e0c2cc7966460a82dcaac2", "52b6e3927a969f02ef82176eb97124a8")

# Function to make call
def dial_numbers():
    for number in DIAL_NUMBERS:
        print("Dialing " + number)
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER, url=TWIML_INSTRUCTIONS_URL, method="GET")

# Function for Image processing
def movement():
    img_uid = str(datetime.now())

    img_name = 'movement_' + img_uid + '.jpg'

    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    img = cv2.resize(frame1, None, fx=2.0, fy=2.0)
    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1 / 2, color, 2)
    cv2.imwrite(f"/home/linuxlite/Desktop/Movement_images/{img_name}", img)
    storage.child(f"images/{img_name}").put(f"/home/linuxlite/Desktop/Movement_images/{img_name}")
    view_img = storage.child(f"images/{img_name}").get_url(None)

    # For sending messages
    for number in DIAL_NUMBERS:
        print("messaging" + number)
        client.messages.create(body=f'Movement detected @ {img_uid} - Click below url to view the spotted image {view_img}', from_=TWILIO_PHONE_NUMBER, to=DIAL_NUMBERS)

# Capturing frames
while video.isOpened:

    check1, frame1 = video.read()
    check2, frame2 = video.read()
    diff = cv2.absdiff(frame1, frame2)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) >= 2500:
            #cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if (image_frame % 50) == 0:
                if called == 0:
                    dial_numbers()
                    called = 1
                movement()
            image_frame += 1

    # Showing frames
    cv2.imshow('CCTV', frame1)

    # Quitting program
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


