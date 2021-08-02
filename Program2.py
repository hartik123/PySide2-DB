from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import mysql.connector as mc

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black")
        self.setWindowTitle("HS VoiceCall pvt Ltd.")
        
        self.company_name = QLabel("HS VOICE CALL")
        self.company_name.setStyleSheet("color: white; font-size: 40px")
        self.company_name.setAlignment(Qt.AlignHCenter)

        # self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        # self.widget = QWidget()                 # Widget that contains the collection of Vertical Box

        self.vbox = QVBoxLayout()

        self.retrieve_form()
        self.showData()
        # self.hideDataField()

        self.vbox.addWidget(self.company_name)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addStretch(1)
        

        self.setLayout(self.vbox)

        # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scroll.setWidgetResizable(True)
        # self.scroll.setWidget(self)

    def retrieve_form(self):
        self.hbox1 = QHBoxLayout()

        self.searchFieldLineEdit = QLineEdit(self)
        self.searchFieldLineEdit.setStyleSheet("font-size: 25px; color: white; width: 500px; height: 30px")
        self.searchFieldLineEdit.setPlaceholderText("Enter a name to fetch record")

        self.searchBtn = QPushButton("SEARCH", self)
        self.searchBtn.setStyleSheet("color: white; font-size: 20px; margin-left: 30px")
        # self.searchBtn.move(200,0)

        self.hbox1.addStretch(1)
        self.hbox1.addWidget(self.searchFieldLineEdit)
        self.hbox1.addWidget(self.searchBtn)
        self.hbox1.addStretch(1)

        self.searchBtn.clicked.connect(self.findInDatabase)
        self.searchBtn.clicked.connect(self.hideDataField)

    def showData(self):
        self.hbox2 = QHBoxLayout()
        self.idLabel = QLabel("<b>Id</b>",self)
        self.idLabel.setStyleSheet("font-size: 30px; color: white")
        self.nameLabel = QLabel("<b>Name</b>",self)
        self.nameLabel.setStyleSheet("font-size: 30px; color: white")
        self.addressLabel = QLabel("<b>Address</b>",self)
        self.addressLabel.setStyleSheet("font-size: 30px; color: white")
        self.PhoneLabel = QLabel("<b>Phone</b>",self)
        self.PhoneLabel.setStyleSheet("font-size: 30px; color: white")
        self.emailLabel = QLabel("<b>Email</b>",self)
        self.emailLabel.setStyleSheet("font-size: 30px; color: white")
        self.visitLabel = QLabel("<b>Visit</b>",self)
        self.visitLabel.setStyleSheet("font-size: 30px; color: white")
        self.pdfLabel = QLabel("Nda",self)
        self.pdfLabel.setStyleSheet("font-size: 30px; color: white")

        # self.nameLabel.move(100,100)
        self.hbox2.addWidget(self.idLabel)
        self.hbox2.addWidget(self.nameLabel)
        self.hbox2.addWidget(self.addressLabel)
        self.hbox2.addWidget(self.PhoneLabel)
        self.hbox2.addWidget(self.emailLabel)
        self.hbox2.addWidget(self.visitLabel)
        self.hbox2.addWidget(self.pdfLabel)
        # self.hbox2.addStretch(1)

    def hideDataField(self):
        connection = mc.connect(host='localhost',
                                             database='cinegencenda',
                                             user='root',
                                             password='root')

        cursor = connection.cursor()
        sql_fetch_blob_query = "SELECT id,name,address,phone,email,pdf_file,visit from cinegencemedia where name= \""+self.searchFieldLineEdit.text()+ "\""

        cursor.execute(sql_fetch_blob_query)
        self.record = cursor.fetchall()
        print("printing record")
        # row = self.record[0]

        for row in self.record:
            self.hbox3 = QHBoxLayout()
            self.idLabelField = QLabel(str(row[0]),self)
            self.nameLabelField = QLabel(row[1],self)
            self.addressLabelField = QLabel(row[2],self)
            self.PhoneLabelField = QLabel(str(row[3]),self)
            self.emailLabelField = QLabel(row[4],self)
            self.visitLabelField = QLabel(str(row[6]),self)
            self.pdfButtonField = QPushButton("Open Pdf", self)
            self.pdfButtonField.clicked.connect(self.openingPDF)

            self.idLabelField.setStyleSheet("color: white; font-size: 15px")
            self.nameLabelField.setStyleSheet("color: white; font-size: 15px")
            self.addressLabelField.setStyleSheet("color: white; font-size: 15px")
            self.PhoneLabelField.setStyleSheet("color: white; font-size: 15px")
            self.emailLabelField.setStyleSheet("color: white; font-size: 15px")
            self.visitLabelField.setStyleSheet("color: white; font-size: 15px")
            self.pdfButtonField.setStyleSheet("color: white; font-size: 15px")

            self.hbox3.addWidget(self.idLabelField)
            self.hbox3.addWidget(self.nameLabelField)
            self.hbox3.addWidget(self.addressLabelField)
            self.hbox3.addWidget(self.PhoneLabelField)
            self.hbox3.addWidget(self.emailLabelField)
            self.hbox3.addWidget(self.visitLabelField)
            self.hbox3.addWidget(self.pdfButtonField)
            # self.hbox3.addWidget(self.pdfLabelField)
            # self.hbox3.addStretch(1)

            self.vbox.addLayout(self.hbox3)
            self.vbox.addStretch(1)

        

        # self.setCentralWidget(self.scroll)


    def showDataField(self):
    
        row = self.record[0]
        self.idLabelField.setText(str(row[0]))
        self.nameLabelField.setText(row[1])
        self.addressLabelField.setText(row[2])
        self.PhoneLabelField.setText(str(row[3]))
        self.emailLabelField.setText(row[4])
        self.visitLabelField.setText(str(row[6]))
        self.pdfButtonField.setText("Open Pdf")
        # self.pdfLabel.setText(row[5])


    def openingPDF(self):
        # row = self.record[0]
        import subprocess
        path= "D:/Learning Python/29-7-2021/EmployeesNda/"+"tatsat"+".pdf"
        subprocess.Popen([path], shell=True)




    def write_file(self, data, filename):
    # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)


    def findInDatabase(self):
        
        try:
            connection = mc.connect(host='localhost',
                                             database='cinegencenda',
                                             user='root',
                                             password='root')

            cursor = connection.cursor()
            sql_fetch_blob_query = "SELECT id,name,address,phone,email,pdf_file,visit from cinegencemedia where name= \""+self.searchFieldLineEdit.text()+ "\""

            cursor.execute(sql_fetch_blob_query)
            self.record = cursor.fetchall()
            for row in self.record:
                print("Id = ", row[0])
                print("Name = ", row[1])
                file = row[5]
                bioData ="D:/Learning Python/29-7-2021/EmployeesNda/"+row[1]+".pdf"
                print("Storing employee image and bio-data on disk /n")
                self.write_file(file, bioData)

        except mc.Error as error:
            print("Failed to read BLOB data from MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


            
app = QApplication(sys.argv)
win = Window()
win.showMaximized()
sys.exit(app.exec_())