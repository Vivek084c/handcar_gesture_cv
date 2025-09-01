import cv2
import numpy as np
import mediapipe as mp
from collections import deque
import os



#local imports
from src.utils import finger_states, angle_with_vertical, classify_gesture
from src.const import TIP_IDS, PIP_IDS, THUMB_IP_ID, WRIST_ID



def main():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  960)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
    cap.set(cv2.CAP_PROP_FPS, 30)

    smoothing = deque(maxlen=5)

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.6
    ) as hands:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            label_to_show = "No Hand"
            if result.multi_hand_landmarks and result.multi_handedness:
                hand_landmarks = result.multi_hand_landmarks[0]
                handedness_label = result.multi_handedness[0].classification[0].label  # "Left"/"Right"
                # draw
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )
                # classify
                lm = hand_landmarks.landmark
                pred = classify_gesture(lm, handedness_label)
                smoothing.append(pred)
                # majority vote smoothing
                label_to_show = max(set(smoothing), key=smoothing.count)

            # overlay label
            cv2.putText(frame, f"Gesture: {label_to_show}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow("Hand Gesture Recognition", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
