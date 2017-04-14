import os, time

class BaseLogger():
	
	def __init__(self, LogFilePath):
		self._LogFilePath = LogFilePath;

	def LoggerClear(self):
		with open(self._LogFilePath, "w") as Logger:
			Logger.write("")
			Logger.close()

	def LoggerInsert(self, insertLog):
		with open(self._LogFilePath, "a") as Logger:
			Logger.write(insertLog+"\n")
			Logger.close()

	def LoggerExit(self):
		self.LoggerInsert("Cannot compile project! Breaked in {0}".format(time.strftime('%H:%M:%S')))