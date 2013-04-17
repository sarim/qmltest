import QtQuick 1.0

Rectangle {
    width: 200
    height: 200
    color: "white"

    Rectangle {
        anchors.centerIn: parent
        width: 100
        height: 20
        color: "black"
        Text {
            anchors.centerIn: parent
            text: "click"
            color: "white"
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                testModel.printText("test")
            }
        }
    }
}
