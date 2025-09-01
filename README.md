# Hand Gesture Recognition (handcar_gesture_cv)


## Demo Video  

- The demo video can be accessed through the link [here](https://drive.google.com/file/d/1hhhnOSMpXxIV75jculkRmvDPz6Qc59wO/view?usp=sharing).

## Demo

### Open Palm
![Open Palm Demo](assets/open.png)

### Thumbs Up
![Thumbs Up Demo](assets/close.png)


## Working Methodology
A simple hand gesture recognition project using OpenCV, MediaPipe, and NumPy.

This project focuses on recognizing hand gestures by analyzing the position of each finger using MediaPipe. The idea is simple: for the four main fingers (index, middle, ring, and pinky), the system checks whether the fingertip is higher or lower than its joint to decide if the finger is raised or folded. The thumb is treated differently, since it bends sideways—its position and angle are checked to see if it’s pointing upwards. Once the state of each finger is known, different gestures are identified through pattern matching. For instance, a raised thumb with other fingers folded is recognized as a “Thumbs Up,” all fingers closed form a “Fist,” all open fingers show an “Open Palm,” and only the index and middle fingers raised represent “Peace.” If no pattern fits, the gesture is labeled as “Unknown.”

## Features

- Detects hand gestures in real-time using your webcam.
- Recognizes gestures like Thumbs Up, Fist, Open Palm, and Peace.


## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/handcar_gesture_cv.git
   cd handcar_gesture_cv
   
## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/handcar_gesture_cv.git
   cd handcar_gesture_cv
   ```

2. **(Optional) Create a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirnment.txt
   ```

## Running the Project

```sh
python -m src.main
```

- A window will open showing your webcam feed.
- Detected gesture will be displayed on the video.
- Press `q` to quit.

## Project Structure

```
handcar_gesture_cv/
├── requirnment.txt
├── README.md
└── src/
    ├── const.py
    ├── main.py
    └── utils.py
└── assets/
    ├── close.png
    ├── open.png
```



## Future work

- Right now the classfication is based on traking the relative postion of critical points and basic maths, this leads to false positive
- This can be further enhanced by implemeting a custom trained Supervised learning model or Deep learninig based model