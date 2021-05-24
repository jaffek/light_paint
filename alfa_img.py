import cv2
import numpy as np

class Alfa_img():
    def __init__(self, data_in, mask_in):
        self.entire_img = data_in
        self.mask = mask_in

    def apply_mask(self, destination):
        self.converted_data = self.entire_img
        self.mask_3ch = cv2.cvtColor(self.mask, cv2.COLOR_GRAY2BGR)
        destination[self.mask_3ch>0]=0
        destination += self.converted_data*(self.mask_3ch>0)
        return destination

    @classmethod
    def sized_frame(cls,frame_width,frame_height):
        data = np.zeros((frame_height,frame_width,3),dtype=np.uint8)
        mask = np.zeros((frame_height,frame_width),dtype=np.uint8)
        return cls(data, mask)

    @classmethod
    def one_frame(cls, frame_data):
        temp_data = frame_data
        temp_mask = None
        return cls(temp_data,temp_mask)
