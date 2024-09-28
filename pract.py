from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication
import sys

app = QApplication(sys.argv)
window = QWidget()

layout = QVBoxLayout()

button1 = QPushButton('Button 1')
button2 = QPushButton('Button 2')

layout.addWidget(button1)
layout.addWidget(button2)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())

