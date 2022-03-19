<!-- PROJECT LOGO -->
<p align="center">
  <img src="https://github.com/Akash-Peace/IOT-PI-DL/blob/main/Screenshots/theft_detector_logo.png" alt="Logo" width="150" height="150">
  <h3 align="center">THEFT DETECTOR</h3>
  <p align="center">
    <a href="https://en.wikipedia.org/wiki/Internet_of_things"><strong>IoT</strong></a>
    .
    <a href="https://www.raspberrypi.org/"><strong>Raspberry Pi</strong></a>
    <br />
    <br />
    <a href="https://github.com/Akash-Peace/IOT-PI-DL/tree/main/Documentations">View Documentations</a>
    ·
    <a href="https://github.com/Akash-Peace/IOT-PI-DL/issues">Report Bug</a>
    ·
    <a href="https://github.com/Akash-Peace/IOT-PI-DL/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#powered-by">Powered By</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#my-raspberry-pi-spec">My Raspberry Pi Spec</a></li>
    <li><a href="#my-system-spec">My System Spec</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Theft detector project objective is to track the surveillance area and alert the user if any movement is detected. The alerting system includes MMS and calling the user done with [twilio](https://www.twilio.com/). User can update multiple numbers to receive mms and call. Movement detection and image processing are done with [OpenCV](https://opencv.org/). Object detection is one of the main features that detect what object is in the image done with [yolo](https://pjreddie.com/darknet/yolo/) deep learning model. Http server used to transfer images. Suspected scenes are captured in image format and store the image locally and in the cloud by [firebase](https://firebase.google.com/), accessed globally. [MIT](https://github.com/Akash-Peace/INDUSTRIAL-WEBSITE/blob/main/LICENSE) licenses this project. If you like this project, give a _star_ and follow me.


## Built With

* [Python](https://www.python.org/)


## Powered By

* [OpenCV](https://opencv.org/)
* [Firebase](https://firebase.google.com/)
* [Twilio](https://www.twilio.com/)
* [Yolo](https://pjreddie.com/darknet/yolo/)


## Requirements

**Device:** RaspberryPi & Laptop/PC\
**OS:** Windows/Linux/Mac\
**Network:** 3G or Above 3G 


## Installation

Step 1: Download [Sender_Camera.py](https://github.com/Akash-Peace/IOT-PI-DL/blob/main/Program%20for%20individual%20system%20and%20camera/Theft_Detector_Sender(Camera).py) file in system and [Receiver_System.py](https://github.com/Akash-Peace/IOT-PI-DL/blob/main/Program%20for%20individual%20system%20and%20camera/Theft_Detector_Receiver(System).py) file in raspberry pi.\
Step 2: Activate [http server](https://github.com/Akash-Peace/IOT-PI-DL/blob/main/Documentations/terminal.txt) through system terminal.\
Step 3: Run Receiver_System.py and then Sender_Camera.py.


<!-- USAGE EXAMPLES -->
## Usage

Usage of this project is to track the theft under the surveillance area and alert the user through call and mms. User can update multiple numbers to receive mms and call. Suspected scenes are captured in image format and stored securely in firebase, So you can access globally.


## Screenshots

View [Screenshots](https://github.com/Akash-Peace/IOT-PI-DL/tree/main/Screenshots) here.


<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](https://github.com/Akash-Peace/IOT-PI-DL/blob/main/LICENSE) for more information.



## My Raspberry Pi Spec

**OS:** [Raspbian](https://www.raspberrypi.org/software/operating-systems/)\
**Model:** Raspberry Pi Zero WH\
**Ram:** 512mb\
**Disk:** SD 32gb


## My System Spec

**OS:** [Garuda](https://garudalinux.org/)\
**Model:** Acer Aspire 5 A515-51G\
**Processor:** Intel i5 7th gen\
**Ram:** DDR4 8gb\
**Disk:** HDD 100gb


<!-- CONTACT -->
## Contact

Akash.A,\
Computer Science Engineer,\
akashcse2000@gmail.com,\
8608550403,\
Chennai.


![GitHub metrics](https://metrics.lecoq.io/Akash-Peace)  

Follow me on

[<img src='https://github.com/Akash-Peace/INDUSTRIAL-WEBSITE/blob/main/images/linkedin.png' alt='linkedin' height='40'>](https://www.linkedin.com/in/akash-2000-cse) &nbsp; &nbsp; &nbsp; [<img src='https://github.com/Akash-Peace/INDUSTRIAL-WEBSITE/blob/main/images/instagram.png' alt='instagram' height='40'>](https://www.instagram.com/nocturnal_lad) &nbsp; &nbsp; &nbsp; [<img src='https://github.com/Akash-Peace/INDUSTRIAL-WEBSITE/blob/main/images/facebook.png' alt='facebook' height='40'>](https://www.facebook.com/profile.php?id=100061841000593) &nbsp; &nbsp; &nbsp; [<img src='https://github.com/Akash-Peace/INDUSTRIAL-WEBSITE/blob/main/images/twitter.png' alt='twitter' height='40'>](https://twitter.com/AkashA53184506) &nbsp; &nbsp; &nbsp; [<img src='https://github.com/Akash-Peace/INDUSTRIAL-WEBSITE/blob/main/images/pypi.png' alt='pypi' height='50'>](https://pypi.org/user/Akash-Peace/) &nbsp; &nbsp; &nbsp; [<img src='https://github.com/Akash-Peace/INDUSTRIAL-WEBSITE/blob/main/images/youtube.png' alt='youtube' height='45'>](https://www.youtube.com/channel/UCmugCO6k7hgSZqaI1jzbelw/featured) 
