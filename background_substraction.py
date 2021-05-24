import cv2
import numpy as np

class MOG2_substractor():
    def __init__(self, in_video, frames_amount, var_minimum, var_maximum, var_thres):
        self.MOG2 = cv2.createBackgroundSubtractorMOG2()
        self.MOG2.setVarMin(var_minimum)
        self.MOG2.setVarMax(var_maximum)
        self.MOG2.setVarThreshold(var_thres)
        self.frgrnd_mask = None
        for i in range(frames_amount):
            self.ret, self.background = in_video.read()
            self.frgrnd_mask = self.MOG2.apply(self.background)

    def generate_mask(self, frame):
        self.frgrnd_mask = self.MOG2.apply(frame, 0, 0)
        self.kernel = np.ones((3, 3), np.uint8)
        self.frgrnd_mask = cv2.erode(self.frgrnd_mask, self.kernel)
        self.frgrnd_mask = cv2.dilate(self.frgrnd_mask, self.kernel)
        self.ret, self.frgrnd_mask = cv2.threshold(self.frgrnd_mask, 0, 255, cv2.THRESH_OTSU)
        self.frgrnd_mask = cv2.medianBlur(self.frgrnd_mask, 9)
        return self.frgrnd_mask


class threshold_substractor():
    def __init__(self, thres_val):
        self.threshold = thres_val

    def generate_mask(self, frame):
        self.grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.ret, self.frame_mask = cv2.threshold(self.grayscale_img, self.threshold, 255, cv2.THRESH_TOZERO)
        return self.frame_mask


class no_substractor():
    def generate_mask(self, frame):
        self.img_height, self.img_width, self.channels = frame.shape
        self.frgrd_mask = np.ones((self.img_height, self.img_width), dtype=np.uint8)
        return self.frgrd_mask