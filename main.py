import sys
from PySide6.QtWidgets import (
    QApplication,
    QStackedWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def create_page(text):
    page = QWidget()
    layout = QVBoxLayout()
    label = QLabel(text)
    layout.addWidget(label)
    page.setLayout(layout)
    return page


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()

    page1 = create_page("This is Page 1")
    page2 = create_page("This is Page 2")
    page3 = create_page("This is Page 3")

    stacked_widget.addWidget(page1)
    stacked_widget.addWidget(page2)
    stacked_widget.addWidget(page3)

    button_previous = QPushButton("Previous")
    button_next = QPushButton("Next")

    def go_to_previous_page():
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex() - 1)

    def go_to_next_page():
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex() + 1)

    button_previous.clicked.connect(go_to_previous_page)
    button_next.clicked.connect(go_to_next_page)

    layout = QVBoxLayout()
    layout.addWidget(stacked_widget)
    layout.addWidget(button_previous)
    layout.addWidget(button_next)

    main_widget = QWidget()
    main_widget.setLayout(layout)
    main_widget.setWindowTitle("QStackedWidget Example")
    main_widget.show()

    sys.exit(app.exec())
