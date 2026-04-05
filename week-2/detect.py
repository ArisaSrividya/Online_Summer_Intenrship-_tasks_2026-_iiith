from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("crosswalk.jpg", save=True)

print("Done")