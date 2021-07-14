import sys
import os
from PySide6.QtGui import *
from PySide6.QtQml import *
from PySide6.QtCore import *

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    app.setWindowIcon(QIcon("icon.png"))
    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))
    if not engine.rootObjects():sys.exit(-1)
    try:sys.exit(app.exec_())
    except:pass