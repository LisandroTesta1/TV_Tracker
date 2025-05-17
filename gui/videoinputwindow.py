import queue

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap

from gui.templates.videodisplaywidget import Ui_VideoDisplay
from gui.video_processing.frame_formatter import FrameFormatter
from gui.video_processing.input_video_stream import InputVideoStream
from gui.video_processing.frame_processing import FrameProcessor


class VideoInputWindow(QWidget, Ui_VideoDisplay):
    """
    GUI for displying video and tracking results
    """

    # Signal declaration for new target selection
    new_selection_signal = pyqtSignal(tuple)
    closed_window_signal = pyqtSignal()
    zoom_control_signal = pyqtSignal(int)

    def __init__(self, video_source=None, parent=None):
        """
        Class constructor

        Parameters
        ----------
        video_source:
            The name of the input video source
        parent:

        """
        super(VideoInputWindow, self).__init__(parent)
        self.setupUi(self)
        self.videosource = video_source

    def initUi(self):
        # Queues for communication between threads
        self.q_videoInput = queue.Queue(128)
        self.q_videoProcessed = queue.Queue(128)
        # Threads for video processing
        # self.th_videoIn = VideoInput(self.videosource, self.q_videoInput)
        # self.th_videoIn = VideoInput(self.videosource)
        self.th_videoIn = InputVideoStream(self.videosource, self.q_videoInput)
        self.th_tracker = FrameProcessor(
            self.q_videoInput, self.q_videoProcessed
        )
        self.th_frameFormatter = FrameFormatter(self.q_videoProcessed)
        self.th_frameFormatter.change_pixmap_signal.connect(self.setImage)
        # Connect signals to slots
        self.frameDisplay.mousePressEvent = self.getPixelPos
        self.frameDisplay.wheelEvent = self.getWheelEvent
        self.new_selection_signal.connect(self.th_tracker.new_selection)
        # self.th_tracker.currentFPS.connect(self.setFPS)
        self.th_videoIn.frame_dimensions_signal.connect(
            self.resizeFrameDisplay
        )
        self.th_videoIn.frame_dimensions_signal.connect(
            self.th_tracker.set_frame_size
        )
        self.closed_window_signal.connect(self.th_tracker.finish_processing)
        self.closed_window_signal.connect(
            self.th_videoIn.finish_input_video_stream
        )
        # self.th_frameFormatter.changePixmap.connect(self.setImage)
        # Start threads execution
        self.th_videoIn.start()
        self.th_tracker.start()
        self.th_frameFormatter.start()

    def closeEvent(self, event):
        self.th_tracker.exit()
        self.th_videoIn.exit()
        self.th_frameFormatter.exit()
        del self.q_videoInput
        del self.q_videoProcessed
        event.accept()
        self.closed_window_signal.emit()

    def getPixelPos(self, event):
        x = event.x()
        y = event.y()
        print("x={}, y={}".format(x, y))
        self.new_selection_signal.emit((x, y))

    def getWheelEvent(self, event):
        delta = event.angleDelta().y() // 120
        modifiers = QApplication.keyboardModifiers()
        if modifiers == QtCore.Qt.ControlModifier:
            delta *= 10
        self.zoom_control_signal.emit(delta)

    def setVideoSource(self, videosource):
        self.videosource = videosource

    @pyqtSlot(QImage)
    def setImage(self, image):
        # FIXME: This sentence throws Segmentation Fault ('core dumped')
        # if(image is not None):
        self.frameDisplay.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(int, int)
    def resizeFrameDisplay(self, width, height):
        self.frameDisplay.resize(width, height)
        self.resize(width, height)
