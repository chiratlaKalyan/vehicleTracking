from ultralytics import YOLO

# Load the model.
model = YOLO('../support/yolov8n_best.pt')

# Training.
results = model.train(
    data='datasets/cars/data.yaml',
    imgsz=640,
    epochs=50,
    batch=8,
    name='yolov8n_cars_custom'
)