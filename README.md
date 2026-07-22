# Helmet Detection System using YOLOv8

An end-to-end Computer Vision pipeline built with YOLOv8 to detect helmet usage.Our classes are `With Helmet` vs `Without Helmet`.


# Visual Results & Detections

Below are sample inference outputs evaluated on the validation dataset:


# Performance Metrics

The model was trained for 25 epochs using `YOLOv8n` backbone on a custom annotated dataset.

mAP@50 = 0.844
Precision = 0.806
Recall = 0.811
mAP@50-95 = 0.491

| Class | Precision | Recall | mAP@50 |
|With Helmet| 0.842 | 0.889 | 0.896 |
|Without Helmet| 0.769 | 0.733 | 0.793 |


# Tech Stack & Tools
* **Core Framework:** PyTorch
* **Model Architecture:** YOLOv8 (Ultralytics)
* **Computer Vision:** OpenCV, PIL
* **Data Annotations:** PASCAL VOC (XML) converted to YOLO format
The model is trained on google colab NVIDIA Tesla T4 GPU.Data annotation format was XML that we converted to YOLO txt format.
