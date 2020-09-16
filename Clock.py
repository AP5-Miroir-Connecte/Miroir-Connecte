from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
class Clock(QWidget):
    
    def __init__(self, *args, **kwargs):
        super(Clock, self).__init__(*args, **kwargs)
        self.clock = QLabel("", self)
        self.clock.setStyleSheet('color: white')
        self.clock.setFont(QFont('caviar dreams', 24))
        self.clock.setAlignment(Qt.AlignCenter)
        self.updateTime()
    
    def updateTime(self):
        dayName = QDateTime.currentDateTime().toString("dddd").capitalize()
        dayInMonth = QDateTime.currentDateTime().toString("dd")
        monthName = QDateTime.currentDateTime().toString("MMMM").capitalize()
        monthInYear = QDateTime.currentDateTime().toString("MM")
        year = QDateTime.currentDateTime().toString("yyyy")
        hoursMinutesSeconds = QDateTime.currentDateTime().toString("HH:mm:ss")
        time = dayName + " " + dayInMonth + " " + monthName + " " + year + "\n" + hoursMinutesSeconds
        self.clock.setText(time)