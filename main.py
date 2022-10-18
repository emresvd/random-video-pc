from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

import sys
import random_video

YOUTUBE_EMBED_URL = "https://www.youtube.com/embed/{}?autoplay=1&mute=1"


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.web = QWebEngineView()
        self.setWindowTitle("Random YouTube Video")
        self.setWindowIcon(QIcon("icon.png"))
        self.setCentralWidget(self.web)
        self.web.load(QUrl(self.getUrl()))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.web.load(QUrl(self.getUrl()))

    def getUrl(self):
        return YOUTUBE_EMBED_URL.format(random_video.get_random_video_id())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
