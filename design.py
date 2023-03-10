# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Python_projects/Passworder/designs/main_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 640)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 640))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMaximumSize(QtCore.QSize(16777215, 60))
        self.header.setStyleSheet("background-color: rgb(239, 165, 35);")
        self.header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setLineWidth(0)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wrapper_toggle_btn = QtWidgets.QFrame(self.header)
        self.wrapper_toggle_btn.setMaximumSize(QtCore.QSize(80, 60))
        self.wrapper_toggle_btn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wrapper_toggle_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wrapper_toggle_btn.setObjectName("wrapper_toggle_btn")
        self.horizontalLayout_2.addWidget(self.wrapper_toggle_btn)
        self.top_bar = QtWidgets.QFrame(self.header)
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.caption = QtWidgets.QLabel(self.top_bar)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.caption.setFont(font)
        self.caption.setObjectName("caption")
        self.horizontalLayout_3.addWidget(self.caption)
        self.horizontalLayout_2.addWidget(self.top_bar)
        self.verticalLayout.addWidget(self.header)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_menu = QtWidgets.QFrame(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy)
        self.left_menu.setMinimumSize(QtCore.QSize(80, 0))
        self.left_menu.setMaximumSize(QtCore.QSize(80, 16777215))
        self.left_menu.setStyleSheet("background-color: rgb(239, 165, 35);")
        self.left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu.setLineWidth(0)
        self.left_menu.setObjectName("left_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 25)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.left_menu)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_home = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_home.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"}")
        self.btn_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Python_projects/Passworder/designs\\icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QtCore.QSize(32, 32))
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_3.addWidget(self.btn_home)
        self.btn_add = QtWidgets.QPushButton(self.frame)
        self.btn_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"}")
        self.btn_add.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/Python_projects/Passworder/designs\\icons/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon1)
        self.btn_add.setIconSize(QtCore.QSize(45, 45))
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout_3.addWidget(self.btn_add)
        self.btn_generator = QtWidgets.QPushButton(self.frame)
        self.btn_generator.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_generator.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"}")
        self.btn_generator.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:/Python_projects/Passworder/designs\\icons/generator_1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_generator.setIcon(icon2)
        self.btn_generator.setIconSize(QtCore.QSize(36, 36))
        self.btn_generator.setObjectName("btn_generator")
        self.verticalLayout_3.addWidget(self.btn_generator)
        self.btn_info = QtWidgets.QPushButton(self.frame)
        self.btn_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_info.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"}")
        self.btn_info.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:/Python_projects/Passworder/designs\\icons/info_1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_info.setIcon(icon3)
        self.btn_info.setIconSize(QtCore.QSize(34, 34))
        self.btn_info.setObjectName("btn_info")
        self.verticalLayout_3.addWidget(self.btn_info)
        self.btn_github = QtWidgets.QPushButton(self.frame)
        self.btn_github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_github.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"}")
        self.btn_github.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("D:/Python_projects/Passworder/designs\\icons/github.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_github.setIcon(icon4)
        self.btn_github.setIconSize(QtCore.QSize(36, 36))
        self.btn_github.setObjectName("btn_github")
        self.verticalLayout_3.addWidget(self.btn_github)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"}")
        self.pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("D:/Python_projects/Passworder/designs\\icons/settings_1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QtCore.QSize(46, 46))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame)
        self.label = QtWidgets.QLabel(self.left_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.left_menu)
        self.wrapper_pages = QtWidgets.QFrame(self.content)
        self.wrapper_pages.setStyleSheet("background-color: rgb(252, 252, 252);")
        self.wrapper_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wrapper_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wrapper_pages.setObjectName("wrapper_pages")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.wrapper_pages)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pages_widget = QtWidgets.QStackedWidget(self.wrapper_pages)
        self.pages_widget.setObjectName("pages_widget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.main_page)
        self.horizontalLayout_4.setContentsMargins(80, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.main_page)
        self.tableWidget.setMinimumSize(QtCore.QSize(755, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("background-color: rgba(239, 165, 35, 153);\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        item.setBackground(QtGui.QColor(239, 165, 35, 153))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(14)
        item.setFont(font)
        item.setBackground(QtGui.QColor(239, 165, 35, 153))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(14)
        item.setFont(font)
        item.setBackground(QtGui.QColor(239, 165, 35, 153))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(239, 165, 35, 153))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("D:/Python_projects/Passworder/designs\\icons/hidden.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(240)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pages_widget.addWidget(self.main_page)
        self.add_page = QtWidgets.QWidget()
        self.add_page.setObjectName("add_page")
        self.pages_widget.addWidget(self.add_page)
        self.verticalLayout_4.addWidget(self.pages_widget)
        self.horizontalLayout.addWidget(self.wrapper_pages)
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pages_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Passworder"))
        self.caption.setText(_translate("MainWindow", "Passworder"))
        self.btn_home.setToolTip(_translate("MainWindow", "Home"))
        self.btn_add.setToolTip(_translate("MainWindow", "Add new"))
        self.btn_generator.setToolTip(_translate("MainWindow", "Generator"))
        self.btn_info.setToolTip(_translate("MainWindow", "Info"))
        self.btn_github.setToolTip(_translate("MainWindow", "GitHub"))
        self.pushButton.setToolTip(_translate("MainWindow", "Settings"))
        self.label.setText(_translate("MainWindow", "v1.0"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Platform"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Login"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Facebook"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
