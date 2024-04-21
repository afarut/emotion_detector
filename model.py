from ultralytics import YOLO
import numpy as np
import cv2 as cv
from transformers import EfficientNetImageProcessor, EfficientNetForImageClassification


class EmotionDetector:
    emoji_names = {0: 'angry.jpg',
                   1: 'disgusted.jpg',
                   2: 'fearful.jpg',
                   3: 'happy.jpg',
                   4: 'neutral.jpg',
                   5: 'sad.jpg',
                   6: 'surprised.jpg'}

    emoji_size = 50
    frame_size = 200
    n = 10
    def __init__(self):
        self.yolo = YOLO('yolo.pth')
        self.effishnet = EfficientNetForImageClassification.from_pretrained("google/efficientnet-b3")
        self.effishnet.classifier.out_features = 7
        self.effishnet.load_state_dict(torch.load('effish.pth'))

        # get classes - self.yolo(array)[index].boxes.cls
        # get coords - self.yolo(array)[index].boxes.xyxy

    def to(self, device):
        self.yolo = self.yolo.to(device)
        # Add layers
        return self


    def combine(layer, emoji, x, y):
        for i in range(emoji.shape[0]):
            for j in range(emoji.shape[1]):
                if np.sum(emoji[i][j]) < 620:
                    if x + j < layer.shape[1] and y + i < layer.shape[0]:
                        layer[y + i, x + j] = emoji[i][j]


    def __call__(self, file_path):
        if file_path: # is video
            pass
        else: # is audio only
            pass

    def video_cycle(self, file_path):
        cap = cv.VideoCapture(file_path)
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter('output.avi', fourcc, 20.0, (self.frame_size, self.frame_size))
        total_frames = 0
        while cap.isOpened():
            total_frames += 1
            ret, frame = cap.read()
            coords = self.yolo(array)[0].boxes.xyxy
            frame = cv.resize(frame, (self.frame_size, self.frame_size))
            emojis = []
            if total_frames % n == 0:
                for xy in coords:
                    x1, y1, x2, y2 = xy.numpy()
                    face = frame[x1:x2, y1:y2]

                    pred = efishnet(face)
                    emotion = torch.argmax(pred).item
                    emoji_path = self.emoji_names[emotion]
                    emoji = cv.resize(cv.imread(emoji_path), (self.emoji_size, self.emoji_size))
                    emojis.append(emoji)

                for emoji in emojis:
                    combine(frame, emoji, 0, 0)

                out.write(frame)

        cap.release()



