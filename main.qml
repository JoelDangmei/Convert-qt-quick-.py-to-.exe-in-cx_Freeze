import QtQuick
import QtQuick.Window
import QtQuick.Controls

ApplicationWindow {
    title: "Hello YouTube"
    visible: true
    width: 300
    height: 300
    color: "#292929"

    // When window is loaded
    Component.onCompleted: {
        x = Screen.width / 2 - width / 2
        y = Screen.height / 2 - height / 2
    }
    
    Text {
        color: "white"
        font.pointSize: 12
        anchors.centerIn: parent
        text: qsTr("Hello World")
    }
}