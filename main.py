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

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('Name :')
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)

		self.createButton = QtWidgets.QPushButton('Create')
		self.cancelButton = QtWidgets.QPushButton('Cancel')
		self.buttonLayout.addWidget(self.createButton)
		self.buttonLayout.addWidget(self.cancelButton)

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
