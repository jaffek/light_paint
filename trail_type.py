import echo
import paint

class standard_echo(echo.Echo):
    def __init__(self,trail_length, frame_width, frame_height,show_last_frame,painting_style):
        super().__init__(trail_length, frame_width, frame_height,show_last_frame,painting_style)

    def iterate(self, target_frame, paint_style, avg):
        for self.iterator in range(len(self.trail_sequence)):
            target_frame = paint.paint_mode(paint_style, target_frame, self.trail_sequence[self.iterator], self.iterator, len(self.trail_sequence), avg)
        return target_frame

class inverted_echo(echo.Echo):
    def __init__(self,trail_length, frame_width, frame_height,show_last_frame,painting_style):
        super().__init__(trail_length, frame_width, frame_height,show_last_frame,painting_style)

    def iterate(self, target_frame, paint_style, avg):
        self.counter = 0
        for self.iterator  in reversed(range(len(self.trail_sequence))):
            target_frame = paint.paint_mode(paint_style, target_frame, self.trail_sequence[self.iterator], self.counter, len(self.trail_sequence), avg)
            self.counter += 1
        return target_frame
