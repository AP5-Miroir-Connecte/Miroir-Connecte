from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
class Color(QWidget):
    
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)