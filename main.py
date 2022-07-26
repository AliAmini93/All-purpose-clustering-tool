import pandas as pd
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from About_Us import Ui_AboutUs
from About_Application import Ui_AboutApp
def is_number(s):
    try:
        float(s) or int(s)
        return True
    except ValueError:
        return False

class Ui_MainWindow(object):        
    def OpenWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_AboutApp()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_AboutUs()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 591)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("post.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Browse.setFont(font)
        self.Browse.setObjectName("Browse")
        self.verticalLayout_5.addWidget(self.Browse)
        #########################################################
        self.Browse.clicked.connect(self.clicker)
        #########################################################
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Silhouette = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Silhouette.setFont(font)
        self.Silhouette.setObjectName("Silhouette")
        self.horizontalLayout_2.addWidget(self.Silhouette)
        ########################################################
        self.Silhouette.setEnabled(False)
        self.Silhouette.toggled.connect(self.Metric_Choosing)
        ########################################################
        self.Distortion = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Distortion.setFont(font)
        self.Distortion.setObjectName("Distortion")
        self.horizontalLayout_2.addWidget(self.Distortion)
        ########################################################
        self.Distortion.setEnabled(False)
        self.Distortion.toggled.connect(self.Metric_Choosing)
        ########################################################
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Run.setFont(font)
        self.Run.setObjectName("Run")
        self.verticalLayout_5.addWidget(self.Run)
        #########################################################
        self.Run.setEnabled(False)
        self.Run.clicked.connect(self.Preprocess_Dataset)
        #########################################################
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Save.setFont(font)
        self.Save.setObjectName("Save")
        self.verticalLayout_5.addWidget(self.Save)
        #########################################################
        self.Save.setEnabled(False)
        self.Save.clicked.connect(self.Save_Result)
        #########################################################
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Tab = QtWidgets.QTabWidget(self.centralwidget)
        self.Tab.setObjectName("Tab")
        self.Log = QtWidgets.QWidget()
        self.Log.setObjectName("Log")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Log)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Log1 = QtWidgets.QTextBrowser(self.Log)
        self.Log1.setObjectName("Log1")
        self.verticalLayout_4.addWidget(self.Log1)
        self.Tab.addTab(self.Log, "")
        self.Result = QtWidgets.QWidget()
        self.Result.setObjectName("Result")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Result)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Result1 = QtWidgets.QTextBrowser(self.Result)
        self.Result1.setObjectName("Result1")
        self.verticalLayout_3.addWidget(self.Result1)
        self.Tab.addTab(self.Result, "")
        self.verticalLayout.addWidget(self.Tab)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AboutUs = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.openWindow())
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutUs.setFont(font)
        self.AboutUs.setObjectName("AboutUs")
        self.horizontalLayout.addWidget(self.AboutUs)
        self.AboutSoftware = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.OpenWindow())
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutSoftware.setFont(font)
        self.AboutSoftware.setObjectName("AboutSoftware")
        self.horizontalLayout.addWidget(self.AboutSoftware)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "All-Purpose Clusterer"))
        self.label.setText(_translate("MainWindow", "Clustering Tool"))
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "Method for Finding optimal cluster number"))
        self.Silhouette.setText(_translate("MainWindow", "Silhouette"))
        self.Distortion.setText(_translate("MainWindow", "Distortion"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.Tab.setTabText(self.Tab.indexOf(self.Log), _translate("MainWindow", "Log"))
        self.Tab.setTabText(self.Tab.indexOf(self.Result), _translate("MainWindow", "Result"))
        self.AboutUs.setText(_translate("MainWindow", "About Us"))
        self.AboutSoftware.setText(_translate("MainWindow", "About Application"))
        
    def clicker(self):
        app.processEvents()
        self.Log1.clear()
        self.Result1.clear()
        path,_ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', '', 'Excel (*.xls, *.xlsx *.xlsm)')
        print(path)
        if path:
            df = pd.read_excel(path)
            dataset = df.values
            self.Log1.append("File has been loaded successfully.")
            self.Log1.append("\nThe File location is: "+ str(path))
            self.dataset = dataset
            self.Distortion.setEnabled(True)
            self.Silhouette.setEnabled(True)
            return(dataset)
            
        else:
            self.Log1.append("\nNo File selected...")
       
    def Preprocess_Dataset(self):
        dataset = self.dataset
        app.processEvents()
        I = dataset.shape[0]
        J = dataset.shape[1]
        ###### X is data without label and X_bolean is made for checking whter all data is number or not!
        X = []
        X_bolean = []
        for i in range(I):
          for j in range(2, J):
            X.append(dataset[i][j])
            X_bolean.append(is_number(str(dataset[i][j])))
        ##### Creating data with label
        X1 = []
        for i in range(I):
          for j in range(1, J):
            X1.append(dataset[i][j])
            
        
        ###### Cause is_number func didn't support nan, we used isna from pandas    
        Isnan = pd.isna(X)    
        Res_nan = False
        Res = True
        for i in range(len(Isnan)):
            Res_nan = Res_nan or Isnan[i]
            Res = Res and X_bolean[i]
        if (Res==True and Res_nan==False):
           # Checking whether number of samples is more than 3.
           if I>3:
               X = np.array(X)
               X = np.reshape(X,(I,J-2))
               X1 = np.array(X1)
               X1 = np.reshape(X1,(I,J-1))
               self.Log1.append("\nThe data format is ok.")
               self.X = X
               self.X1 = X1
               self.Finding_Optimal()
           else:
                self.Log1.append("\nThe Number of samples should be at least 4.")
        else:
            self.Log1.append("\nThe File format is not supported. For more information, visit the 'About Application' section.")
        
    def Metric_Choosing(self):
        app.processEvents()
        if self.Distortion.isChecked():
            s ="distortion"
        else:
            s ="silhouette"
        self.Run.setEnabled(True)
        return(s)
    
    def Metric_Changing(self,M):
        if (M=="distortion"):
            s="silhouette"
        else:
            s ="distortion"
        return(s)    
    
    def Finding_Optimal(self):
        app.processEvents()
        s = self.Metric_Choosing()
        self.Log1.append("\nThe metric is %s"%(str(s)))
        X = self.X
        X1 = self.X1
        ############## Finding optimal K ###################
        from sklearn.cluster import KMeans
        # Elbow Method for K means
        # Import ElbowVisualizer
        from yellowbrick.cluster import KElbowVisualizer
        model0 = KMeans()
        # k is range of number of clusters.
        visualizer0 = KElbowVisualizer(model0, k=(2,X.shape[0]), metric=s, timings= True)
        visualizer0.fit(X)        # Fit data to visualizer
        k0 = visualizer0.elbow_value_
        itr = 0
        while (k0 == None):
            itr = itr + 1
            if (itr==2):
                self.Log1.append("\nSorry! We can't find any optimal cluster number for this data.")
            self.Log1.append("\n%s metric didn't find any optimal cluster number!"%(str(s)))
            self.Log1.append("\nMetric is changing...")
            s = self.Metric_Changing(s)
            self.Log1.append("\nThe new metric is %s"%(s))
            visualizer0 = KElbowVisualizer(model0, k=(2,X.shape[0]), metric=s, timings= True)
            visualizer0.fit(X)        # Fit data to visualizer
            k0 = visualizer0.elbow_value_
            
            
        k0 = int(visualizer0.elbow_value_)
        print(k0)
        self.Log1.append("\nThe optimal number of clusters is: "+ str(k0))
        self.Log1.append("\nYou can see the results in corresponding tab.")
        self.X = X
        self.X1 = X1
        self.k0 = k0
        self.Run_App()
              
    def Run_App(self):
        app.processEvents()
        X = self.X
        X1 = self.X1
        k0 = self.k0
        from sklearn.cluster import KMeans
        #k0 = self.k0
        ########## k-means clustering ##########################        
        # define the model
        model2 = KMeans(n_clusters=k0)
        # fit the model
        model2.fit(X)
        # assign a cluster to each example
        yhat = model2.predict(X)
        ################ clusters result ##########
        cluster =[[] for i in range(int(k0))]
        for i in range(len(yhat)):
            cluster[yhat[i]].append(X1[i][0])
            
        centers = model2.cluster_centers_
        
        for i in range(k0):
            self.Result1.append("\nCluster %d is %s:" %(i+1, str(cluster[i])))
            self.Result1.append('\nThe center of cluster %d is %s.' %(int(i+1), str(list(centers[i]))))
        self.cluster = cluster
        self.k0 = k0
        self.Save.setEnabled(True)
       
    def Save_Result(self):
        app.processEvents()
        cluster = self.cluster
        k0 = self.k0
        dic = {}
        for i in range(k0):
            dic['Cluster'+str(i+1)] = cluster[i]
        df1 = pd.DataFrame.from_dict(dic, orient='index')
        path2,_ = QtWidgets.QFileDialog.getSaveFileName(None, 'Save file', '', 'Excel (*.xlsx)')
        print(path2)
        if path2:
            df1.to_excel(path2)
            self.Log1.append("\nFile has been saved successfully.")
            self.Log1.append("The File location is: "+ str(path2))
        else:
            self.Log1.append("\nThe File has not been saved.")
         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
