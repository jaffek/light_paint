from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLineEdit,  QSlider, QLabel, QComboBox, QCheckBox, QSpinBox, QMessageBox, QGroupBox, QDoubleSpinBox
from PyQt5.QtCore import Qt
import light_trails

class Lightapp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Light Painting Video')
        self.setGeometry(300, 300, 900, 400)

        self.bckg_group()
        self.browse_open()
        self.create_button()
        self.browse_open_box()
        self.paint_method_list()
        self.infinite_trail_check()
        self.trail_length_spinbox_setter()
        self.light_detection_list()
        self.threshold_spinbox_setter()
        self.show_background_check()
        self.reverse_trail_check()
        self.redraw_frame_check()
        self.invalid_file = False
        self.learn_bckg_spinbox_setter()
        self.fps_setter()
        self.source_frame_setter()
        self.var_min_spinbox_setter()
        self.var_max_spinbox_setter()
        self.var_threshold_spinbox_setter()
        self.stop_processing_label()
        self.reset_button()
        self.browse_save()
        self.browse_save_box()
        self.normalize_colors_check()
        self.average_gain_spinbox_setter()

# BUTTONS   ###############################################

    def browse_open(self):
        self.browse_open_button = QPushButton("Open", self)
        self.browse_open_button.setGeometry(500, 10, 60, 32)
        self.browse_open_button.setObjectName("browseOpenButton")
        self.browse_open_button.clicked.connect(self.file_open)

    def browse_save(self):
        self.browse_save_button = QPushButton("Export directory", self)
        self.browse_save_button.setGeometry(500, 290, 100, 32)
        self.browse_save_button.setObjectName("browseSaveButton")
        self.browse_save_button.clicked.connect(self.file_save)

    def create_button(self):
        self.createButton = QPushButton("Create video", self)
        self.createButton.setGeometry(750, 350, 100, 30)
        self.createButton.setObjectName("createButton")
        self.createButton.clicked.connect(self.start)

    def reset_button(self):
        self.createButton = QPushButton("Reset parameters", self)
        self.createButton.setGeometry(630, 350, 100, 30)
        self.createButton.setObjectName("resetButton")
        self.createButton.clicked.connect(self.reset_action)

# CHECKBOXES   ###############################################

    def show_background_check(self):
        self.show_background_checkbox = QCheckBox(self)
        self.show_background_checkbox.move(750, 95)
        self.show_background_checkbox.setChecked(True)
        self.show_background_checkbox_label = QLabel("Show background", self)
        self.show_background_checkbox_label.setGeometry(770, 95, 85, 30)

    def reverse_trail_check(self):
        self.reverse_trail_checkbox = QCheckBox(self)
        self.reverse_trail_checkbox.move(750, 125)
        self.reverse_trail_checkbox.setChecked(False)
        self.reverse_trail_checkbox.setEnabled(False)
        self.reverse_trail_checkbox_label = QLabel("Reverse trail", self)
        self.reverse_trail_checkbox_label.setGeometry(770, 125, 85, 30)

    def redraw_frame_check(self):
        self.redraw_frame_checkbox = QCheckBox(self)
        self.redraw_frame_checkbox.move(750, 155)
        self.redraw_frame_checkbox.setChecked(False)
        self.redraw_frame_checkbox_label = QLabel("Redraw last frame", self)
        self.redraw_frame_checkbox_label.setGeometry(770, 155, 105, 30)

    def source_frame_setter(self):
        self.source_frame_checkbox = QCheckBox(self)
        self.source_frame_checkbox.move(550, 230)
        self.source_frame_checkbox.setChecked(True)
        self.source_frame_checkbox_label = QLabel("Source framerate", self)
        self.source_frame_checkbox_label.setGeometry(570, 230, 105, 30)
        self.source_frame_checkbox.stateChanged.connect(self.framerate_control)


    def infinite_trail_check(self):
        self.infinite_trail_checkbox = QCheckBox("Infinite trail",self)
        self.infinite_trail_checkbox.move(750, 65)
        self.infinite_trail_checkbox.setChecked(False)
        self.infinite_trail_checkbox.stateChanged.connect(self.trail_length_control)

    def normalize_colors_check(self):
        self.normalize_colors_checkbox = QCheckBox(self)
        self.normalize_colors_checkbox.move(750, 185)
        self.normalize_colors_checkbox.setChecked(False)
        self.source_frame_checkbox_label = QLabel("Normalize colors", self)
        self.source_frame_checkbox_label.setGeometry(770, 185, 105, 30)

