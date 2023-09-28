import sys
import time
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QApplication,QWidget, QFrame, QGridLayout, QLabel
from PyQt5.QtCore import QRect, QSize, QMetaObject, QCoreApplication, Qt
from PyQt5 import QtCore, QtGui, QtWidgets

qt_resource_data = b"\
\x00\x00\x07\xb8\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x18\x00\x00\x00\x18\x08\x06\x00\x00\x00\xe0\x77\x3d\xf8\
\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x16\x25\x00\x00\x16\x25\
\x01\x49\x52\x24\xf0\x00\x00\x05\xf1\x69\x54\x58\x74\x58\x4d\x4c\
\x3a\x63\x6f\x6d\x2e\x61\x64\x6f\x62\x65\x2e\x78\x6d\x70\x00\x00\
\x00\x00\x00\x3c\x3f\x78\x70\x61\x63\x6b\x65\x74\x20\x62\x65\x67\
\x69\x6e\x3d\x22\xef\xbb\xbf\x22\x20\x69\x64\x3d\x22\x57\x35\x4d\
\x30\x4d\x70\x43\x65\x68\x69\x48\x7a\x72\x65\x53\x7a\x4e\x54\x63\
\x7a\x6b\x63\x39\x64\x22\x3f\x3e\x20\x3c\x78\x3a\x78\x6d\x70\x6d\
\x65\x74\x61\x20\x78\x6d\x6c\x6e\x73\x3a\x78\x3d\x22\x61\x64\x6f\
\x62\x65\x3a\x6e\x73\x3a\x6d\x65\x74\x61\x2f\x22\x20\x78\x3a\x78\
\x6d\x70\x74\x6b\x3d\x22\x41\x64\x6f\x62\x65\x20\x58\x4d\x50\x20\
\x43\x6f\x72\x65\x20\x35\x2e\x36\x2d\x63\x31\x34\x38\x20\x37\x39\
\x2e\x31\x36\x34\x30\x33\x36\x2c\x20\x32\x30\x31\x39\x2f\x30\x38\
\x2f\x31\x33\x2d\x30\x31\x3a\x30\x36\x3a\x35\x37\x20\x20\x20\x20\
\x20\x20\x20\x20\x22\x3e\x20\x3c\x72\x64\x66\x3a\x52\x44\x46\x20\
\x78\x6d\x6c\x6e\x73\x3a\x72\x64\x66\x3d\x22\x68\x74\x74\x70\x3a\
\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\x72\x67\x2f\x31\x39\x39\
\x39\x2f\x30\x32\x2f\x32\x32\x2d\x72\x64\x66\x2d\x73\x79\x6e\x74\
\x61\x78\x2d\x6e\x73\x23\x22\x3e\x20\x3c\x72\x64\x66\x3a\x44\x65\
\x73\x63\x72\x69\x70\x74\x69\x6f\x6e\x20\x72\x64\x66\x3a\x61\x62\
\x6f\x75\x74\x3d\x22\x22\x20\x78\x6d\x6c\x6e\x73\x3a\x78\x6d\x70\
\x3d\x22\x68\x74\x74\x70\x3a\x2f\x2f\x6e\x73\x2e\x61\x64\x6f\x62\
\x65\x2e\x63\x6f\x6d\x2f\x78\x61\x70\x2f\x31\x2e\x30\x2f\x22\x20\
\x78\x6d\x6c\x6e\x73\x3a\x64\x63\x3d\x22\x68\x74\x74\x70\x3a\x2f\
\x2f\x70\x75\x72\x6c\x2e\x6f\x72\x67\x2f\x64\x63\x2f\x65\x6c\x65\
\x6d\x65\x6e\x74\x73\x2f\x31\x2e\x31\x2f\x22\x20\x78\x6d\x6c\x6e\
\x73\x3a\x70\x68\x6f\x74\x6f\x73\x68\x6f\x70\x3d\x22\x68\x74\x74\
\x70\x3a\x2f\x2f\x6e\x73\x2e\x61\x64\x6f\x62\x65\x2e\x63\x6f\x6d\
\x2f\x70\x68\x6f\x74\x6f\x73\x68\x6f\x70\x2f\x31\x2e\x30\x2f\x22\
\x20\x78\x6d\x6c\x6e\x73\x3a\x78\x6d\x70\x4d\x4d\x3d\x22\x68\x74\
\x74\x70\x3a\x2f\x2f\x6e\x73\x2e\x61\x64\x6f\x62\x65\x2e\x63\x6f\
\x6d\x2f\x78\x61\x70\x2f\x31\x2e\x30\x2f\x6d\x6d\x2f\x22\x20\x78\
\x6d\x6c\x6e\x73\x3a\x73\x74\x45\x76\x74\x3d\x22\x68\x74\x74\x70\
\x3a\x2f\x2f\x6e\x73\x2e\x61\x64\x6f\x62\x65\x2e\x63\x6f\x6d\x2f\
\x78\x61\x70\x2f\x31\x2e\x30\x2f\x73\x54\x79\x70\x65\x2f\x52\x65\
\x73\x6f\x75\x72\x63\x65\x45\x76\x65\x6e\x74\x23\x22\x20\x78\x6d\
\x70\x3a\x43\x72\x65\x61\x74\x6f\x72\x54\x6f\x6f\x6c\x3d\x22\x41\
\x64\x6f\x62\x65\x20\x50\x68\x6f\x74\x6f\x73\x68\x6f\x70\x20\x32\
\x31\x2e\x30\x20\x28\x57\x69\x6e\x64\x6f\x77\x73\x29\x22\x20\x78\
\x6d\x70\x3a\x43\x72\x65\x61\x74\x65\x44\x61\x74\x65\x3d\x22\x32\
\x30\x32\x30\x2d\x30\x35\x2d\x30\x32\x54\x31\x37\x3a\x34\x38\x3a\
\x32\x34\x2d\x30\x33\x3a\x30\x30\x22\x20\x78\x6d\x70\x3a\x4d\x6f\
\x64\x69\x66\x79\x44\x61\x74\x65\x3d\x22\x32\x30\x32\x30\x2d\x30\
\x35\x2d\x30\x32\x54\x31\x37\x3a\x35\x32\x3a\x34\x30\x2d\x30\x33\
\x3a\x30\x30\x22\x20\x78\x6d\x70\x3a\x4d\x65\x74\x61\x64\x61\x74\
\x61\x44\x61\x74\x65\x3d\x22\x32\x30\x32\x30\x2d\x30\x35\x2d\x30\
\x32\x54\x31\x37\x3a\x35\x32\x3a\x34\x30\x2d\x30\x33\x3a\x30\x30\
\x22\x20\x64\x63\x3a\x66\x6f\x72\x6d\x61\x74\x3d\x22\x69\x6d\x61\
\x67\x65\x2f\x70\x6e\x67\x22\x20\x70\x68\x6f\x74\x6f\x73\x68\x6f\
\x70\x3a\x43\x6f\x6c\x6f\x72\x4d\x6f\x64\x65\x3d\x22\x33\x22\x20\
\x70\x68\x6f\x74\x6f\x73\x68\x6f\x70\x3a\x49\x43\x43\x50\x72\x6f\
\x66\x69\x6c\x65\x3d\x22\x73\x52\x47\x42\x20\x49\x45\x43\x36\x31\
\x39\x36\x36\x2d\x32\x2e\x31\x22\x20\x78\x6d\x70\x4d\x4d\x3a\x49\
\x6e\x73\x74\x61\x6e\x63\x65\x49\x44\x3d\x22\x78\x6d\x70\x2e\x69\
\x69\x64\x3a\x64\x38\x66\x65\x61\x39\x37\x33\x2d\x30\x36\x38\x34\
\x2d\x34\x64\x34\x64\x2d\x61\x35\x37\x66\x2d\x63\x31\x39\x66\x65\
\x61\x34\x31\x31\x35\x31\x37\x22\x20\x78\x6d\x70\x4d\x4d\x3a\x44\
\x6f\x63\x75\x6d\x65\x6e\x74\x49\x44\x3d\x22\x61\x64\x6f\x62\x65\
\x3a\x64\x6f\x63\x69\x64\x3a\x70\x68\x6f\x74\x6f\x73\x68\x6f\x70\
\x3a\x39\x30\x65\x31\x32\x32\x34\x35\x2d\x63\x66\x65\x61\x2d\x35\
\x37\x34\x33\x2d\x39\x38\x61\x32\x2d\x64\x63\x66\x39\x33\x61\x66\
\x66\x66\x39\x31\x39\x22\x20\x78\x6d\x70\x4d\x4d\x3a\x4f\x72\x69\
\x67\x69\x6e\x61\x6c\x44\x6f\x63\x75\x6d\x65\x6e\x74\x49\x44\x3d\
\x22\x78\x6d\x70\x2e\x64\x69\x64\x3a\x39\x64\x33\x64\x33\x37\x36\
\x33\x2d\x38\x66\x32\x31\x2d\x32\x34\x34\x61\x2d\x61\x66\x38\x64\
\x2d\x34\x36\x61\x34\x33\x62\x65\x39\x63\x37\x31\x31\x22\x3e\x20\
\x3c\x78\x6d\x70\x4d\x4d\x3a\x48\x69\x73\x74\x6f\x72\x79\x3e\x20\
\x3c\x72\x64\x66\x3a\x53\x65\x71\x3e\x20\x3c\x72\x64\x66\x3a\x6c\
\x69\x20\x73\x74\x45\x76\x74\x3a\x61\x63\x74\x69\x6f\x6e\x3d\x22\
\x63\x72\x65\x61\x74\x65\x64\x22\x20\x73\x74\x45\x76\x74\x3a\x69\
\x6e\x73\x74\x61\x6e\x63\x65\x49\x44\x3d\x22\x78\x6d\x70\x2e\x69\
\x69\x64\x3a\x39\x64\x33\x64\x33\x37\x36\x33\x2d\x38\x66\x32\x31\
\x2d\x32\x34\x34\x61\x2d\x61\x66\x38\x64\x2d\x34\x36\x61\x34\x33\
\x62\x65\x39\x63\x37\x31\x31\x22\x20\x73\x74\x45\x76\x74\x3a\x77\
\x68\x65\x6e\x3d\x22\x32\x30\x32\x30\x2d\x30\x35\x2d\x30\x32\x54\
\x31\x37\x3a\x34\x38\x3a\x32\x34\x2d\x30\x33\x3a\x30\x30\x22\x20\
\x73\x74\x45\x76\x74\x3a\x73\x6f\x66\x74\x77\x61\x72\x65\x41\x67\
\x65\x6e\x74\x3d\x22\x41\x64\x6f\x62\x65\x20\x50\x68\x6f\x74\x6f\
\x73\x68\x6f\x70\x20\x32\x31\x2e\x30\x20\x28\x57\x69\x6e\x64\x6f\
\x77\x73\x29\x22\x2f\x3e\x20\x3c\x72\x64\x66\x3a\x6c\x69\x20\x73\
\x74\x45\x76\x74\x3a\x61\x63\x74\x69\x6f\x6e\x3d\x22\x73\x61\x76\
\x65\x64\x22\x20\x73\x74\x45\x76\x74\x3a\x69\x6e\x73\x74\x61\x6e\
\x63\x65\x49\x44\x3d\x22\x78\x6d\x70\x2e\x69\x69\x64\x3a\x64\x38\
\x66\x65\x61\x39\x37\x33\x2d\x30\x36\x38\x34\x2d\x34\x64\x34\x64\
\x2d\x61\x35\x37\x66\x2d\x63\x31\x39\x66\x65\x61\x34\x31\x31\x35\
\x31\x37\x22\x20\x73\x74\x45\x76\x74\x3a\x77\x68\x65\x6e\x3d\x22\
\x32\x30\x32\x30\x2d\x30\x35\x2d\x30\x32\x54\x31\x37\x3a\x35\x32\
\x3a\x34\x30\x2d\x30\x33\x3a\x30\x30\x22\x20\x73\x74\x45\x76\x74\
\x3a\x73\x6f\x66\x74\x77\x61\x72\x65\x41\x67\x65\x6e\x74\x3d\x22\
\x41\x64\x6f\x62\x65\x20\x50\x68\x6f\x74\x6f\x73\x68\x6f\x70\x20\
\x32\x31\x2e\x30\x20\x28\x57\x69\x6e\x64\x6f\x77\x73\x29\x22\x20\
\x73\x74\x45\x76\x74\x3a\x63\x68\x61\x6e\x67\x65\x64\x3d\x22\x2f\
\x22\x2f\x3e\x20\x3c\x2f\x72\x64\x66\x3a\x53\x65\x71\x3e\x20\x3c\
\x2f\x78\x6d\x70\x4d\x4d\x3a\x48\x69\x73\x74\x6f\x72\x79\x3e\x20\
\x3c\x2f\x72\x64\x66\x3a\x44\x65\x73\x63\x72\x69\x70\x74\x69\x6f\
\x6e\x3e\x20\x3c\x2f\x72\x64\x66\x3a\x52\x44\x46\x3e\x20\x3c\x2f\
\x78\x3a\x78\x6d\x70\x6d\x65\x74\x61\x3e\x20\x3c\x3f\x78\x70\x61\
\x63\x6b\x65\x74\x20\x65\x6e\x64\x3d\x22\x72\x22\x3f\x3e\xd7\xf0\
\x47\x8a\x00\x00\x01\x6d\x49\x44\x41\x54\x48\xc7\xed\xd5\x21\x4f\
\xde\x50\x14\xc6\xf1\x5f\x05\x0c\x43\x5e\x12\x54\x3f\xc2\x0c\x10\
\x0c\x58\x3c\x02\xb1\x6c\x66\x09\x09\xc9\xc4\xc4\xc2\xc6\x18\x0a\
\x4b\xc8\x60\x1b\x8c\x4c\x80\x25\x21\x88\x65\x8a\x2c\x01\x04\x66\
\x28\x82\x47\x0d\xfb\x7e\x85\x19\xe8\xcc\xed\xd2\xf4\xed\xbd\xbc\
\x25\xc1\x90\x1d\xd5\xde\x7b\x7b\xfe\x7d\x9e\x73\x4e\x9b\x15\x45\
\xe1\x21\x23\x7b\x3c\x80\x6e\xb7\x5b\xae\x0d\xe1\xcf\x3d\x72\x0d\
\xe0\x06\xb7\x90\xe7\x79\x23\x60\x18\x47\xb8\xc6\x42\xf9\x12\x88\
\xc9\x2c\xf7\x46\xf0\x13\x97\x58\x4c\x01\x86\xb0\x83\x57\xf8\x86\
\x37\x09\x48\xb9\x36\x8c\x73\x8c\xe1\x35\x76\x63\x80\x6a\x92\x2f\
\x78\x87\x2d\x2c\x25\x6c\x19\xc4\x31\x66\x30\x8f\xfd\x12\x1c\x53\
\x50\x85\x6c\xe0\x03\xb6\x03\xac\xdc\x17\xce\x74\x42\xf2\x69\x3c\
\xc7\xf7\x2a\x39\x06\xa8\xc7\x26\x96\x6b\x76\x95\xb5\xfa\x85\x71\
\xbc\xc4\x41\xdd\xc6\xbb\x00\xd5\xc3\x5b\x78\x5b\xb3\xeb\xac\x66\
\x4b\x4f\xf4\xa3\xa0\x0a\xf9\x1c\x92\x6f\xe2\x29\x66\x9b\x6c\xb9\
\x8f\x45\xd5\xf8\x88\x95\x70\xfd\x0c\x3f\x52\x2d\xdc\x16\x90\xe1\
\x10\x2f\xc2\xfd\x2a\xd6\x52\x0f\xb4\xb1\xa8\x83\x13\x4c\x61\x2e\
\x58\xb4\x5e\xab\x49\x8f\x92\x7e\x8b\xdc\xd4\x2d\xb1\xee\x6a\xd5\
\x45\xc9\x21\x4a\x74\xd7\x9d\x0a\xb2\x3e\x86\xa8\x0a\xf9\x84\xf7\
\x0d\xc3\x58\xa4\x14\x8c\xe2\x14\x93\xb1\x21\x8a\x0c\xe3\xd7\xa0\
\xe4\x16\x59\x9e\xe7\x45\x13\x60\x00\x17\x98\x48\x0d\x51\x83\x92\
\xed\xf0\x15\xfd\x57\x93\x98\x82\x27\xa1\xdf\xaf\xb0\xd7\xcf\xff\
\xa4\x02\xd9\xc1\xef\xa0\xa4\xf5\x24\xb7\x8e\x1e\xc0\xff\x9f\x7e\
\x2c\xfe\x02\x87\x80\xd4\xd1\x08\xa9\x5c\xc1\x00\x00\x00\x00\x49\
\x45\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = b"\
\x00\x09\
\x0c\x78\x54\x88\
\x00\x6e\
\x00\x65\x00\x77\x00\x50\x00\x72\x00\x65\x00\x66\x00\x69\x00\x78\
\x00\x05\
\x00\x6f\xa6\x53\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x73\
\x00\x09\
\x0f\x4b\x84\xa7\
\x00\x63\
\x00\x69\x00\x6c\x00\x2d\x00\x78\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x18\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x28\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x18\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x28\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x74\x06\xc0\x29\xb8\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()

