# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\cooki\OneDrive\Desktop\fever_monitor\qtgui\ui\SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(388, 383)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.comboBox_temp_unit = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_temp_unit.sizePolicy().hasHeightForWidth())
        self.comboBox_temp_unit.setSizePolicy(sizePolicy)
        self.comboBox_temp_unit.setMinimumSize(QtCore.QSize(110, 0))
        self.comboBox_temp_unit.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_temp_unit.setFont(font)
        self.comboBox_temp_unit.setObjectName("comboBox_temp_unit")
        self.gridLayout.addWidget(self.comboBox_temp_unit, 0, 2, 1, 1)
        self.comboBox_colormap = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_colormap.sizePolicy().hasHeightForWidth())
        self.comboBox_colormap.setSizePolicy(sizePolicy)
        self.comboBox_colormap.setMinimumSize(QtCore.QSize(110, 0))
        self.comboBox_colormap.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_colormap.setFont(font)
        self.comboBox_colormap.setObjectName("comboBox_colormap")
        self.gridLayout.addWidget(self.comboBox_colormap, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.checkBox_sound = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_sound.setFont(font)
        self.checkBox_sound.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_sound.setObjectName("checkBox_sound")
        self.horizontalLayout_7.addWidget(self.checkBox_sound)
        spacerItem3 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem4 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.checkBox_fps = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_fps.setFont(font)
        self.checkBox_fps.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_fps.setObjectName("checkBox_fps")
        self.horizontalLayout_9.addWidget(self.checkBox_fps)
        spacerItem5 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem6)
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.doubleSpinBox_temp_thresh = QtWidgets.QDoubleSpinBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_temp_thresh.setFont(font)
        self.doubleSpinBox_temp_thresh.setMaximum(1000.0)
        self.doubleSpinBox_temp_thresh.setObjectName("doubleSpinBox_temp_thresh")
        self.gridLayout_2.addWidget(self.doubleSpinBox_temp_thresh, 2, 1, 1, 1)
        self.comboBox_model = QtWidgets.QComboBox(Dialog)
        self.comboBox_model.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_model.setFont(font)
        self.comboBox_model.setObjectName("comboBox_model")
        self.gridLayout_2.addWidget(self.comboBox_model, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.doubleSpinBox_confidence_thresh = QtWidgets.QDoubleSpinBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_confidence_thresh.setFont(font)
        self.doubleSpinBox_confidence_thresh.setMaximum(1.0)
        self.doubleSpinBox_confidence_thresh.setSingleStep(0.01)
        self.doubleSpinBox_confidence_thresh.setProperty("value", 0.5)
        self.doubleSpinBox_confidence_thresh.setObjectName("doubleSpinBox_confidence_thresh")
        self.gridLayout_2.addWidget(self.doubleSpinBox_confidence_thresh, 1, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem9 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.pushButton_apply = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_apply.setFont(font)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout_8.addWidget(self.pushButton_apply)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Settings"))
        self.label_4.setText(_translate("Dialog", "Colormap"))
        self.label_3.setText(_translate("Dialog", "Temperature Unit"))
        self.checkBox_sound.setText(_translate("Dialog", "Enable Sound"))
        self.checkBox_fps.setText(_translate("Dialog", "Show FPS"))
        self.label_6.setText(_translate("Dialog", "Advanced Settings"))
        self.label_7.setText(_translate("Dialog", "Temperature Threshold"))
        self.label_2.setText(_translate("Dialog", "Face Detection Model"))
        self.label_8.setText(_translate("Dialog", "Model Confidence Threshold"))
        self.pushButton_apply.setText(_translate("Dialog", "Apply"))