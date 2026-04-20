# Week 3 Task 1 - Object Detection & Semantic Segmentation

## 📊 Performance Metrics

### Detection Metrics:

* Box Precision: 0.7006
* Box Recall: 0.5650
* Box mAP50: 0.6515
* Box mAP50-95: 0.4895

### Segmentation Metrics:

* Mask Precision: 0.686
* Mask Recall: 0.617
* Mask mAP50: 0.582
* Mask mAP50-95: 0.407

## 📈 Training Results

![Results](results.png)

## 🎥 Final Output Video

The final segmented video with added background audio:

* Semantic segmentation highlights objects with colored masks
* Only the added audio is present in the video

## 🧠 Description

This project demonstrates object detection and semantic segmentation using YOLOv8. Detection provides bounding boxes, while segmentation provides pixel-level classification of objects.

The model was evaluated using precision, recall, and mAP metrics. The results indicate reasonable performance in both detection and segmentation tasks.

## 🚀 Conclusion

Semantic segmentation helps in identifying precise object boundaries, which is useful in applications like autonomous driving and medical imaging.
