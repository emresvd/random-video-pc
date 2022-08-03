from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
import random_video


class Window(QMainWindow):
    def __init__(self, url):
        super(Window, self).__init__()
        self.web = QWebEngineView()
        self.web.load(QUrl(url))
        self.setWindowTitle("Random Video")
        self.setWindowIcon(QIcon("icon.png"))
        self.setCentralWidget(self.web)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.web.load(
                QUrl("https://www.youtube.com/embed/" + random_video.get_random_video_id()))


if __name__ == '__main__':
    url = "https://www.youtube.com/embed/" + random_video.get_random_video_id()
    app = QApplication(sys.argv)
    window = Window(url)
    window.show()
    sys.exit(app.exec())
