import requests, os, datetime, time, pyrebase, numpy as np, cv2
from twilio.rest import Client
from gpiozero import LED

led1 = LED(23)
led2 = LED(24)

# To avoid multiple calls
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
client = Client("ACbf7167e386e0c2cc7966460a82dcaac2", "1df9158670fac6f94b989af64bc73d50")

# Function to make call
def dial_numbers():
    led1.on()
    for number in DIAL_NUMBERS:
        print("Dialing " + number)
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER, url=TWIML_INSTRUCTIONS_URL, method="GET")
    led1.off()

# Function for Image processing
def cloud():
    led2.on()
    storage.child(f"images/{frame_uid}").put(f"/home/pi/Desktop/dl_processed/{frame_uid}")
    view_img = storage.child(f"images/{frame_uid}").get_url(None)

    # For sending messages
    for number in DIAL_NUMBERS:
        print("messaging" + number)
        client.messages.create(body=f'Movement detected @ {frame_uid[:-4]} - Click below url to view the spotted image {view_img}', from_=TWILIO_PHONE_NUMBER, to=DIAL_NUMBERS)
    led2.off()


while True:
    #driver.refresh()
    time.sleep(2)
    url = 'http://192.168.43.41:22111/frames/snap.jpg'
    r = requests.get(url)

    open('/home/pi/Desktop/frames/snap.jpg', 'wb').write(r.content)
    size = os.path.getsize('/home/pi/Desktop/frames/snap.jpg')
    if size > 500:
        print("image got")
        frame_uid = str(datetime.datetime.now()) + '.jpg'
        open(f'/home/pi/Desktop/dl_processed/{frame_uid}', 'wb').write(r.content)
        if called == 0:
            dial_numbers()
            called = 1
        cloud()
    os.remove('/home/pi/Desktop/frames/snap.jpg')
