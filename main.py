from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui

ROOT_RESOURCE_DIR = 'C:/Users/ICT68/Documents/maya/2025/scripts/myStyleTool/resource'

class MyStyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		
		self.setWindowTitle('My Tool')
		self.resize(300,300)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color : #F5F5F0;')

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/image/background.jpg")
		scale_pixmap = self.imagePixmap.scaled(
			QtCore.QSize(256,256),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)
		self.imageLabel.setPixmap(scale_pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('Name :')
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)
		self.nameLabel.setStyleSheet(
			'''
				QLabel {
	                color: #432323;
	                font-family: Papirus;
	                font-size: 20px;
	                font-weight: bold;
	                padding: 10px;
				}

			'''
		)
		self.nameLineEdit.setStyleSheet("""
	            QLineEdit {
	                background-color: #E0D9D9;
	                border: 2px solid #2F5755;
	                border-radius: 5px;
	                padding: 5px;
	                color: #432323;
	                font-size: 14px;
	            }
	            QLineEdit:focus {
	                border: 2px solid #2F5755;
	            }
	            QLineEdit:hover {
	                background-color: #E0D9D9;
	            }
        """)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)

		self.createButton = QtWidgets.QPushButton('Create')
		self.cancelButton = QtWidgets.QPushButton('Cancel')
		self.buttonLayout.addWidget(self.createButton)
		self.buttonLayout.addWidget(self.cancelButton)
		self.createButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #432323;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					padding: 8px;
					font-family: Papirus;
					font-weight: bold;
				}
				QPushButton:pressed {
					background-color: #5A9690;
				}
			'''

		)
		self.cancelButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #5A9690;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					padding: 8px;
					font-family: Papirus;
					font-weight: bold;
				}
				QPushButton:pressed {
					background-color: #432323;
				}
			'''
		)

		self.mainLayout.addStretch()

def run():
	global ui
	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = MyStyleToolDialog(parent=ptr)
	ui.show()
