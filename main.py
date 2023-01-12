import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QTableWidgetItem, QFileDialog
import pandas as pd

from pgs import Ui_MainWindow

global g_num_employees
global g_num_shifts
global g_num_days
global g_employees_per_shift
global g_names_employees
global g_priorities
global g_shift_requests
global g_max_num_of_shifts

global g_col_names
global res


def adjust_table_1(table):
    """sets table 1 parameters"""
    table.setRowCount(g_num_shifts)
    table.setColumnCount(1)
    table.horizontalHeader().setVisible(False)
    table.setColumnWidth(0, 210)

    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(13)
    font.setWeight(50)
    table.setFont(font)
    table.setStyleSheet("color: rgb(255, 255, 255)")
    table.verticalHeader().setStyleSheet("color: rgb(0, 0, 0)")


def adjust_table_2(table):
    """sets table 2 parameters"""
    table.setRowCount(g_num_employees)
    col = g_num_shifts * g_num_days + 2
    table.setColumnCount(col)
    for i in range(col):
        table.setColumnWidth(i, 5)

    global g_col_names
    g_col_names = ['ФИО', 'Рейтинг', ]
    for d in range(g_num_days):
        for s in range(g_num_shifts):
            g_col_names.append(f'd{d + 1}s{s + 1}')

    table.setHorizontalHeaderLabels(g_col_names)

    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    font.setWeight(50)
    table.setFont(font)
    table.setStyleSheet("color: rgb(255, 255, 255)")
    table.verticalHeader().setStyleSheet("color: rgb(0, 0, 0)")
    table.horizontalHeader().setStyleSheet("color: rgb(0, 0, 0)")

    table.horizontalHeaderItem(1).setToolTip("Чем больше число, тем больше приоритет.\n Если это не требуется, можно поставить всем 1 ")


def adjust_table_3(table):
    """sets table 3 parameters"""
    table.setRowCount(g_num_employees)
    table.setColumnCount(g_num_shifts * g_num_days)

    for i in range(g_num_shifts * g_num_days):
        table.setColumnWidth(i, 5)

    table.setHorizontalHeaderLabels(g_col_names[2::])
    table.setVerticalHeaderLabels(g_names_employees)

    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    font.setWeight(50)
    table.setFont(font)
    table.setStyleSheet("color: rgb(255, 255, 255)")
    table.verticalHeader().setStyleSheet("color: rgb(0, 0, 0)")
    table.horizontalHeader().setStyleSheet("color: rgb(0, 0, 0)")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # PAGES
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # BUTTONS
        self.ui.btn_save_1.clicked.connect(self.click_save_1)
        self.ui.btn_save_2.clicked.connect(self.click_save_2)
        self.ui.btn_save_3.clicked.connect(self.click_save_3)
        self.ui.btn_save_4.clicked.connect(self.click_save_4)
        self.ui.btn_save_5.clicked.connect(self.click_save_5)

    def click_save_1(self):
        """get the entered data"""
        global g_num_employees
        global g_num_shifts
        global g_num_days
        global g_max_num_of_shifts
        g_num_employees = int(self.ui.spinBox_1.text())
        g_num_shifts = int(self.ui.spinBox_2.text())
        g_num_days = int(self.ui.spinBox_3.text())
        g_max_num_of_shifts = int(self.ui.spinBox_4.text())
        adjust_table_1(self.ui.tableWidget)
        print(g_num_employees)
        print(g_num_shifts)
        print(g_num_days)

    def click_save_2(self):
        """get the entered data"""
        # g_employees_per_shift[i] indicates number of employees required for shift i
        global g_employees_per_shift
        g_employees_per_shift = []
        for i in range(self.ui.tableWidget.rowCount()):
            g_employees_per_shift.append(int(self.ui.tableWidget.item(i, 0).text()))
        print(g_employees_per_shift)

        adjust_table_2(self.ui.tableWidget_2)
        self.ui.tableWidget_2.resizeColumnsToContents()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def click_save_3(self):
        """get the entered data from table 2"""
        self.ui.tableWidget_2.resizeColumnsToContents()
        # get g_names_employees from table_2
        global g_names_employees
        g_names_employees = []
        for em in range(g_num_employees):
            g_names_employees.append(self.ui.tableWidget_2.item(em, 0).text())
        print(g_names_employees)

        # get priorities from table_2
        # g_priorities[i] indicates rank of employee i
        global g_priorities
        g_priorities = []
        for em in range(g_num_employees):
            g_priorities.append(int(self.ui.tableWidget_2.item(em, 1).text()))
        print(g_priorities)

        # get requests from table_2
        # g_shift_requests[i][j][k] indicates whether employee i wants to work shift k on day j
        global g_shift_requests
        g_shift_requests = []
        col = g_num_shifts * g_num_days + 2
        for em in range(g_num_employees):
            for s in range(2, col):
                g_shift_requests.append(self.ui.tableWidget_2.item(em, s).text())

        def chunks(lst, n):
            """Yield successive n-sized chunks from lst."""
            for i in range(0, len(lst), n):
                yield lst[i:i + n]

        g_shift_requests = [s.replace('+', '1') for s in g_shift_requests]
        g_shift_requests = [s.replace('-', '0') for s in g_shift_requests]
        g_shift_requests = [int(s) for s in g_shift_requests]

        g_shift_requests = list(chunks(g_shift_requests, g_num_shifts))
        g_shift_requests = list(chunks(g_shift_requests, g_num_days))
        print(g_shift_requests)

    def click_save_4(self):
        """pass data to the main function and convert the result"""
        from main_function import func

        global g_num_employees
        global g_num_shifts
        global g_num_days
        global g_employees_per_shift
        global g_priorities
        global g_shift_requests
        global g_names_employees

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        global res
        res = func(g_num_employees, g_num_shifts, g_num_days, g_employees_per_shift, g_priorities, g_shift_requests, g_max_num_of_shifts)
        print(res)
        print(type(res))

        adjust_table_3(self.ui.tableWidget_3)
        #for i, row in res.iterrows():
        #    for j in range(g_num_days*g_num_shifts):
        #        self.ui.tableWidget_3.setItem(i-1, j, QTableWidgetItem(str(row[j])))
        for i, row in res.iterrows():
            for j in range(g_num_days*g_num_shifts):
                if str(row[j])[0] == "+":
                    self.ui.tableWidget_3.setItem(i-1, j, QTableWidgetItem(str(row[j])))
                    self.ui.tableWidget_3.item(i-1, j).setBackground(QColor(180, 142, 205))
                else:
                    self.ui.tableWidget_3.setItem(i-1, j, QTableWidgetItem(str(row[j])))

        from main_function import percentage
        self.ui.label.setText(QtCore.QCoreApplication.translate("MainWindow", "Удовлетворено " + str(percentage) + "% просьб"))
        print(percentage)

    def click_save_5(self):
        """save the result to exel"""
        res.to_excel(r'C:\Users\Regina\Downloads\table.xlsx')
        print("SAVED!!!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
