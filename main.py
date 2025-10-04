from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui

class MyStyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		
		self.setWindowTitle('My Tool')
		self.resize(300,300)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color : #E0D9D9;')

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
					padding: 8px;s
					font-family: Papirus;
					font-weight: bold;
				}
				QPushButton:pressed {
					background-color: #E0D9D9;
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
