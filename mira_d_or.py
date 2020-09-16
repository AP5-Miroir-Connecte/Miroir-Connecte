import sys
from MainWindow import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()
    #widget.resize(800, 600)
    widget.showFullScreen()
    #widget.show()

    sys.exit(app.exec_())