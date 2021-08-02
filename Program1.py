from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import mysql.connector as mc
from datetime import datetime

class Window(QWidget):
    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()
        self.form()
        vbox.addLayout(self.hbox1)
        # vbox.addStretch(1)
        vbox.addLayout(self.hbox2)
        # vbox.addStretch(2)
        vbox.addLayout(self.hbox3)
        # vbox.addStretch(3)
        vbox.addLayout(self.hbox4)
        vbox.addStretch(4)
        vbox.addWidget(self.submitBtn)
        vbox.addWidget(self.ackLabel)

        self.setLayout(vbox)

    def form(self):
        global name1
        #NAME
        self.hbox1 = QHBoxLayout()
        self.nameLabel = QLabel("Name: ", self)
        self.nameLabel.setStyleSheet("margin: 10px auto 10px auto")
        self.nameLineEdit = QLineEdit(self)
        self.nameLineEdit.setPlaceholderText("Enter your name")
        self.nameLineEdit.setStyleSheet("margin: 10px auto 10px 0px")
        self.hbox1.addWidget(self.nameLabel)
        self.hbox1.addWidget(self.nameLineEdit)
        self.hbox1.addStretch(1)
        # self.hbox1.addStretch(0)
        
        #ADDRESS
        self.hbox2 = QHBoxLayout()
        self.addressLabel = QLabel("Address: ", self)
        self.addressLabel.setStyleSheet("margin: 10px auto 10px auto")
        self.addressLineEdit = QLineEdit(self)
        self.addressLineEdit.setPlaceholderText("Enter your address")
        self.addressLineEdit.setStyleSheet("margin: 10px auto 10px 0px")
        self.hbox2.addWidget(self.addressLabel)
        self.hbox2.addWidget(self.addressLineEdit)
        self.hbox2.addStretch(1)
        
        #PHONE
        self.hbox3 = QHBoxLayout()
        self.phoneLabel = QLabel("Phone: ", self)
        self.phoneLabel.setStyleSheet("margin: 10px auto 10px auto")
        self.phoneLineEdit = QLineEdit(self)
        self.phoneLineEdit.setValidator(QIntValidator())
        self.phoneLineEdit.setMaxLength(10)
        self.phoneLineEdit.setPlaceholderText("Enter your phone")
        self.phoneLineEdit.setStyleSheet("margin: 10px auto 10px 0px")
        self.hbox3.addWidget(self.phoneLabel)
        self.hbox3.addWidget(self.phoneLineEdit)
        self.hbox3.addStretch(1)

        #EMAIL ID
        self.hbox4 = QHBoxLayout()
        self.emailLabel = QLabel("Email: ", self)
        self.emailLabel.setStyleSheet("margin: 10px auto 10px auto")
        self.emailLineEdit = QLineEdit(self)
        self.emailLineEdit.setPlaceholderText("Enter your email")
        self.emailLineEdit.setStyleSheet("margin: 10px auto 10px 0px")
        self.hbox4.addWidget(self.emailLabel)
        self.hbox4.addWidget(self.emailLineEdit)
        self.hbox4.addStretch(1)

        #SUBMIT BTN
        self.submitBtn = QPushButton("Submit", self)
        self.submitBtn.clicked.connect(self.insert_data)

        self.ackLabel = QLabel("", self)
        # self.ackLabel.setGeometry(500,500,100,30)



    def convert_data(file_name):
        with open(file_name, 'rb') as file:
            binary_data = file.read()
        return binary_data
    
    def insert_data(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password= "root",
                database = "cinegencenda"
            )

            mycursor = mydb.cursor()

            name = self.nameLineEdit.text()
            address = self.addressLineEdit.text()
            phone = self.phoneLineEdit.text()
            email = self.emailLineEdit.text()
            now = datetime.now()
            # now = now.strftime("%Y-%M-%D %H:%M:%S")
            print(now)

            query = "INSERT INTO cinegencemedia (name, address, phone, email, pdf_file, visit) VALUES (%s,%s,%s,%s,%s,%s)"
            pdf_file = Window.convert_data('D:/Learning Python/29-7-2021/heloo.pdf')
            value = (name,address,phone,email,pdf_file, now)

            mycursor.execute(query, value)
            mydb.commit()

            self.ackLabel.setText("Data inserted successfuly")
        
        
        except mc.Error as e:
            print(e)
            self.ackLabel.setText("ERROR occured")


app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())








































































