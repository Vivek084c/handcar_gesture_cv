#global importa
import numpy as np

#local imports
from src.const import TIP_IDS, PIP_IDS, THUMB_IP_ID, WRIST_ID
def finger_states(landmarks, handedness_label):
    """Return dict: {index:bool, middle:bool, ring:bool, pinky:bool, thumb:bool}."""
    # landmarks are normalized (x,y) in [0,1]; we only compare relative positions
    fingers = {}
    # Non-thumb
    for f in ["index", "middle", "ring", "pinky"]:
        tip = landmarks[TIP_IDS[f]]
        pip = landmarks[PIP_IDS[f]]
        # tip.y < pip.y means the tip is higher on the image (finger up)
        fingers[f] = tip.y < pip.y

    # Thumb (use x based on handedness)
    thumb_tip = landmarks[TIP_IDS["thumb"]]
    thumb_ip  = landmarks[THUMB_IP_ID]
    if handedness_label == "Right":
        fingers["thumb"] = thumb_tip.x < thumb_ip.x
    else:
        fingers["thumb"] = thumb_tip.x > thumb_ip.x

    return fingers


def angle_with_vertical(p, q):
    """Angle (degrees) between vector p->q and the 'up' vertical direction."""
    vx, vy = (q.x - p.x, q.y - p.y)
    # Up vector in image coords is (0, -1)
    dot = vx*0 + vy*(-1)
    mag = np.hypot(vx, vy) + 1e-6
    cos_theta = np.clip(dot / mag, -1.0, 1.0)
    theta = np.degrees(np.arccos(cos_theta))
    return theta  # 0 = perfectly up, 180 = perfectly down

def classify_gesture(landmarks, handedness_label):
    fs = finger_states(landmarks, handedness_label)
    up = [f for f, state in fs.items() if state]
    down = [f for f, state in fs.items() if not state]

    # Thumbs Up: thumb up, others down, and thumb pointing roughly up
    if fs["thumb"] and all(not fs[f] for f in ["index","middle","ring","pinky"]):
        wrist = landmarks[WRIST_ID]
        thumb_tip = landmarks[TIP_IDS["thumb"]]
        if angle_with_vertical(wrist, thumb_tip) < 25:  # roughly upwards
            return "Thumbs Up"

    # Fist: all four main fingers down (ignore thumb)
    if all(not fs[f] for f in ["index","middle","ring","pinky"]):
        return "Fist"

    # Open Palm: all four main fingers up (thumb free)
    if all(fs[f] for f in ["index","middle","ring","pinky"]):
        return "Open Palm"

    # Peace: index + middle up, ring + pinky down
    if fs["index"] and fs["middle"] and (not fs["ring"]) and (not fs["pinky"]):
        return "Peace"

    return "Unknown"