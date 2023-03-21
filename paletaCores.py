import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QColorDialog, QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtGui import QClipboard, QColor
from PyQt5.QtCore import Qt

class ColorPalette(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Paleta de Cores - HEX / RGB')

        layout = QVBoxLayout()

        self.color_dialog_button = QPushButton('Selecionar Cor', self)
        self.color_dialog_button.clicked.connect(self.open_color_dialog)

        # Adicionando um layout horizontal para o código HEX
        hex_layout = QHBoxLayout()
        hex_label = QLabel('HEX:')
        self.hex_line_edit = QLineEdit(self)
        self.hex_line_edit.setPlaceholderText('Código HEX da cor selecionada')
        hex_copy_button = QPushButton('Copiar', self)
        hex_copy_button.clicked.connect(self.copy_hex)
        hex_layout.addWidget(hex_label)
        hex_layout.addWidget(self.hex_line_edit)
        hex_layout.addWidget(hex_copy_button)

        # Adicionando um layout horizontal para o código RGB
        rgb_layout = QHBoxLayout()
        rgb_label = QLabel('RGB:')
        self.rgb_line_edit = QLineEdit(self)
        self.rgb_line_edit.setPlaceholderText('Código RGB da cor selecionada')
        rgb_copy_button = QPushButton('Copiar', self)
        rgb_copy_button.clicked.connect(self.copy_rgb)
        rgb_layout.addWidget(rgb_label)
        rgb_layout.addWidget(self.rgb_line_edit)
        rgb_layout.addWidget(rgb_copy_button)

        # Adicionando uma QLabel para exibir a cor selecionada
        self.color_label = QLabel(self)
        self.color_label.setFixedHeight(50)
        self.color_label.setStyleSheet("background-color: white; border: 1px solid black;")
        self.color_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout.addWidget(self.color_dialog_button)
        layout.addLayout(hex_layout)
        layout.addLayout(rgb_layout)
        layout.addWidget(self.color_label)

        self.setLayout(layout)

    def open_color_dialog(self):
        color = QColorDialog.getColor(Qt.white, self, 'Selecionar Cor')
        if color.isValid():
            self.hex_line_edit.setText(color.name())
            self.rgb_line_edit.setText(f'({color.red()}, {color.green()}, {color.blue()})')
            self.update_color_label(color)

    def copy_hex(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.hex_line_edit.text())

    def copy_rgb(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.rgb_line_edit.text())

    def update_color_label(self, color: QColor):
        self.color_label.setStyleSheet(f"background-color: {color.name()}; border: 1px solid black;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = ColorPalette()
    window.show()
    window.setFixedSize(400,200)
    window.setMaximumSize(400,200)

    sys.exit(app.exec_())
