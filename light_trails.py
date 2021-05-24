import cv2
import trail_type
import background_substraction
import alfa_img
import numpy as np
import time

def main(input_file, painting_method, infinite_trail, shadow_length, background_learn_frames, substraction_method, threshold_level, show_background,
         inverted_trail, paint_last_frame, bad_file, fps_val, source_fps, var_min, var_max, var_threshold, output_file_dir, color_normal, avrg_gain):
    if infinite_trail:
        trail_length = -1
    else:
        trail_length = shadow_length

    actual_time = time.strftime("%Y%m%d-%H%M%S")
    in_video = cv2.VideoCapture(input_file)
    if in_video.isOpened() == True:
        bad_file = False
        frame_height = int(in_video.get(4))
        frame_width = int(in_video.get(3))
        if source_fps == True:
            fps = int(in_video.get(cv2.CAP_PROP_FPS))
        else:
            fps = fps_val
        out_video = cv2.VideoWriter(output_file_dir+"/Light" + actual_time +".mp4",cv2.VideoWriter_fourcc('M','P','G','4'), fps, (frame_width,frame_height))

        if inverted_trail:
            actual_trail_sequence = trail_type.inverted_echo(trail_length, frame_width, frame_height,paint_last_frame,painting_method)
        else:
            actual_trail_sequence = trail_type.standard_echo(trail_length, frame_width, frame_height,paint_last_frame,painting_method)

        if substraction_method == "Background substraction":
            substraction = background_substraction.MOG2_substractor(in_video, background_learn_frames, var_min, var_max, var_threshold)
            if show_background:
                bckgd = np.zeros((frame_height,frame_width,3),dtype=np.uint8)
                bckgd = cv2.BackgroundSubtractor.getBackgroundImage(substraction.MOG2)
                actual_trail_sequence.background = bckgd
        elif substraction_method == "Thresholding":
            substraction = background_substraction.threshold_substractor(threshold_level)
        elif substraction_method == "Simple sum":
            substraction = background_substraction.no_substractor()

        cv2.namedWindow("Test",cv2.WINDOW_NORMAL)

        while(in_video.isOpened()):
            ret, input_frame =  in_video.read()
            if ret==True:
                foreground = alfa_img.Alfa_img(input_frame, substraction.generate_mask(input_frame))
                actual_trail_sequence.update(foreground)
                final_img = np.zeros_like(input_frame).astype(np.uint8)
                final_img = actual_trail_sequence.paint_function(final_img, color_normal, avrg_gain)
                out_video.write(final_img)
                cv2.imshow("Test",final_img)
                if cv2.waitKey(1) == 27:
                    break
            else:
                break
        in_video.release()
        out_video.release()
        cv2.destroyAllWindows()
        return bad_file
    else:
        bad_file = True
        return bad_file




