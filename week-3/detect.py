from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.predict(source="input-task3.mp4", save=True)