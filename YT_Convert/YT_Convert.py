import pafy
import time
import os
import logging
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import QWDialog

class YTConvert(QMainWindow):
    def __init__(self, w, h):
        super(YTConvert, self).__init__()
        self.resx = w
        self.resy = h
        self.initUI()

    def initUI(self):
        mainWidg = QWidget()
        logging.getLogger().setLevel(logging.ERROR)

        mMenu = self.menuBar()
        fileMenu = mMenu.addMenu("File")
        editMenu = mMenu.addMenu("Edit")
        viewMenu = mMenu.addMenu("View")
        toolsMenu = mMenu.addMenu("Tools")
        helpMenu = mMenu.addMenu("Help")

        hbox = QHBoxLayout()

        self.font = QFont("default", 9)
        v1Widg = QWidget()
        vbox1 = QVBoxLayout()
        v1Widg.setMinimumSize(int(self.resx * (1/5)),0)
        descLabel = QLabel(text="Enter YouTube links seperated by commas: ")
        descLabel.setFont(self.font)
        t = QPlainTextEdit()

        sLayout = QHBoxLayout()
        cButton = QPushButton("Convert")
        self.comboBox = QComboBox()
        self.comboBox.addItem("Video")
        self.comboBox.addItem("Audio")
        sLayout.addWidget(self.comboBox)
        sLayout.addWidget(cButton)
        #comboBox.setFixedSize(50,35)
        vbox1.addWidget(descLabel)
        vbox1.addWidget(t)
        vbox1.addLayout(sLayout)
        v1Widg.setLayout(vbox1)

        cButton.clicked.connect(lambda: self.convert(t.toPlainText()))

        self.owDialog = QDialog()
        self.owDialog.setWindowTitle("Overwrite File")

        v2Widg = QWidget()

        self.recentDown = []
        self.vbox2 = QVBoxLayout()
        v2Widg.setMinimumSize(int(self.resx * (1/5)),0)
        q = QLabel()
        file = QPlainTextEdit()
        dLabel = QLabel()
        self.progress = QProgressBar()
        q.setText("Recent Downloads")
        q.setFont(self.font)
        file.setMinimumSize(int(self.resx * (1/40)),0)
        #dLabel.setText("No Downloads in Progress")
        self.vbox2.addWidget(q)
        #self.vbox2.addWidget(file)
        self.vbox2.setAlignment(Qt.AlignTop)
        v2Widg.setLayout(self.vbox2)
        
        hbox.addWidget(v1Widg)
        hbox.addWidget(v2Widg)
        mainWidg.setFixedSize(int(self.resx * (1/2.5)), int(self.resy * (1/4)))
        mainWidg.setLayout(hbox)    

        self.setCentralWidget(mainWidg)
        self.setFixedSize(int(self.resx * (1/2.5)), int(self.resy * (1/2)))
        self.setWindowTitle("Convert YouTube videos to mp3s")
        self.show()

    def convert(self, text):
        linkList = re.split(",| |, |\n", text)
        self.links = []
        while "" in linkList:
            linkList.remove("")
        for i in linkList:
            pLay = QVBoxLayout()
            url = i
            vid = pafy.new(url)
            pLabel = QLabel(vid.title)
            progress = QProgressBar()
            pLay.addWidget(pLabel)
            pLay.addWidget(progress)
            self.vbox2.addLayout(pLay)
            self.links.append([i, progress])
        
        print(self.links)
        if (self.comboBox.currentText() == "Video"):
            self.urlType = "Video"
            QTimer.singleShot(50, self.updateProgress)
        elif (self.comboBox.currentText() == "Audio"):
            self.urlType = "Audio"
            QTimer.singleShot(50, self.updateProgress)
        
    def updateProgress(self):
        url = self.links[0][0]
        vid = pafy.new(url)
        if self.urlType == "Video":
            stream = vid.getbestvideo()
        elif self.urlType == "Audio":
            stream = vid.getbestaudio()
        name = vid.title
        restrict = ["<", ">", ":", "/", "\\", "|", "?", "*", " "]
        for i in restrict:
            name = name.replace(i, "")
        if self.urlType == "Video":
            if os.path.isfile("%s.mp4"%name):
                return 
            filename = stream.download(quiet=True, callback=self.progressB, 
                filepath="%s.mp4" % name)

        elif self.urlType == "Audio":
            if os.path.isfile("%s.mp3"%name):
                return
            filename = stream.download(quiet=True, callback=self.progressB, 
                filepath="%s.mp3" % name)

        self.links.pop(0)
        if self.links != []:
            if (self.comboBox.currentText() == "Video"):
                self.urlType = "Video"
                QTimer.singleShot(50, self.updateProgress)
            elif (self.comboBox.currentText() == "Audio"):
                self.urlType = "Audio"
                QTimer.singleShot(50, self.updateProgress)
   
    def progressB(self, total, recvd, ratio, rate, eta):
        time.sleep(.005)
        self.links[0][1].setValue(int(ratio*100))
