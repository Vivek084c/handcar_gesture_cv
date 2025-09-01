# Hand Gesture Recognition (handcar_gesture_cv)

A simple hand gesture recognition project using OpenCV, MediaPipe, and NumPy.

## Features

- Detects hand gestures in real-time using your webcam.
- Recognizes gestures like Thumbs Up, Fist, Open Palm, and Peace.

## Demo

### Open Palm
![Open Palm Demo](assets/open.png)

### Thumbs Up
![Thumbs Up Demo](assets/close.png)

## Demo Video  

- The demo video can be accessed through the link [here](https://drive.google.com/file/d/1hhhnOSMpXxIV75jculkRmvDPz6Qc59wO/view?usp=sharing).

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