import pafy
import time
import os
import logging
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class OWDialog(QMainWindow):
    def __init__(self):
        super(OWDialog, self).__init__()
        self.initUI()

    def initUI(self, fileName):
        owLabel = QLabel("%s.mp3 already exists. Overwrite?"%name);
        owLayoutV = QVBoxLayout()
        owLayoutH = QHBoxLayout()
        owYButton = QPushButton("Yes")
        owNButton = QPushButton("No")
        owLayoutV.addWidget(owLabel)
        owLayoutH.addWidget(owYButton)
        owLayoutH.addWidget(owNButton)
        owLayoutV.addLayout(owLayoutH)
        self.owDialog.setLayout(owLayoutV)
        self.owDialog.show()