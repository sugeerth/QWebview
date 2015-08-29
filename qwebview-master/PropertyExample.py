from PySide.QtCore import QObject, Property
 
class MyObject(QObject):
 def __init__(self,startval=42):
	 QObject.__init__(self)
	 self.ppval = startval
 
def readPP(self):
 return self.ppval
 
def setPP(self,val):
 self.ppval = val
 
pp = Property(int, readPP, setPP)
 
obj = MyObject()
obj.pp = 47
print (obj.pp)