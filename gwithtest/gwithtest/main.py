import sys
from PyQt5.QtWidgets import QApplication
from testcheckedf.testchecked import TestChecked

app = QApplication(sys.argv)
window = TestChecked()
sys.exit(app.exec_())