# SPINBOXES   ###############################################

    def trail_length_spinbox_setter(self):
        self.trail_length_box = QSpinBox(self)
        self.trail_length_box.setMinimum(1)
        self.trail_length_box.setMaximum(500)
        self.trail_length_box.setValue(25)
        self.trail_length_box.setEnabled(True)
        self.trail_length_box.setGeometry(375, 147, 50, 25)
        self.trail_length_box_label = QLabel("Trail length:", self)
        self.trail_length_box_label.setGeometry(315, 145, 60, 30)

    def threshold_spinbox_setter(self):
        self.threshold_box = QSpinBox(self)
        self.threshold_box.setMinimum(0)
        self.threshold_box.setMaximum(255)
        self.threshold_box.setValue(10)
        self.threshold_box.setEnabled(False)
        self.threshold_box.setGeometry(670, 77, 50, 25)
        self.threshold_box_label = QLabel("Threshold:", self)
        self.threshold_box_label.setGeometry(615, 75, 70, 30)

    def var_min_spinbox_setter(self):
        self.var_min_box = QSpinBox(self)
        self.var_min_box.setMinimum(0)
        self.var_min_box.setMaximum(200)
        self.var_min_box.setValue(4)
        self.var_min_box.setEnabled(True)
        self.var_min_box.setGeometry(300, 77, 50, 25)
        self.var_min_box_label = QLabel("varMin:", self)
        self.var_min_box_label.setGeometry(260, 75, 40, 30)

    def var_max_spinbox_setter(self):
        self.var_max_box = QSpinBox(self)
        self.var_max_box.setMinimum(0)
        self.var_max_box.setMaximum(200)
        self.var_max_box.setValue(75)
        self.var_max_box.setEnabled(True)
        self.var_max_box.setGeometry(405, 77, 50, 25)
        self.var_max_box_label = QLabel("varMax:", self)
        self.var_max_box_label.setGeometry(360, 75, 40, 30)

    def var_threshold_spinbox_setter(self):
        self.var_threshold_box = QSpinBox(self)
        self.var_threshold_box.setMinimum(0)
        self.var_threshold_box.setMaximum(200)
        self.var_threshold_box.setValue(16)
        self.var_threshold_box.setEnabled(True)
        self.var_threshold_box.setGeometry(535, 77, 50, 25)
        self.var_threshold_box_label = QLabel("varThreshold:", self)
        self.var_threshold_box_label.setGeometry(465, 75, 70, 30)

    def learn_bckg_spinbox_setter(self):
        self.learn_bcg_frames = QSpinBox(self)
        self.learn_bcg_frames.setMinimum(0)
        self.learn_bcg_frames.setMaximum(1000)
        self.learn_bcg_frames.setValue(25)
        self.learn_bcg_frames.setEnabled(True)
        self.learn_bcg_frames.setGeometry(540, 147, 50, 25)
        self.learn_bcg_frames_label = QLabel("Number of frames\nto learn background:", self)
        self.learn_bcg_frames_label.setGeometry(435, 145, 100, 30)

    def average_gain_spinbox_setter(self):
        self.average_gain = QDoubleSpinBox(self)
        self.average_gain.setMinimum(0)
        self.average_gain.setMaximum(1)
        self.average_gain.setValue(0)
        self.average_gain.setDecimals(2)
        self.average_gain.setSingleStep(0.01)
        self.average_gain.setEnabled(False)
        self.average_gain.setGeometry(670, 147, 50, 25)
        self.average_gain_label = QLabel("Average gain:", self)
        self.average_gain_label.setGeometry(600, 145, 70, 30)

# COMBOBOXES (LISTS)   ###############################################

    def paint_method_list(self):
        self.paint_method = QComboBox(self)
        self.paint_method.setGeometry(100, 145, 210, 30)
        self.paint_method.addItem("Copy")
        self.paint_method.addItem("Accumulation")
        self.paint_method.addItem("Fading copy")
        self.paint_method.addItem("Weighted accumulate (OpenCV function)")
        self.paint_method.addItem("Fading accumulation")
        self.paint_method.addItem("Average")
        self.paint_method_label = QLabel("Painting method:", self)
        self.paint_method_label.setGeometry(10, 145, 85, 30)
        self.paint_method.currentIndexChanged.connect(self.infinite_checkbox_control)

    def light_detection_list(self):
        self.light_detection_method = QComboBox(self)
        self.light_detection_method.setGeometry(100, 75, 150, 30)
        self.light_detection_method.addItem("Background substraction")
        self.light_detection_method.addItem("Thresholding")
        self.light_detection_method.addItem("Simple sum")
        self.light_detection_method_label = QLabel("Light detection\nmethod:", self)
        self.light_detection_method_label.setGeometry(10, 75, 85, 30)
        self.light_detection_method.currentIndexChanged.connect(self.widget_disbler)

