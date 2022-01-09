from PyQt6.QtWidgets import QCheckBox, QLineEdit, QWidget, QGridLayout, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIntValidator, QFont
from PyQt6.QtCore import Qt
from string_generator import StringGenerator

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 225, 175)
        self.setWindowTitle('Random String Generator')
        self.init_ui()

        self.uppercase = False
        self.numbers = False
        self.specials = False

        self.string_generator = StringGenerator()

    def init_ui(self):
        layout = QGridLayout()
        length_input_layout = QHBoxLayout()

        self.length_label = QLabel('Length: ')
        self.length_input = QLineEdit()
        self.length_input.setValidator(QIntValidator())
        self.length_input.setMaxLength(2)
        
        self.upper_checkbox = QCheckBox('Uppercase')
        self.upper_checkbox.setChecked(False)
        self.upper_checkbox.toggled.connect(lambda:self.btn_state(self.upper_checkbox))

        self.numbers_checkbox = QCheckBox('Numbers')
        self.numbers_checkbox.setChecked(False)
        self.numbers_checkbox.toggled.connect(lambda:self.btn_state(self.numbers_checkbox))

        self.specials_checkbox = QCheckBox('Special Characters')
        self.specials_checkbox.setChecked(False)
        self.specials_checkbox.toggled.connect(lambda:self.btn_state(self.specials_checkbox))

        self.generate_button = QPushButton(text='Generate')
        self.generate_button.clicked.connect(self.get_output)
        
        self.output_string = QLineEdit()
        self.output_string.setReadOnly(True)

        length_input_layout.addWidget(self.length_label)
        length_input_layout.addWidget(self.length_input)
        layout.addLayout(length_input_layout, 0, 0)
        layout.addWidget(self.upper_checkbox, 1, 0)
        layout.addWidget(self.numbers_checkbox, 2, 0)
        layout.addWidget(self.specials_checkbox, 3, 0)
        layout.addWidget(self.generate_button, 4, 0)
        layout.addWidget(self.output_string, 5, 0)

        self.setLayout(layout)

    def get_output(self):
        passes_validation = False
        while not passes_validation:
            output = self.string_generator.generate(int(self.length_input.text()), upper=self.uppercase, numbers=self.numbers, specials=self.specials)
            passes_validation = self.string_generator.validate(output, upper=self.uppercase, numbers=self.numbers, specials=self.specials)
            if not passes_validation: print('Failed validation')
        
        print('Passed validation')
        self.output_string.setText(f'{output}')

    def btn_state(self, btn):
        if btn.text() == 'Uppercase':
            self.uppercase = True if btn.isChecked() else False
        
        if btn.text() == 'Numbers':
            self.numbers = True if btn.isChecked() else False
        
        if btn.text() == 'Special Characters':
            self.specials = True if btn.isChecked() else False
            

