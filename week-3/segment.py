from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

results = model.predict(
    source="input-task3.mp4",
    save=True,
    boxes=False
)