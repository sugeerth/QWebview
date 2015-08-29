import sys
from PySide import QtCore
 
# define a new slot that receives a string and has
# 'saySomeWords' as its name
@QtCore.Slot(str)
def saySomeWords(words):
 print words


@QtCore.Slot(str)
def sayTwoWords(words):
 print words + "Two"


@QtCore.Slot(str)
def sayThreeWords(words):
 print words + "Three"

@QtCore.Slot(int)
@QtCore.Slot(str)
def sayFourWords(words):
 print words, "Four"
 
class Communicate(QtCore.QObject):
 # create a new signal on the fly and name it 'speak'
 speak = QtCore.Signal(str)
 moreSignals = QtCore.Signal(str)
 sign = QtCore.Signal(int)

someone = Communicate()
# connect signal and slot
someone.speak.connect(saySomeWords)
someone.speak.connect(sayFourWords)

someone.moreSignals.connect(sayFourWords)
someone.sign.connect(sayFourWords)


# emit 'speak' signal
someone.sign.emit(23)
someone.moreSignals.emit("asdada")

someone.speak.emit("Awesome slots !")
