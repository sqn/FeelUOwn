# -*- coding:utf8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DesktopScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)


class DesktopView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._scene = DesktopScene(self)
        self.setScene(self._scene)
        self.resize(600, 400)

        self._scene.setSceneRect(QRectF(QPointF(0, 0), QSizeF(self.size())))
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setStyleSheet("background: rgba(20, 20, 20, 0.3);")


class DesktopContainer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._view = DesktopView(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self._exit_shortcut = QShortcut(QKeySequence(Qt.Key_Escape), self)
        self._init_signal_binding()

    def _init_signal_binding(self):
        self._exit_shortcut.activated.connect(self.close)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = DesktopContainer()
    w.show()
    app.exec_()
