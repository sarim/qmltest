 import QtQuick 1.0

 Rectangle {
     id: page
     width: 500; height: 200
     color: "lightgray"

     Rectangle {
        id: titlebar
        width: 25
        height: 25
        x: 475
        y: 0

        Text {
        x: 5
        text: "X"
        font.pointSize: 18
        }

        MouseArea {
            anchors.fill: parent
            onClicked: {
                GittuCM.quitMe()
            }
        }
     }

     Text {
         id: helloText
         text: "Hello world!"
         y: 30
         anchors.horizontalCenter: page.horizontalCenter
         font.pointSize: 24; font.bold: true
     }

     Grid {
         id: colorPicker
         x: 4; anchors.bottom: page.bottom; anchors.bottomMargin: 4
         rows: 2; columns: 3; spacing: 3

         Cell { cellColor: "red"; onClicked: helloText.color = cellColor }
         Cell { cellColor: "green"; onClicked: helloText.color = cellColor }
         Cell { cellColor: "blue"; onClicked: helloText.color = cellColor }
         Cell { cellColor: "yellow"; onClicked: helloText.color = cellColor }
         Cell { cellColor: "steelblue"; onClicked: helloText.color = cellColor }
         Cell { cellColor: "black"; onClicked: helloText.color = cellColor }
     }
 }

