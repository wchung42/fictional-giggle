from PyQt6.QtWidgets import QApplication
from ui import App
import sys

def run():
    app = QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec())

if __name__=='__main__':
    run()
