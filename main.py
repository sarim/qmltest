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

class MainWindow( QtDeclarative.QDeclarativeView ):
    def __init__( self, parent=None ):
        super( MainWindow, self ).__init__( parent )
        self.setWindowTitle( "Test" )
        #print self.mouseMove.connect
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setSource( QtCore.QUrl.fromLocalFile( './Main.qml' ) )
        self.setResizeMode( QtDeclarative.QDeclarativeView.SizeRootObjectToView )

    @QtCore.Slot("QMouseEvent")
    def mouseMoveEvent(self,event):
        ex = event.pos().x()
        ey = event.pos().y()
        gx = event.globalPos().x()
        gy = event.globalPos().y()
        # if (ex > 3):
        #     self.lx = ex
        #     self.ly = ey
        #     print ex - gx , ey - gy
        #     self.move(ex , ey )
        # else:
        #     self.move(gx , gy )
        
        print event.globalPos(), event.pos() 
        self.move(gx , gy )

app = QtGui.QApplication( sys.argv )
window = MainWindow()
context = window.rootContext()
context.setContextProperty("GittuCM",GittuCM())
window.show()
sys.exit( app.exec_() )
