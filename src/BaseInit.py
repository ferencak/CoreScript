import os
from src.BaseLogger import BaseLogger
from src.BaseCompile import BaseCompile
class BaseInit():

	def __init__(self, ProjectName, ProjectLocation):
		self.__ProjectName = ProjectName
		self.__ProjectLocation = ProjectLocation
		self._CurrentPath = os.path.realpath(__file__)
		self._LogFilePath = "logs/latest_log.txt"
		BaseLoggerClass = BaseLogger(self._LogFilePath)
		BaseLoggerClass.LoggerClear()
		BaseLoggerClass.LoggerInsert("Starting compilation for '{0}'.".format(ProjectName))
		BaseLoggerClass.LoggerInsert("Checking if exist 00-DEFAULT.cscript:")
		if os.path.exists(self.__ProjectLocation+"/00-DEFAULT.cscript"):
			BaseLoggerClass.LoggerInsert("- Default script 00-DEFAULT.cscript exist.")
			BaseCompileClass = BaseCompile(self.__ProjectLocation)
			BaseCompileClass.BaseCompileStart()
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			BaseLoggerClass.LoggerExit()
		else:
			BaseLoggerClass.LoggerInsert("- Default script 00-DEFAULT.cscript missing!")
			BaseLoggerClass.LoggerExit()
