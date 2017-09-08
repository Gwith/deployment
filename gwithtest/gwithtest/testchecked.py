from testcheckedf.ui_testchecked import Ui_TestChecked

class TestChecked(Ui_TestChecked):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.iterbutton.clicked.connect(self.test_iter)

        self.show()

    def test_iter(self):
        for i in range(self.itertable.rowCount()):
            for d in range(self.itertable.columnCount()):
                if self.itertable.item(i, d).checkState():
                    print('checked')
                else:
                    print('not checked')