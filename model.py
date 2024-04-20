from ultralytics import YOLO


class EmotionDetector:
	def __init__(self):
		self.layer1 = YOLO('yolo.pth')
		# get classes - self.layer1(array)[index].boxes.cls
		# get coords - self.layer1(array)[index].boxes.xyxy

	def to(self, device):
		self.layer1 = self.layer1.to(device)
		# Add layers
		return self