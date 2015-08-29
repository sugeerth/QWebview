import sys  
from PySide import QtCore, QtGui, QtWebKit  
from PySide.QtCore import QObject, Property
  
"""Html snippet."""  
html = """ 
<html><body> 
  <center> 
  <script language="JavaScript"> 
    document.write('<p>Python ' + pyObj.pyVersion + '</p>') 
  </script> 
  <button onClick="pyObj.showMessage(pyObj.pyVersion +'iiiiiirom WebKit')">Press me</button> 
  </center> 
</body></html> 
"""  
  
class StupidClass(QtCore.QObject):  
    """Simple class with one slot and one read-only property."""  
 
    @QtCore.Slot(str)  
    def showMessage(self, msg):  
        """Open a message box and display the specified message."""  
        QtGui.QMessageBox.information(None, "Info", msg)  
        print "asdas"
  
    def makeInertison(self,Yo):
        print Yo


    def _pyVersion(self):  
        """Return the Python version."""  
        return sys.version  
  
    """Python interpreter version property."""  
    pyVersion = Property(str, fget=_pyVersion)  
  
def main():  
    app = QtGui.QApplication(sys.argv)  
  
    myObj = StupidClass()  
  
    webView = QtWebKit.QWebView()  
    # Make myObj exposed as JavaScript object named 'pyObj'  
    webView.page().mainFrame().addToJavaScriptWindowObject("pyObj", myObj)  
    webView.setHtml(html)  
  
    window = QtGui.QMainWindow()  
    window.setCentralWidget(webView)  
    window.show()  
  
    sys.exit(app.exec_())  
  
if __name__ == "__main__":  
    main()  