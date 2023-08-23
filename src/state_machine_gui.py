from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QComboBox, QLineEdit, QMessageBox
from state_machine import *


class StateMachineUI(QWidget):
    def __init__(self):
        super().__init__()
        self.vending_machine = VendingMachine()
        self.initUI()

    def initUI(self) -> None:
        self.setWindowTitle("State Machine")
        self.setGeometry(300, 300, 300, 300)

        self.init_buttons()
        self.init_labels()
        self.init_boxes()
        self.show()

    def init_buttons(self) -> None:
        self.quit = QPushButton("Quit", self)
        self.reset = QPushButton("Reset", self)
        self.insert_coin = QPushButton("Insert Coin", self)
        self.vend = QPushButton("Vend", self)
        self.refund = QPushButton("Refund", self)

        self.quit.move(200, 250)
        self.reset.move(125, 250)
        self.insert_coin.move(5, 200)
        self.vend.move(125, 200)
        self.refund.move(200, 200)

        self.quit.clicked.connect(self.quit_event)
        self.reset.clicked.connect(self.reset_event)
        self.insert_coin.clicked.connect(self.insert_coin_event)
        self.vend.clicked.connect(self.vend_event)
        self.refund.clicked.connect(self.refund_event)

        self.setStyleSheet(
            "QPushButton { background-color: #444444; color: white; font-size: 16px; font-weight: bold; "
            "border-radius: 7px; border: 2px solid black; padding: 5px; }"
            "QPushButton:hover { background-color: #00AA00; }"
        )

    def init_labels(self) -> None:
        self.vending_machine_label = QLabel("Vending Machine", self)
        self.state_label = QLabel("Current State", self)
        self.message_label = QLabel("Message", self)

        self.vending_machine_label.move(100, 10)
        self.state_label.move(20, 50)
        self.message_label.move(20, 150)

    def init_boxes(self) -> None:
        self.current_state = QLineEdit(self)
        self.current_state.move(100, 50)
        self.current_state.setReadOnly(True)
        self.current_state.setText("Idle")

        self.message_result = QLineEdit(self)
        self.message_result.move(100, 150)

    def insert_coin_event(self) -> None:
        try:
            self.vending_machine.insert_coin()
            self.message_result.setText("Coin inserted")
            self.current_state.setText(self.vending_machine.waiting.value)
        except TransitionNotAllowed as e:
            QMessageBox.critical(self, "Error", str(e))

    def vend_event(self) -> None:
        try:
            self.vending_machine.vend()
            self.message_result.setText("Vended")
            self.current_state.setText(self.vending_machine.vended.value)
        except TransitionNotAllowed as e:
            QMessageBox.critical(self, "Error", str(e))

    def refund_event(self) -> None:
        try:
            self.vending_machine.refund()
            self.message_result.setText("Refunded")
            self.current_state.setText(self.vending_machine.refunded.value)
        except TransitionNotAllowed as e:
            QMessageBox.critical(self, "Error", str(e))

    def reset_event(self) -> None:
        try:
            self.vending_machine.reset()
            self.message_result.setText("")
            self.current_state.setText(self.vending_machine.idle.value)
        except TransitionNotAllowed as e:
            QMessageBox.critical(self, "Error", str(e))

    def quit_event(self) -> None:
        self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ex = StateMachineUI()
    sys.exit(app.exec_())
