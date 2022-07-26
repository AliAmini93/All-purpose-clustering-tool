# All-purpose-clustering-tool
Clustering tool powered by ML algorithms.

This is a Python program that uses pyqt5 to cluster data from excel files.
The user may load the input file using the Browse button, and then pick amongst strategies for determining the ideal number of clusters to suit the data. Existing measures for determining optimal cluster numbers include silhouette and distortion.
The program clusters the loaded data using the K-means method when the Run button is pressed. The result tab displays the results, including the members of each cluster and their center.
Finally, the Save button will be used to save these findings to an excel file. This application is built on pyqt5(https://github.com/PyQt5) and utilizes the KElbowVisualizer(https://github.com/DistrictDataLabs/yellowbrick) for selecting the optimal number of clusters based on the silhouette and distortion method.

![Drawing1](https://user-images.githubusercontent.com/96921261/180947601-0f1d2081-a419-47ad-9ca3-4cdec4c399ae.jpg)
