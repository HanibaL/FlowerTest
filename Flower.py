# utf-8
from tkinter import *
from tkinter.messagebox import *
import random

class FlowerCell(object):
	"""docstring for FlowerCell"""
	def __init__(self, row, column):
		self.row = row
		self.column = column
		self.value = 0
		self.type = 'False'

		markSequence = [ 'False', 'True' ]

	def getValue(self):
		return self.value

	def setValue(self, value):
		self.value = value

	def click( self, value ):
		if self.value == value:
			self.type = 'True'



class FlowerModel:
	"""docstring for FlowerModel"""
	def __init__(self):
		self.startTest()

	def startTest( self, rowCount = 3, columnCount = 3 ):
		self.firstStep = True
		self.testOver = False
		self.cellsTable = []


	def checkCell(self, row, column):
		pass

	def setCenterCell(self, row, column, value):
		pass



class FlowerView( Frame ):
	def __init__( self, model, controller, parent = None ):
		Frame.__init__( self, parent )
		self.model = model
		self.controller = controller
		self.controller.setView( self )
		self.createBoard()

		panel = Frame( self )
		panel.pack( side = BOTTOM, fill = X )

		Button( panel, text = 'New test', command = self.controller.startNewTest ).pack( side = RIGHT )

	def createBoard( self ):
		try:
			self.board.pack_forget()
			self.board.destroy()

			self.rowCount.set( self.model.rowCount )
			self.columnCount.set( self.model.columnCount )
		except:
			pass

		self.board = Frame( self )
		self.board.pack()
		self.buttonTable = []


class FlowerController:
	def __init__( self, model ):
		self.model = model

	def setView( self, view ):
		self.view = view

	def startNewTest( self ):
		testSettings = self.view.getTestSettings()
		try:
			self.model.startTest( *map( int, testSettings ) )
		except:
			self.model.startTest( self.model.rowCount, self.model.columnCount, self.model.flowerCount )

		self.view.createBoard()

	def onRightClick( self, row, column ):
		pass


model = FlowerModel()
controller = FlowerController( model )
view = FlowerView( model, controller )
view.pack()
view.mainloop()
