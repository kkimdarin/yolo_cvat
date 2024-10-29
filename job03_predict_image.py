from ultralytics import YOLO


model = YOLO("best.pt")
model.predict(source='21.jpg', save=True)  # 추론 및 결과 저장
