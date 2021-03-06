import cv2, datetime, os, time, numpy as np, subprocess

# http connection for transferring files(like socket, ftp...)
process = subprocess.Popen("xfce4-terminal -x python3 -m http.server 22111", shell=True)

# Camera ON
video = cv2.VideoCapture(0)
image_frame = 0

# dl datasheets
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Image processing
def dl():
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
            cv2.putText(img, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 2/2, color, 2)
    cv2.imwrite("/home/linuxlite/Desktop/frames/snap.jpg", img)
    cv2.imwrite(f"/home/linuxlite/Desktop/Dl_processed/{frame_uid}", img)
    time.sleep(2)
    os.remove("/home/linuxlite/Desktop/frames/snap.jpg")

# Movement detecting
while video.isOpened:

    # difference
    check1, frame1 = video.read()
    check2, frame2 = video.read()
    diff = cv2.absdiff(frame1, frame2)

    # frame conversions
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # if motion...
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) >= 2500:
            if (image_frame % 50) == 0:
                print("Movement Detected")
                frame_uid = str(datetime.datetime.now()) + ".jpg"
                dl()
                original_img = cv2.resize(frame1, None, fx=2.0, fy=2.0)
                cv2.imwrite(f"/home/linuxlite/Desktop/Movement_images/{frame_uid}", original_img)
            image_frame += 1

    # Showing frames
    cv2.imshow('CCTV', frame1)


# Quitting program
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()