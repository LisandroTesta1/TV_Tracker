# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameracontrolpanel.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CameraControlWidget(object):
    def setupUi(self, CameraControlWidget):
        CameraControlWidget.setObjectName("CameraControlWidget")
        CameraControlWidget.resize(202, 344)
        self.camOnOffButton = QtWidgets.QPushButton(CameraControlWidget)
        self.camOnOffButton.setEnabled(True)
        self.camOnOffButton.setGeometry(QtCore.QRect(20, 290, 161, 29))
        self.camOnOffButton.setObjectName("camOnOffButton")
        self.camZoomSlider = QtWidgets.QSlider(CameraControlWidget)
        self.camZoomSlider.setEnabled(True)
        self.camZoomSlider.setGeometry(QtCore.QRect(40, 30, 17, 160))
        self.camZoomSlider.setMaximum(16384)
        self.camZoomSlider.setOrientation(QtCore.Qt.Vertical)
        self.camZoomSlider.setObjectName("camZoomSlider")
        self.zoomLabel = QtWidgets.QLabel(CameraControlWidget)
        self.zoomLabel.setGeometry(QtCore.QRect(20, 200, 54, 17))
        self.zoomLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.zoomLabel.setObjectName("zoomLabel")
        self.camFocusSlider = QtWidgets.QSlider(CameraControlWidget)
        self.camFocusSlider.setEnabled(True)
        self.camFocusSlider.setGeometry(QtCore.QRect(130, 30, 17, 160))
        self.camFocusSlider.setOrientation(QtCore.Qt.Vertical)
        self.camFocusSlider.setObjectName("camFocusSlider")
        self.camFocusLabel = QtWidgets.QLabel(CameraControlWidget)
        self.camFocusLabel.setGeometry(QtCore.QRect(120, 200, 41, 17))
        self.camFocusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.camFocusLabel.setObjectName("camFocusLabel")

        self.retranslateUi(CameraControlWidget)
        QtCore.QMetaObject.connectSlotsByName(CameraControlWidget)

    def retranslateUi(self, CameraControlWidget):
        _translate = QtCore.QCoreApplication.translate
        CameraControlWidget.setWindowTitle(_translate("CameraControlWidget", "Form"))
        self.camOnOffButton.setText(_translate("CameraControlWidget", "On/Off"))
        self.zoomLabel.setText(_translate("CameraControlWidget", "Zoom"))
        self.camFocusLabel.setText(_translate("CameraControlWidget", "Focus"))
