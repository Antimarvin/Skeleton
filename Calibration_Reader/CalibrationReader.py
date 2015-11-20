import os

class CalibrationReader:
	def __init__(self, fname):
		self.filename = fname
		self.data = []
		parsefile(self.filename)
		
	def parsefile(self):
		file = open(self.filename)
		for line in file.readlines():
			self.data.append(line)
	
	