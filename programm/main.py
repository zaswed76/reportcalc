import sys
from PyQt5 import QtWidgets
import pandas

from programm.gui import mainwidget

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = mainwidget.Widget()
    main.show()
    sys.exit(app.exec_())