counter = 0
jumper = 1
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()


    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value, widget, color):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.progressBarValue(0)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(15)
        self.show()

    def progress (self):
        global counter
        global jumper


        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))
        value = counter
        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 1
            time.sleep(0.05)

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 0.5

    ## DEF PROGRESS BAR VALUE
    ########################################################################'''

    def progressBarValue(self, value):
        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1559, 829)
        Dialog.setStyleSheet("border-radius: 10px;")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 40, 1431, 741))
        self.frame.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, -1, 2, 2))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_right_btns = QtWidgets.QFrame(self.frame)
        self.top_right_btns.setGeometry(QtCore.QRect(1410, 10, 91, 21))
        self.top_right_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.top_right_btns.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.top_right_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_right_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_right_btns.setObjectName("top_right_btns")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(660, 0, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 40, 1411, 691))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(99, 99, 99);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Tabe_Data = QtWidgets.QTableWidget(self.frame_2)
        self.Tabe_Data.setGeometry(QtCore.QRect(20, 20, 1061, 431))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Tabe_Data.setFont(font)
        self.Tabe_Data.setStyleSheet("border:3px solid rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Tabe_Data.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Tabe_Data.setColumnCount(6)
        self.Tabe_Data.setObjectName("Tabe_Data")
        self.Tabe_Data.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Tabe_Data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabe_Data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabe_Data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabe_Data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabe_Data.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabe_Data.setHorizontalHeaderItem(5, item)
        self.Tabe_Data.horizontalHeader().setDefaultSectionSize(175)
        self.AWT = QtWidgets.QFrame(self.frame_2)
        self.AWT.setGeometry(QtCore.QRect(1100, 250, 291, 201))
        self.AWT.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:3px solid rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.AWT.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AWT.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AWT.setObjectName("AWT")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.AWT)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.AWT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border:3px solid rgb(255,255,255);\n"
