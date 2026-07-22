from ultralytics import YOLO

# Load the trained model weights
model = YOLO('path/to/best.pt')

# Run inference on a sample image
results = model.predict(source='sample.jpg', conf=0.30)

# Save or display results
results[0].show()
