# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About_Application.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutApp(object):
    def setupUi(self, AboutApp):
        AboutApp.setObjectName("AboutApp")
        AboutApp.resize(514, 508)
        self.horizontalLayout = QtWidgets.QHBoxLayout(AboutApp)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(AboutApp)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)

        self.retranslateUi(AboutApp)
        QtCore.QMetaObject.connectSlotsByName(AboutApp)

    def retranslateUi(self, AboutApp):
        _translate = QtCore.QCoreApplication.translate
        AboutApp.setWindowTitle(_translate("AboutApp", "About Software"))
        self.textBrowser.setHtml(_translate("AboutApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Version 1.0</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">This application finds optimal cluster numbers using the Distortion and Silhouette metric and categorizes the input data utilizing the K-means algorithm.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Use the Browse button to upload your input data in(*.xls, *.xlsx, *.xlsm) format.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The input data format must be as shown below.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/Sample.JPG\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The software reserves the first and second columns for the sample number and sample name, respectively, and requires the user to prepare them. The third and subsequent columns are used to organize the characteristics of each sample and must be changed by the user. Finally, you may download the results as an Excel file. Additionally, you may see these findings on the Result tab. If you have any questions about how to use this program, you may go to the About us section.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))

import Source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutApp = QtWidgets.QDialog()
    ui = Ui_AboutApp()
    ui.setupUi(AboutApp)
    AboutApp.show()
    sys.exit(app.exec_())

