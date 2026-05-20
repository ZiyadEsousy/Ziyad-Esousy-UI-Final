import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)

from PySide6.QtCore import Qt


class BudgetApp(QWidget):
    def __init__(self):
        super().__init__()

        self.income = 0
        self.total_expenses = 0
        self.expenses = []

        self.setWindowTitle("💸 Budget Tracker")
        self.resize(500, 650)

        # MAIN LAYOUT
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # TITLE
        title = QLabel("💸 Budget Tracker")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: white;
        """)

        layout.addWidget(title)

        # BALANCE CARD
        self.balance_label = QLabel("Remaining Balance: $0.00")
        self.income_label = QLabel("Income: $0.00")
        self.expense_label = QLabel("Expenses: $0.00")

        for label in [
            self.balance_label,
            self.income_label,
            self.expense_label
        ]:
            label.setStyleSheet("""
                color: white;
                font-size: 18px;
            """)

        balance_card = QWidget()
        balance_layout = QVBoxLayout()

        balance_layout.addWidget(self.balance_label)
        balance_layout.addWidget(self.income_label)
        balance_layout.addWidget(self.expense_label)

        balance_card.setLayout(balance_layout)

        balance_card.setStyleSheet("""
            background-color: #3B82F6;
            border-radius: 20px;
            padding: 20px;
        """)

        layout.addWidget(balance_card)

        # INCOME INPUT
        self.income_input = QLineEdit()
        self.income_input.setPlaceholderText("Monthly Income")

        self.set_income_btn = QPushButton("Set Income")
        self.set_income_btn.clicked.connect(self.set_income)

        layout.addWidget(self.income_input)
        layout.addWidget(self.set_income_btn)

        # EXPENSE NAME
        self.expense_name_input = QLineEdit()
        self.expense_name_input.setPlaceholderText("Expense Name")

        # EXPENSE AMOUNT
        self.expense_amount_input = QLineEdit()
        self.expense_amount_input.setPlaceholderText("Expense Amount")

        self.add_expense_btn = QPushButton("Add Expense")
        self.add_expense_btn.clicked.connect(self.add_expense)

        layout.addWidget(self.expense_name_input)
        layout.addWidget(self.expense_amount_input)
        layout.addWidget(self.add_expense_btn)

        # EXPENSE LIST TITLE
        expense_title = QLabel("Expenses")
        expense_title.setStyleSheet("""
            color: white;
            font-size: 22px;
            font-weight: bold;
        """)

        layout.addWidget(expense_title)

        # EXPENSE LIST
        self.expense_list = QListWidget()

        self.expense_list.setStyleSheet("""
            QListWidget {
                background-color: #1F2937;
                border-radius: 15px;
                padding: 10px;
                color: white;
                font-size: 16px;
            }
        """)

        layout.addWidget(self.expense_list)

        # DELETE BUTTON
        self.delete_btn = QPushButton("Delete Selected Expense")
        self.delete_btn.clicked.connect(self.delete_expense)

        layout.addWidget(self.delete_btn)

        self.setLayout(layout)

        # MAIN WINDOW STYLE
        self.setStyleSheet("""
            QWidget {
                background-color: #111827;
                font-family: Arial;
            }

            QLineEdit {
                background-color: #1F2937;
                color: white;
                border: 2px solid #374151;
                border-radius: 12px;
                padding: 10px;
                font-size: 16px;
            }

            QPushButton {
                background-color: #2563EB;
                color: white;
                border-radius: 12px;
                padding: 12px;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1D4ED8;
            }
        """)

    def set_income(self):
        try:
            self.income = float(self.income_input.text())
            self.update_labels()
        except ValueError:
            QMessageBox.warning(
                self,
                "Error",
                "Enter a valid income amount."
            )

    def add_expense(self):
        name = self.expense_name_input.text()

        try:
            amount = float(self.expense_amount_input.text())

        except ValueError:
            QMessageBox.warning(
                self,
                "Error",
                "Enter a valid expense amount."
            )
            return

        if not name or amount <= 0:
            QMessageBox.warning(
                self,
                "Error",
                "Invalid expense."
            )
            return

        self.expenses.append((name, amount))
        self.total_expenses += amount

        item = QListWidgetItem(f"{name} - ${amount:.2f}")
        self.expense_list.addItem(item)

        self.expense_name_input.clear()
        self.expense_amount_input.clear()

        self.update_labels()

    def delete_expense(self):
        selected_item = self.expense_list.currentRow()

        if selected_item >= 0:

            expense = self.expenses[selected_item]
            self.total_expenses -= expense[1]

            self.expenses.pop(selected_item)

            self.expense_list.takeItem(selected_item)

            self.update_labels()

    def update_labels(self):
        remaining = self.income - self.total_expenses

        self.balance_label.setText(
            f"Remaining Balance: ${remaining:.2f}"
        )

        self.income_label.setText(
            f"Income: ${self.income:.2f}"
        )

        self.expense_label.setText(
            f"Expenses: ${self.total_expenses:.2f}"
        )


app = QApplication(sys.argv)

window = BudgetApp()
window.show()

sys.exit(app.exec())