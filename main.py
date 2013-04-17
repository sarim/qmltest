#!/usr/bin/env python

import sys
from PySide import QtCore, QtGui, QtDeclarative

class GittuCM( QtCore.QObject ):
    def __init__( self ):
        QtCore.QObject.__init__(self)

    @QtCore.Slot('QString')
    def printText(self,text):
        print text

    @QtCore.Slot()
    def quitMe(self):
        sys.exit()
        
class dTypeView ( QtDeclarative.QDeclarativeView ):
    def __init__( self, parent=None ):
        super( dTypeView, self ).__init__( parent )
        self.setSource( QtCore.QUrl.fromLocalFile( './Main.qml' ) )
        self.setResizeMode( QtDeclarative.QDeclarativeView.SizeRootObjectToView )
        self.gittuParent = parent
        
    @QtCore.Slot("QMouseEvent")
    def mouseMoveEvent(self,event):

        print event.globalPos(), event.pos() 
        if (event.buttons() & QtCore.Qt.LeftButton ):
            self.gittuParent.move(event.globalPos() - self.dragpos )
            event.accept()

class MainWindow( QtGui.QMainWindow ):
    def __init__( self, parent=None ):
        super( MainWindow, self ).__init__( parent )
        self.setWindowTitle( "Test" )

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.dView = dTypeView(self)
        
        self.setCentralWidget(self.dView)
        
    @QtCore.Slot("QMouseEvent")
    def mousePressEvent(self,event):
        if (event.button() == QtCore.Qt.LeftButton):
            self.dView.dragpos = event.globalPos() - self.frameGeometry().topLeft()


app = QtGui.QApplication( sys.argv )
window = MainWindow()
context = window.dView.rootContext()
context.setContextProperty("GittuCM",GittuCM())
window.show()
sys.exit( app.exec_() )