# INTERACTIVE TEXTBOXES   ###############################################

    def browse_open_box(self):
        self.browse_open_textbox = QLineEdit(self)
        self.browse_open_textbox.setEnabled(True)
        self.browse_open_textbox.resize(480, 30)
        self.browse_open_textbox.move(10, 10)
        self.browse_open_textbox.setGeometry(10, 10, 480, 30)
        self.browse_open_textbox.setObjectName("openTextBox")

    def browse_save_box(self):
        self.browse_save_textbox = QLineEdit(self)
        self.browse_save_textbox.setEnabled(True)
        self.browse_save_textbox.resize(480, 30)
        self.browse_save_textbox.move(10, 10)
        self.browse_save_textbox.setGeometry(10, 290, 480, 30)
        self.browse_save_textbox.setObjectName("saveTextBox")

# SLIDERS   ###############################################

    def fps_setter(self):
        self.fps_output_video = QSlider(Qt.Horizontal, self)
        self.fps_output_video.setGeometry(80,230, 450, 30)
        self.fps_output_video.setMinimum(1)
        self.fps_output_video.setMaximum(200)
        self.fps_output_video.setValue(25)
        self.fps_output_video.setEnabled(False)
        self.fps_output_video.setTickPosition(QSlider.TicksBelow)
        self.fps_output_video.setTickInterval(1)
        self.fps_output_video.valueChanged.connect(self.fps_slider_val)
        self.fps_output_video_label = QLabel("Output FPS:", self)
        self.fps_output_video_label.setGeometry(10, 225, 70, 30)
        self.fps_output_video_value = QLabel("Source", self)
        self.fps_output_video_value.move(298, 200)

# LABELS/MESSAGES   ###############################################

    def stop_processing_label(self):
        self.stop_label = QLabel("ESC to stop processing", self)
        self.stop_label.setGeometry(500, 350, 150, 30)

    def bckg_group(self):
        self.bckg_parameters = QGroupBox("Background substraction parameters:",self)
        self.bckg_parameters.setGeometry(255,55,335,55)

    def error_open_window_directory(self):
        QMessageBox.about(self,"Error", "Invalid file!")

    def error_save_window_directory(self):
        QMessageBox.about(self, "Error", "Invalid directory!")

    def show_error_directory(self):
        self.error_dir_window.showMessage("Invalid file")

