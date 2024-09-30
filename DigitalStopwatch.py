import sys
from PyQt5.QtWidgets import (QApplication ,QWidget 
                             ,QLabel,QPushButton ,QVBoxLayout ,QHBoxLayout)
from PyQt5.QtCore import QTimer ,QTime, Qt 

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00",self)
        self.start_button = QPushButton("Start",self)#buttons 
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset",self)
        self.timer = QTimer(self)#prediocally calls the timer to update the stuffs
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital StopWatch  ")
        self.setGeometry(200,400,300,200)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)#acctually this sets the layout of the stuff here
        hbox =QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)#we are adding this hbox layout to vbox 
        self.setStyleSheet("""
                           QPushButton,QLabel{
                           padding: 20px;
                           font-weight:bold}
            QPushButton{
                   font-size: 50px;
                           color:rgb(0, 51, 153);
                           }
            QLabel{
                   font-size: 120px;
                           color: rgb(0, 26, 77);
                           background: rgb(102, 255, 179);
                           border-radius: 30px;
                           }   """)
    
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)


    def start(self):
        self.timer.start(10)


    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds =time.msec()//10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time =self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())