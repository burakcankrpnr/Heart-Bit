import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QScrollArea
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtGui import QFont, QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__() #parents yapısı dede torun super ile sağlanır kalıtım yani
        self.initUI() #arayüzü başlatmak veya calıstırmak icin

    def initUI(self):
        self.setWindowIcon(QIcon('C:\heart2.jpg'))
        self.setWindowTitle('Heart Beat')
        self.setStyleSheet("background-color: black;") #cccccc yedek renk
        self.showFullScreen()

        self.bit_counter = 0
        self.byte_counter = 1

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.add_to_list)

        label_font = QFont('Arial', 16 , QFont.Bold)

        self.left_label = QLabel('Data', self)
        self.left_label.setFont(label_font)
        self.left_label.setStyleSheet("background-color: #b2b2b2; padding: 10px;")
        self.left_label.setAlignment(Qt.AlignCenter)

        self.middle_label = QLabel('Location', self)
        self.middle_label.setFont(label_font)
        self.middle_label.setStyleSheet("background-color: #b2b2b2; padding: 10px;")
        self.middle_label.setAlignment(Qt.AlignCenter)

        self.right_label = QLabel('Date', self)
        self.right_label.setFont(label_font)
        self.right_label.setStyleSheet("background-color: #b2b2b2; padding: 10px; ")
        self.right_label.setAlignment(Qt.AlignCenter)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollBar:vertical {
                background: #cccccc;
                width: 20px;
            }
            QScrollBar::handle:vertical {
                background: #666666;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical {
                background: #cccccc;
                height: 20px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical {
                background: #cccccc;
                height: 20px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)

        self.left_listbox = QListWidget(self)
        self.left_listbox.setStyleSheet("background-color: #666666; color: white; font-weight: bold; padding: 30px; font-size: 30px; ")
        self.middle_listbox = QListWidget(self)
        self.middle_listbox.setStyleSheet("background-color: #666666; color: white; font-weight: bold; padding: 30px; font-size: 30px;")
        self.right_listbox = QListWidget(self)
        self.right_listbox.setStyleSheet("background-color: #666666; color: white; font-weight: bold; padding: 30px; font-size: 30px; ")

        button_font = QFont('Arial', 20, QFont.Bold)
        self.start_button = QPushButton('Start', self)
        self.start_button.setStyleSheet("background-color:green ; padding: 20px; ")
        self.start_button.setFont(button_font)
        self.start_button.clicked.connect(self.button_click)

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.setStyleSheet("background-color: red; padding: 20px;")
        self.stop_button.setFont(button_font)
        self.stop_button.clicked.connect(self.stop_timer)

        self.exit_button = QPushButton('Tam Ekrandan Çık', self)
        self.exit_button.setStyleSheet("background-color: lightgreen; padding: 25px; font-size: 18px; font-weight: bold;")
        self.exit_button.setFont(button_font)
        self.exit_button.clicked.connect(self.exit_fullscreen)

        self.fullscreen_button = QPushButton('Tam Ekran', self)
        self.fullscreen_button.setStyleSheet("background-color: lightblue; padding: 20px; ")
        self.fullscreen_button.setFont(button_font)
        self.fullscreen_button.clicked.connect(self.toggle_fullscreen)

        # Layouts
        grid = QGridLayout()
        grid.addWidget(self.left_label, 0, 0)
        grid.addWidget(self.middle_label, 0, 1)
        grid.addWidget(self.right_label, 0, 2)
        grid.addWidget(self.left_listbox, 1, 0)
        grid.addWidget(self.middle_listbox, 1, 1)
        grid.addWidget(self.right_listbox, 1, 2)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.fullscreen_button)
        button_layout.addWidget(self.exit_button)
        button_layout.addWidget(self.stop_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(grid)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def button_click(self):
        self.timer.start(1000)

    def toggle_fullscreen(self):
        if not self.isFullScreen():
            self.showFullScreen()

    def add_to_list(self):
        self.bit_counter += 1
        if self.bit_counter > 8:
            self.bit_counter = 1
            self.byte_counter += 1

        current_time = QDateTime.currentDateTime().toString("dd/MM/yyyy HH:mm:ss")
        bit_info = f"{self.byte_counter}. byte {self.bit_counter}. bit"

        self.middle_listbox.insertItem(0, bit_info)
        self.right_listbox.insertItem(0, current_time)
        self.left_listbox.insertItem(0, '1')

    def stop_timer(self):
        self.timer.stop()

    def exit_fullscreen(self):
        self.showNormal()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
