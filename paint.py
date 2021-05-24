import cv2
import numpy as np

def paint_mode(style, target_frame, frame_in, index, trail_size, average_multiplier):
    if style == "Copy":
        target_frame = frame_in.apply_mask(target_frame)
    elif style == "Accumulation":
        cv2.accumulate(frame_in.entire_img, target_frame, frame_in.mask)
    elif style == "Fading copy":
        weight = np.divide(index, trail_size)
        weighted_frame = np.multiply(frame_in.entire_img, weight)
        mask_3ch = cv2.cvtColor(frame_in.mask, cv2.COLOR_GRAY2BGR)
        target_frame[mask_3ch > 0] = 0
        target_frame += weighted_frame * (mask_3ch > 0)
    elif style == "Weighted accumulate (OpenCV function)":
        weight = np.divide(index, trail_size)
        cv2.accumulateWeighted(frame_in.entire_img, target_frame, weight, frame_in.mask)
    elif style == "Fading accumulation":
        weight = np.divide(index, trail_size)
        weighted_frame = np.multiply(frame_in.entire_img, weight)
        weighted_frame = weighted_frame.astype(np.float32)
        cv2.accumulate(weighted_frame, target_frame, frame_in.mask)
    elif style == "Average":
        weight = (float(1) / trail_size)+float(1 - float(1)/trail_size)*average_multiplier
        cv2.accumulateWeighted(frame_in.entire_img, target_frame, weight, frame_in.mask)
    return target_frame

def normalize(input_array,normalize):
    input_array = np.divide(input_array,255)
    max = np.amax(input_array)
    if max > 1:
        if normalize == True:
            max_pixel_val = 0
            array_height, array_width, num_channels = input_array.shape
            for i in range(array_height):
                for j in range(array_width):
                    max_pixel_val = np.amax(input_array[i,j])
                    if max_pixel_val > 1:
                        input_array[i,j,:] = np.divide(input_array[i,j,:],max_pixel_val)
        else:
            input_array[input_array > 1] = 1
    return input_array
