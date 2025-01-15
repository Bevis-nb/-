# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledKlLkPV.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QSizePolicy,
    QVBoxLayout, QWidget)

from rrd_widgets import SimpleButton_4

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(915, 598)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.top = QFrame(self.centralwidget)
        self.top.setObjectName(u"top")
        self.top.setFrameShape(QFrame.Shape.StyledPanel)
        self.top.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.top)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame = QFrame(self.top)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(631, 511))
        self.frame.setStyleSheet(u"#frame{\n"
"border:2px solid blue;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout_12.addWidget(self.frame)

        self.frame_2 = QFrame(self.top)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.name = QLineEdit(self.frame_2)
        self.name.setObjectName(u"name")

        self.horizontalLayout_2.addWidget(self.name)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(220, 141))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.PA = QLineEdit(self.groupBox)
        self.PA.setObjectName(u"PA")
        self.PA.setMinimumSize(QSize(157, 0))
        self.PA.setSizeIncrement(QSize(133, 0))

        self.horizontalLayout_6.addWidget(self.PA)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.PB = QLineEdit(self.groupBox)
        self.PB.setObjectName(u"PB")
        self.PB.setMinimumSize(QSize(157, 0))

        self.horizontalLayout_7.addWidget(self.PB)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.PH = QLineEdit(self.groupBox)
        self.PH.setObjectName(u"PH")
        self.PH.setMinimumSize(QSize(157, 0))
        self.PH.setSizeIncrement(QSize(133, 0))

        self.horizontalLayout_8.addWidget(self.PH)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(220, 144))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_11.addWidget(self.label_7)

        self.PA2 = QLineEdit(self.groupBox_2)
        self.PA2.setObjectName(u"PA2")
        self.PA2.setMinimumSize(QSize(157, 0))

        self.horizontalLayout_11.addWidget(self.PA2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.PB2 = QLineEdit(self.groupBox_2)
        self.PB2.setObjectName(u"PB2")
        self.PB2.setMinimumSize(QSize(157, 0))

        self.horizontalLayout_10.addWidget(self.PB2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.PH2 = QLineEdit(self.groupBox_2)
        self.PH2.setObjectName(u"PH2")
        self.PH2.setMinimumSize(QSize(157, 0))

        self.horizontalLayout_9.addWidget(self.PH2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.color = QLineEdit(self.frame_2)
        self.color.setObjectName(u"color")

        self.horizontalLayout_3.addWidget(self.color)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.weight = QLineEdit(self.frame_2)
        self.weight.setObjectName(u"weight")

        self.horizontalLayout_4.addWidget(self.weight)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.inpix = SimpleButton_4(self.frame_2)
        self.inpix.setObjectName(u"inpix")

        self.horizontalLayout_5.addWidget(self.inpix)

        self.mix = SimpleButton_4(self.frame_2)
        self.mix.setObjectName(u"mix")

        self.horizontalLayout_5.addWidget(self.mix)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.out = SimpleButton_4(self.frame_2)
        self.out.setObjectName(u"out")

        self.horizontalLayout_13.addWidget(self.out)

        self.print = SimpleButton_4(self.frame_2)
        self.print.setObjectName(u"print")

        self.horizontalLayout_13.addWidget(self.print)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_12.addWidget(self.frame_2)


        self.verticalLayout_5.addWidget(self.top)

        self.bottom = QFrame(self.centralwidget)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottom.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.bottom)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_11 = QLabel(self.bottom)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.name_find = QLineEdit(self.bottom)
        self.name_find.setObjectName(u"name_find")

        self.horizontalLayout.addWidget(self.name_find)

        self.finder = SimpleButton_4(self.bottom)
        self.finder.setObjectName(u"finder")

        self.horizontalLayout.addWidget(self.finder)


        self.verticalLayout_5.addWidget(self.bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MARKINGER", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8\u533a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u578b\u53f7\uff1a", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u5c3a\u5bf8", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u957f\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5bbd\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\uff1a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5305\u88c5\u5c3a\u5bf8", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u957f\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5bbd\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u989c\u8272\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u91cf\uff1a", None))
        self.inpix.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u56fe\u7247", None))
        self.mix.setText(QCoreApplication.translate("MainWindow", u"\u5408\u6210", None))
        self.out.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.print.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u5df2\u6709\u578b\u53f7\uff1a", None))
        self.finder.setText(QCoreApplication.translate("MainWindow", u"\u5bfb\u627e", None))
    # retranslateUi

