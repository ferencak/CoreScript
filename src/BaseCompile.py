import os, time

ALLOWED_CONST = []

class BaseCompile():

	def __init__(self, Project):
		self._Project = Project

		with open(self._Project+"/00-DEFAULT.cscript", "r") as ProjectContent:
			self._ProjectContent = ProjectContent.read()

	def BaseCompileStart(self): 
		Content = list(self._ProjectContent)
		ContentLen = len(Content)
		ContentString = ""
		CONST_STATE = 0
		CONST_STRING = ""

		for char in Content:
			ContentString += char
			if ContentString == " ":
				if CONST_STATE == 0:
					ContentString = ""
				else:
					ContentString = " "
			elif ContentString == "\n":
				ContentString = ""
			elif ContentString == "ECHO" or ContentString == "echo":
				ALLOWED_CONST.append("ECHO")
				ContentString = ""
			elif ContentString == "PRINT" or ContentString == "print":
				ALLOWED_CONST.append("PRINT")
				ContentString = ""
			elif ContentString == "\"":
				if CONST_STATE == 0:
					CONST_STATE = 1
				elif CONST_STATE == 1:
					ALLOWED_CONST.append("STRING:"+CONST_STRING + "\"")
					CONST_STRING = ""
					CONST_STATE = 0
					ContentString = ""
			elif CONST_STATE == 1:
				CONST_STRING += ContentString
				ContentString = ""
		self.BaseCompileParse(ALLOWED_CONST)		

	def BaseCompileParse(self, Const):
		i = 0
		while(i < len(Const)):
			if Const[i] + " " + Const[i+1][0:6] == "PRINT STRING":
				print(Const[i+1][7:])
				i+=2