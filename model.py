from ultralytics import YOLO


class EmotionDetector:
	def __init__(self):
		self.yolo = YOLO('yolo.pth')
		# get classes - self.yolo(array)[index].boxes.cls
		# get coords - self.yolo(array)[index].boxes.xyxy

	def to(self, device):
		self.yolo = self.yolo.to(device)
		# Add layers
		return self

	def __call__(self, file_path):
		if file_path: # is video
			pass
		else: # is audio only
			pass