import alfa_img
import cv2
import numpy as np
import paint

class Echo():
    def __init__(self, trail_length, frame_width, frame_height,show_last_frame,painting_style):
        self.background = np.zeros((frame_height,frame_width,3),dtype=np.uint8)
        self.paint_last_frame = False
        self.paint_method = "Copy"
        self.permanent = False
        self.trail_sequence = []
        self.paint_last_frame = show_last_frame
        self.paint_method = painting_style

        if trail_length < 0:
            self.permanent = True
            self.background = np.zeros((frame_height,frame_width,3),dtype=np.uint8)
        if trail_length < 1:
            trail_length = 1
        for i in range(trail_length):
            self.trail_sequence.append(alfa_img.Alfa_img.sized_frame(frame_width, frame_height))

    def iterate(self):
        pass

    def update(self,new_frame):
        del self.trail_sequence[0]
        self.trail_sequence.append(new_frame)

    def paint_function(self, target_frame, color_normalizator, avg_gain):
        self.float_target = None
        if self.background.any():
            self.float_target = self.background.astype(np.float32)
        else:
            self.float_target = target_frame.astype(np.float32)
        self.float_target = self.iterate(self.float_target, self.paint_method, avg_gain)

        self.float_target = paint.normalize(self.float_target, color_normalizator) * 255
        target_frame = self.float_target.astype(np.uint8)

        if self.paint_last_frame:
            self.current_frame = self.trail_sequence[-1]
            self.mask_3ch = cv2.cvtColor(self.current_frame.mask, cv2.COLOR_GRAY2BGR)
            target_frame[self.mask_3ch > 0] = 0
            target_frame += self.current_frame.entire_img * (self.mask_3ch > 0)
        if self.permanent:
            self.background = self.float_target.astype(np.uint8)
        return target_frame