"border-radius: 20px;")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.Text_AWT = QtWidgets.QTextBrowser(self.AWT)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Text_AWT.setFont(font)
        self.Text_AWT.setStyleSheet("font: 75 40pt \"Times New Roman\";")
        self.Text_AWT.setObjectName("Text_AWT")
        self.verticalLayout_3.addWidget(self.Text_AWT)
        self.Delete_Button = QtWidgets.QPushButton(self.frame_2)
        self.Delete_Button.setGeometry(QtCore.QRect(1220, 560, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Delete_Button.setFont(font)
        self.Delete_Button.setStyleSheet("border:3px solid rgb(0, 0, 0);\n"
"border-radius: 20px;background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Delete_Button.setObjectName("Delete_Button")
        self.Run_Button = QtWidgets.QPushButton(self.frame_2)
        self.Run_Button.setGeometry(QtCore.QRect(1130, 620, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Run_Button.setFont(font)
        self.Run_Button.setStyleSheet("border:3px solid rgb(0, 0, 0);\n"
"border-radius: 20px;background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Run_Button.setObjectName("Run_Button")
        self.Reset_Button = QtWidgets.QPushButton(self.frame_2)
        self.Reset_Button.setGeometry(QtCore.QRect(1060, 560, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Reset_Button.setFont(font)
        self.Reset_Button.setStyleSheet("border:3px solid rgb(0, 0, 0);\n"
"border-radius: 20px;background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Reset_Button.setObjectName("Reset_Button")
        self.Add_Button = QtWidgets.QPushButton(self.frame_2)
        self.Add_Button.setGeometry(QtCore.QRect(1060, 490, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Add_Button.setFont(font)
        self.Add_Button.setStyleSheet("border:3px solid rgb(0, 0, 0);\n"
"border-radius: 20px;background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Add_Button.setObjectName("Add_Button")
        self.SJF_SRTF = QtWidgets.QComboBox(self.frame_2)
        self.SJF_SRTF.setGeometry(QtCore.QRect(1220, 490, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SJF_SRTF.setFont(font)
        self.SJF_SRTF.setStyleSheet("border:3px solid rgb(0, 0, 0);\n"
"border-radius: 20px;background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.SJF_SRTF.setObjectName("SJF_SRTF")
        self.SJF_SRTF.addItem("")
        self.SJF_SRTF.addItem("")
        self.ATT = QtWidgets.QFrame(self.frame_2)
        self.ATT.setGeometry(QtCore.QRect(1100, 20, 291, 211))
        self.ATT.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:3px solid rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.ATT.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ATT.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ATT.setObjectName("ATT")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.ATT)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.ATT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border:3px solid rgb(255,255,255);\n"
"border-radius: 20px;")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_5.addWidget(self.lineEdit_6)
        self.Text_ATT = QtWidgets.QTextBrowser(self.ATT)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Text_ATT.setFont(font)
        self.Text_ATT.setStyleSheet("font: 75 40pt \"Times New Roman\";")
        self.Text_ATT.setObjectName("Text_ATT")
        self.verticalLayout_5.addWidget(self.Text_ATT)
        self.Gantt_Chart_QFrame = QtWidgets.QFrame(self.frame_2)
        self.Gantt_Chart_QFrame.setGeometry(QtCore.QRect(20, 470, 991, 211))
        self.Gantt_Chart_QFrame.setStyleSheet("border: 7px solid rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.Gantt_Chart_QFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Gantt_Chart_QFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Gantt_Chart_QFrame.setObjectName("Gantt_Chart_QFrame")
        self.Gantt_Chart_text = QtWidgets.QTextBrowser(self.Gantt_Chart_QFrame)
        self.Gantt_Chart_text.setGeometry(QtCore.QRect(0, 40, 991, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Gantt_Chart_text.setFont(font)
        self.Gantt_Chart_text.setStyleSheet("font: 75 18pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.Gantt_Chart_text.setObjectName("Gantt_Chart_text")
        self.Label_Gantt_Chart = QtWidgets.QLabel(self.frame_2)
        self.Label_Gantt_Chart.setGeometry(QtCore.QRect(30, 480, 671, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Label_Gantt_Chart.setFont(font)
        self.Label_Gantt_Chart.setStyleSheet("border:3px solid rgb(99,99,99);\n"
"\n"
"border-radius: 20px;\n"
"color: rgb(255, 255, 255);")
        self.Label_Gantt_Chart.setObjectName("Label_Gantt_Chart")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(1380, 10, 31, 21))
        self.pushButton.setStyleSheet("image: url(:/newPrefix/icons/cil-x.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.Add_Button.clicked.connect(lambda: self.add())
        self.Reset_Button.clicked.connect(lambda: self.reset())
        self.Run_Button.clicked.connect(lambda: self.run())
        self.Delete_Button.clicked.connect(lambda: self.det())
        self.pushButton.clicked.connect(lambda: exit())
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def add(self):
        self.Tabe_Data.insertRow(self.Tabe_Data.rowCount())

    def reset(self):
        self.Gantt_Chart_text.setText('')
        self.Text_ATT.setText('')
        self.Text_AWT.setText('')
        for i in range(0, self.Tabe_Data.rowCount()):
            if self.Tabe_Data.rowCount() > 0:
                self.Tabe_Data.removeRow(self.Tabe_Data.rowCount() - 1)

    def det(self):
        if self.Tabe_Data.rowCount() > 0:
            self.Tabe_Data.removeRow(self.Tabe_Data.rowCount() - 1)

    def run(self):
        if self.SJF_SRTF.currentText() == 'SJF':
            return self.SJF()
        else:
            return self.SRTF()

    def SJF(self):
        data = []
        for row in range(self.Tabe_Data.rowCount()):
            data1 = []
            for column in range(0, 3):
                value = self.Tabe_Data.item(row, column)
                value = value.text()
                data1.append(int(value))

            data1 = data1 + [0]
            data.append(data1)
        print(data)
        process_data = data
        start_time = []
        exit_time = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        sequence_of_process = []
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []

            for j in range(len(process_data)):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][3] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    normal_queue.append(temp)
                    temp = []

            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])

                start_time.append(s_time)

                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])

                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)

            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)

                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)

                sequence_of_process.append(normal_queue[0][0])

                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][4] - process_data[i][1]

            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = round(total_turnaround_time / len(process_data), 2)
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][5] - process_data[i][2]

            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = round(total_waiting_time / len(process_data), 2)
        process_data.sort(key=lambda x: x[0])
        s = ''
        for i in range(0, len(sequence_of_process)):
            s += (' |' + str(sequence_of_process[i]) + '| ')
        self.Gantt_Chart_text.setText(s)
        self.Text_ATT.setText(str(average_turnaround_time).center(13))
        self.Text_AWT.setText(str(average_waiting_time).center(13))
        print(process_data)
        for i in range(self.Tabe_Data.rowCount()):
            for j in range(4, len(process_data[i])):
                self.Tabe_Data.setItem(i, j - 1, QtWidgets.QTableWidgetItem(str(process_data[i][j])))
            print()

    def SRTF(self):
        data = []
        for row in range(self.Tabe_Data.rowCount()):
            data1 = []
            for column in range(0, 3):
                value = self.Tabe_Data.item(row, column)
                value = value.text()
                data1.append(int(value))
            data1 = data1 + [0, data1[-1]]
            data.append(data1)
        process_data = data
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key=lambda x: x[1])

        while 1:
            ready_queue = []
            normal_queue = []
            temp = []

            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2],
                                 process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2],
                                 process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][
                    2] == 0:
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
            if len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][
                    2] == 0:
                    process_data[k][3] = 1
                    process_data[k].append(e_time)

        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = round(total_turnaround_time / len(process_data), 2)
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = round(total_waiting_time / len(process_data), 2)
        process_data.sort(key=lambda x: x[0])
        s = ''
        for i in range(0, len(sequence_of_process)):
            s += (' |' + str(sequence_of_process[i]) + '| ')
        self.Gantt_Chart_text.setText(s)
        self.Text_ATT.setText(str(average_turnaround_time).center(13))
        self.Text_AWT.setText(str(average_waiting_time).center(13))
        for i in range(self.Tabe_Data.rowCount()):
            for j in range(5, len(process_data[i])):
                self.Tabe_Data.setItem(i, j - 2, QtWidgets.QTableWidgetItem(str(process_data[i][j])))
            print()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CPU Scheduling"))
        item = self.Tabe_Data.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.Tabe_Data.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Arrival Time"))
        item = self.Tabe_Data.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Burst Time"))
        item = self.Tabe_Data.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Completion Time"))
        item = self.Tabe_Data.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Turnaround Time"))
        item = self.Tabe_Data.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Waiting Time"))
        self.lineEdit_4.setText(_translate("Dialog", "Average Waiting Time"))
        self.Delete_Button.setText(_translate("Dialog", "Delete"))
        self.Run_Button.setText(_translate("Dialog", "Run"))
        self.Reset_Button.setText(_translate("Dialog", "Reset"))
        self.Add_Button.setText(_translate("Dialog", "Add"))
        self.SJF_SRTF.setItemText(0, _translate("Dialog", "SJF"))
        self.SJF_SRTF.setItemText(1, _translate("Dialog", "SRTF"))
        self.lineEdit_6.setText(_translate("Dialog", "Average Turnaround Time"))
        self.Label_Gantt_Chart.setText(_translate("Dialog", "Gantt Chart"))




class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(340, 340)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 135px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.container)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 50, 193, 191))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.widget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)

        self.labelPercentage = QLabel(self.widget)
        self.labelPercentage.setObjectName(u"labelPercentage")
        font1 = QFont()
        font1.setFamily(u"Roboto Thin")
        font1.setPointSize(68)
        self.labelPercentage.setFont(font1)
        self.labelPercentage.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1, 1)

        self.labelLoadingInfo = QLabel(self.widget)
        self.labelLoadingInfo.setObjectName(u"labelLoadingInfo")
        self.labelLoadingInfo.setMinimumSize(QSize(0, 20))
        self.labelLoadingInfo.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        self.labelLoadingInfo.setFont(font2)
        self.labelLoadingInfo.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(93, 93, 154);\n"
"	color: #FFFFFF;\n"
"	margin-left: 40px;\n"
"	margin-right: 40px;\n"
"}")
        self.labelLoadingInfo.setFrameShape(QFrame.NoFrame)
        self.labelLoadingInfo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelLoadingInfo, 2, 0, 1, 1)

        self.labelCredits = QLabel(self.widget)
        self.labelCredits.setObjectName(u"labelCredits")
        self.labelCredits.setFont(font2)
        self.labelCredits.setStyleSheet(u"background-color: none;\n"
"color: rgb(155, 155, 255);")
        self.labelCredits.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelCredits, 3, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.labelTitle.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600; color:#9b9bff;\">CPU</span> Scheduling</p></body></html>", None))
        self.labelPercentage.setText(QCoreApplication.translate("SplashScreen", u"<p><span style=\" font-size:68pt;\">0</span><span style=\" font-size:58pt; vertical-align:super;\">%</span></p>", None))
        self.labelLoadingInfo.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.labelCredits.setText(QCoreApplication.translate("SplashScreen", u"by: Group 4", None))
    # retranslateUi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())