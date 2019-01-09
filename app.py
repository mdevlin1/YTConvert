import sys
import qdarkstyle
import re
import pafy
import time
import os
import logging
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from YT_Convert import YT_Convert as ytc
import QWDialog

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    resx = app.desktop().screenGeometry().width()
    resy = app.desktop().screenGeometry().height()

    yt = ytc.YTConvert(resx, resy)
    sys.exit(app.exec_())

main()
