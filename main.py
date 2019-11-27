import sys
from PySide2.QtWidgets import QApplication, QLabel
from windows import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
