# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_landit.ui'
#
# Created: Wed Mar 20 16:50:52 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LandIt(object):
    def setupUi(self, LandIt):
        LandIt.setObjectName(_fromUtf8("LandIt"))
        LandIt.resize(384, 259)
        self.gridLayout = QtGui.QGridLayout(LandIt)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget_2 = QtGui.QWidget(LandIt)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_4 = QtGui.QLabel(self.widget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        self.dtmLayer = QtGui.QComboBox(self.widget_2)
        self.dtmLayer.setObjectName(_fromUtf8("dtmLayer"))
        self.gridLayout_3.addWidget(self.dtmLayer, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 3)
        self.widget_3 = QtGui.QWidget(LandIt)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.widget_3)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label = QtGui.QLabel(self.widget_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.sourceLayer = QtGui.QComboBox(self.widget_3)
        self.sourceLayer.setObjectName(_fromUtf8("sourceLayer"))
        self.gridLayout_4.addWidget(self.sourceLayer, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 3)
        self.checkBox = QtGui.QCheckBox(LandIt)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 7, 0, 1, 3)
        self.pushButton = QtGui.QPushButton(LandIt)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 8, 2, 1, 1)
        self.progressBar = QtGui.QProgressBar(LandIt)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 8, 0, 1, 2)
        self.widget_4 = QtGui.QWidget(LandIt)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.widget_4)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.interpolationMethod = QtGui.QComboBox(self.widget_4)
        self.interpolationMethod.setObjectName(_fromUtf8("interpolationMethod"))
        self.interpolationMethod.addItem(_fromUtf8(""))
        self.interpolationMethod.addItem(_fromUtf8(""))
        self.interpolationMethod.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.interpolationMethod, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.widget_4, 5, 0, 1, 3)
        self.widget = QtGui.QWidget(LandIt)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.destinationField = QtGui.QComboBox(self.widget)
        self.destinationField.setObjectName(_fromUtf8("destinationField"))
        self.gridLayout_2.addWidget(self.destinationField, 1, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 4, 1, 1)
        self.gridLayout.addWidget(self.widget, 4, 0, 1, 3)
        self.widget_5 = QtGui.QWidget(LandIt)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.gridLayout_6 = QtGui.QGridLayout(self.widget_5)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_5 = QtGui.QLabel(self.widget_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.widget_5)
        self.doubleSpinBox.setMinimum(-999.99)
        self.doubleSpinBox.setMaximum(999.99)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout_6.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.widget_5, 6, 0, 1, 3)

        self.retranslateUi(LandIt)
        self.interpolationMethod.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(LandIt)

    def retranslateUi(self, LandIt):
        LandIt.setWindowTitle(QtGui.QApplication.translate("LandIt", "LandIt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("LandIt", "DTM", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LandIt", "Points from layer", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("LandIt", "Only process point where destination field is NULL", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("LandIt", "GO", None, QtGui.QApplication.UnicodeUTF8))
        self.interpolationMethod.setItemText(0, QtGui.QApplication.translate("LandIt", "nearest neighbor", None, QtGui.QApplication.UnicodeUTF8))
        self.interpolationMethod.setItemText(1, QtGui.QApplication.translate("LandIt", "linear interpolation", None, QtGui.QApplication.UnicodeUTF8))
        self.interpolationMethod.setItemText(2, QtGui.QApplication.translate("LandIt", "cubic interpolation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("LandIt", "Interpolation method", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("LandIt", "Destination field", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("LandIt", "Add", None, QtGui.QApplication.UnicodeUTF8))

