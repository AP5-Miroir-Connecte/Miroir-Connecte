from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import requests, json
from Clock import *
from Weather import *
from Color import *
from News import *
class MainWindow(QMainWindow):
    def __init__(self,*args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Mira d'or")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.screen = [
                    "","","","","",
                    "","","","","",
                    "","","","","",
                    "","","","","",
                    "","","","","",
                 ]
        self.setClock(0,0)
        self.setWeather(0,4)
        positions = [(i, j) for i in range(5) for j in range(5)]

        for position, element in zip(positions,self.screen):

            if element == "":
                element = Color("white")
            layout.addWidget(element, *position)
        

        self.timerClock = QTimer(self)
        self.timerClock.setInterval(1000)
        self.timerClock.timeout.connect(self.displayTime)
        self.timerClock.start()

        self.timerWeather = QTimer(self)
        self.timerWeather.setInterval(1800000)
        self.timerWeather.timeout.connect(self.displayWeather)
        self.timerWeather.start()
        
    def displayTime(self):
        self.clock.updateTime()
    
    def displayWeather(self):
        self.weather.updateWeather()

    def getIndex(self,x,y):
        if x == 0:
            return y
        elif x > 0 and x < 2:
            if y == 0 :
                return 5+y+1
            else:
                return 5+y
        elif x > 1 and x < 3:
            if y == 0 :
                return 10+y+1
            else:
                return 10+y
        elif x > 2 and x < 4:
            if y == 0 :
                return 15+y+1
            else:
                return 15+y
        else:
            return -1

    def setClock(self,x,y):
        self.clock = Clock()
        self.screen[self.getIndex(x,y)] = self.clock

    def setWeather(self,x,y):
        self.weather = Weather()
        self.screen[self.getIndex(x,y)] = self.weather