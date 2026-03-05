import os
import cv2
import numpy as np
from ultralytics import YOLO

RGB_ROOT   = r"D:\Chorerobotics\codes\RGB"
SEG_ROOT   = r"D:\Chorerobotics\codes\Segmentation"
DEPTH_ROOT = r"D:\Chorerobotics\codes\Depth"

print("🚀 EDEN V4 — Instance + Depth Perception Stack")

# Optional YOLO layer
model = YOLO("yolov8n.pt")

# --------------------------------------------------
def get_instance_boxes(inst_img):
    """
    Each unique color = one object instance
    """
    boxes = []

    colors = np.unique(inst_img.reshape(-1,3),axis=0)

    for col in colors:

        if np.all(col==0):
            continue

        mask = cv2.inRange(inst_img,col,col)
        contours,_ = cv2.findContours(mask,
                                      cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            x,y,w,h = cv2.boundingRect(c)

            if w*h < 800:   # remove tiny noise
                continue

            boxes.append((x,y,x+w,y+h))

    return boxes

# --------------------------------------------------
def estimate_distance(depth,box):
    x1,y1,x2,y2 = box
    roi = depth[y1:y2,x1:x2]

    if roi.size==0:
        return 999

    d = np.mean(roi)
    return int(100 - (d/255*100))

# --------------------------------------------------
def guess_label(frame,box):

    x1,y1,x2,y2 = box
    roi = frame[y1:y2,x1:x2]

    if roi.size==0:
        return "Obstacle"

    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

    h = np.mean(hsv[:,:,0])
    s = np.mean(hsv[:,:,1])

    # green-ish
    if 35<h<85 and s>50:
        return "Bush"

    # gray-ish
    if s<40:
        return "Stone"

    return "Obstacle"

# --------------------------------------------------
for scene in os.listdir(RGB_ROOT):
    for weather in os.listdir(os.path.join(RGB_ROOT,scene)):

        rgb_folder   = os.path.join(RGB_ROOT,scene,weather)
        seg_folder   = os.path.join(SEG_ROOT,scene,weather)
        depth_folder = os.path.join(DEPTH_ROOT,scene,weather)

        files = [f for f in os.listdir(rgb_folder) if f.endswith("_L.png")]

        for f in files:

            rgb_path   = os.path.join(rgb_folder,f)
            inst_path  = os.path.join(seg_folder,f.replace(".png","_Inst.png"))
            depth_path = os.path.join(depth_folder,f.replace(".png","_vis.png"))

            if not os.path.exists(inst_path):
                continue

            frame = cv2.imread(rgb_path)
            inst  = cv2.imread(inst_path)
            depth = cv2.imread(depth_path,0)

            if frame is None or inst is None or depth is None:
                continue

            vis = frame.copy()

            # 🔥 INSTANCE OBJECTS
            boxes = get_instance_boxes(inst)

            for box in boxes:

                x1,y1,x2,y2 = box

                dist = estimate_distance(depth,box)
                label = guess_label(frame,box)

                # risk color
                if dist<30:
                    color=(0,0,255)
                elif dist<60:
                    color=(0,165,255)
                else:
                    color=(0,255,255)

                cv2.rectangle(vis,(x1,y1),(x2,y2),color,2)
                cv2.putText(vis,f"{label} {dist}cm",
                            (x1,y1-8),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,color,2)

            # depth mini view
            depth_vis = cv2.applyColorMap(depth,cv2.COLORMAP_JET)
            depth_vis = cv2.resize(depth_vis,(320,180))
            vis[0:180,0:320] = depth_vis

            cv2.imshow("EDEN V4 — Advanced Obstacle Perception",vis)

            if cv2.waitKey(30)==27:
                exit()

cv2.destroyAllWindows()