# ACTIONS   ###############################################

    def reset_action(self):
        self.show_background_checkbox.setChecked(True)
        self.reverse_trail_checkbox.setChecked(False)
        self.redraw_frame_checkbox.setChecked(False)
        self.source_frame_checkbox.setChecked(True)
        self.infinite_trail_checkbox.setChecked(False)
        self.normalize_colors_checkbox.setChecked(False)
        self.trail_length_box.setValue(25)
        self.trail_length_box.setEnabled(True)
        self.threshold_box.setValue(10)
        self.threshold_box.setEnabled(False)
        self.var_min_box.setValue(4)
        self.var_min_box.setEnabled(True)
        self.var_max_box.setValue(75)
        self.var_max_box.setEnabled(True)
        self.var_threshold_box.setValue(16)
        self.var_threshold_box.setEnabled(True)
        self.learn_bcg_frames.setValue(25)
        self.learn_bcg_frames.setEnabled(True)
        self.paint_method.setCurrentIndex(0)
        self.light_detection_method.setCurrentIndex(0)
        self.fps_output_video.setValue(25)
        self.fps_output_video.setEnabled(False)
        self.average_gain.setValue(0)
        self.average_gain.setEnabled(False)
        self.reverse_trail_checkbox.setChecked(False)
        self.reverse_trail_checkbox.setEnabled(False)
        self.fps_output_video_value.setText("Source")

    def framerate_control(self):
        if self.source_frame_checkbox.isChecked():
            self.fps_output_video.setEnabled(False)
            self.fps_output_video_value.setText("Source")
        else:
            self.fps_output_video.setEnabled(True)
            self.fps_output_video.setValue(25)
            self.fps_output_video_value.setText(str(25))

    def infinite_checkbox_control(self):
        if self.paint_method.currentIndex() == 2 or self.paint_method.currentIndex() == 3 or self.paint_method.currentIndex() == 4 or self.paint_method.currentIndex() == 5:
            self.infinite_trail_checkbox.setChecked(False)
            self.infinite_trail_checkbox.setEnabled(False)
        else:
            self.infinite_trail_checkbox.setEnabled(True)
            self.infinite_trail_checkbox.setChecked(False)

        if self.paint_method.currentIndex() == 2 or self.paint_method.currentIndex() == 3 or self.paint_method.currentIndex() == 4:
            self.reverse_trail_checkbox.setChecked(False)
            self.reverse_trail_checkbox.setEnabled(True)
        else:
            self.reverse_trail_checkbox.setChecked(False)
            self.reverse_trail_checkbox.setEnabled(False)

        if self.paint_method.currentIndex() == 5:
            self.average_gain.setEnabled(True)
            self.average_gain.setValue(0)
        else:
            self.average_gain.setEnabled(False)
            self.average_gain.setValue(0)


    def trail_length_control(self):
        if self.infinite_trail_checkbox.isChecked():
            self.trail_length_box.setEnabled(False)
        else:
            self.trail_length_box.setEnabled(True)
            self.trail_length_box.setValue(25)

    def widget_disbler(self):
        if self.light_detection_method.currentIndex() == 1:
            self.threshold_box.setEnabled(True)
            self.learn_bcg_frames.setEnabled(False)
            self.var_min_box.setEnabled(False)
            self.show_background_checkbox.setEnabled(False)
            self.show_background_checkbox.setChecked(False)
            self.var_max_box.setEnabled(False)
            self.threshold_box.setValue(10)
            self.var_threshold_box.setEnabled(False)
        elif self.light_detection_method.currentIndex() == 0:
            self.threshold_box.setEnabled(False)
            self.learn_bcg_frames.setEnabled(True)
            self.var_min_box.setEnabled(True)
            self.var_max_box.setEnabled(True)
            self.var_threshold_box.setEnabled(True)
            self.show_background_checkbox.setEnabled(True)
            self.show_background_checkbox.setChecked(True)
            self.var_min_box.setValue(4)
            self.var_max_box.setValue(75)
            self.var_threshold_box.setValue(16)
        elif self.light_detection_method.currentIndex() == 2:
            self.threshold_box.setEnabled(False)
            self.learn_bcg_frames.setEnabled(False)
            self.show_background_checkbox.setEnabled(False)
            self.show_background_checkbox.setChecked(False)
            self.var_min_box.setEnabled(False)
            self.var_max_box.setEnabled(False)
            self.var_threshold_box.setEnabled(False)

    def file_open(self):
        self.directory_open = QFileDialog.getOpenFileName(self, 'Open file','/home')
        self.browse_open_textbox.setText(self.directory_open[0])

    def file_save(self):
        self.directory_save = QFileDialog.getExistingDirectory(self, 'Select directory','/home')
        self.browse_save_textbox.setText(self.directory_save)

    def fps_slider_val(self):
        self.delay = self.fps_output_video.value()
        self.fps_output_video_value.setText(str(self.delay))

    def start(self):
        if self.browse_open_textbox.text() == "":
            self.error_open_window_directory()
        elif self.browse_save_textbox.text() == "":
            self.error_save_window_directory()
        else:
            self.invalid_file = light_trails.main(self.browse_open_textbox.text(), self.paint_method.currentText(), self.infinite_trail_checkbox.isChecked(),
                          self.trail_length_box.value(),self.learn_bcg_frames.value(),self.light_detection_method.currentText(),
                          self.threshold_box.value(),self.show_background_checkbox.isChecked(),self.reverse_trail_checkbox.isChecked(),
                          self.redraw_frame_checkbox.isChecked(),self.invalid_file,self.fps_output_video.value(),self.source_frame_checkbox.isChecked(),
                          self.var_min_box.value(),self.var_max_box.value(),self.var_threshold_box.value(),self.browse_save_textbox.text(),
                          self.normalize_colors_checkbox.isChecked(),self.average_gain.value())
        if self.invalid_file == True:
            self.error_window_directory()