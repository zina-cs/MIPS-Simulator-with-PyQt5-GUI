import sys
from random import seed
from random import randint
from PyQt5.QtGui import  QPalette, QColor
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class window(QDialog):

    regfile = {"$zero": "0", "$v0": "0", "$v1": "0", "$a0": "0", "$a1": "0", "$a2": "0", "$a3": "0", "$t0": "0", "$t1": "0", "$t2": "0", "$t3": "0", "$t4": "0", "$t5": "0", "$t6": "0", "$t7": "0",
             "$s0": "0", "$s1": "0", "$s2": "0", "$s3": "0", "$s4": "0", "$s5": "0", "$s6": "0", "$s7": "0", "$t8": "0", "$t9": "0", "$gp": "0", "$sp": "0", "$fp": "0", "$ra": "0"}
    PC = 0

    memfile = []

    def __init__(self):
        super().__init__()

        seed(1)
        for _ in range(176):
            self.memfile.append(randint(0, 90374))

        # setting window title
        self.setWindowTitle("Python")

        # setting geometry to the window
        self.setGeometry(100, 100, 300, 400)

        # creating a group box
        self.formGroupBox = QGroupBox("MIPS Simulator: Enter Instruction")

        # creating spin box to select age
        self.regfSpinBar = QSpinBox()
        self.regsSpinBar = QSpinBox()
        self.regdSpinBar = QSpinBox()

        self.regfSpinBar.setMaximum(65535)
        self.regsSpinBar.setMaximum(65535)
        self.regdSpinBar.setMaximum(65535)

        # creating combo box to select degree
        self.regf = QComboBox()

        self.textbox = QLineEdit()

        self.textbox1 = QLineEdit()

        self.textbox2 = QLineEdit()

        # adding items to the combo box
        self.regf.addItems(["$zero", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7", "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7", "$t8", "$t9", "$gp", "$sp", "$fp", "$ra"])
        self.regs = QComboBox()

        # adding items to the combo box
        self.regs.addItems(
            ["$zero", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7",
             "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7", "$t8", "$t9", "$gp", "$sp", "$fp", "$ra"])

        self.regd = QComboBox()

        # adding items to the combo box
        self.regd.addItems(
            ["$zero", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7",
             "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7", "$t8", "$t9", "$gp", "$sp", "$fp", "$ra"])
        # creating a line edit
        self.nameLineEdit = QComboBox()
        self.nameLineEdit.addItems(["add", "addi", "lw", "sw", "sll", "and", "andi", "or", "ori", "nor", "beq", "j", "jal", "jr", "slt"])



        # creating a vertical layout
        mainLayout = QVBoxLayout()

        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)

        # adding button box to the layout
        self.layout = QFormLayout()


        self.layout.addRow(QLabel("Instruction"), self.nameLineEdit)
        # setting lay out
        self.formGroupBox.setLayout(self.layout)
        self.setLayout(mainLayout)
        self.pybutton = QPushButton('OK', self)
        self.pybutton.clicked.connect(self.clickMethod)
        self.pybutton.resize(50, 40)
        self.pybutton.move(225, 100)


        self.button = QPushButton('OK', self)
        self.button.clicked.connect(self.getInfo)
        self.button.resize(50, 40)
        self.button.move(225, 340)
        self.button.hide()

        self.ybutton = QPushButton('Next Instruction', self)
        self.ybutton.hide()


    def clickMethod(self):
        self.pybutton.hide()
        self.button.show()


        if self.nameLineEdit.currentText() == "add" or self.nameLineEdit.currentText() == "and" or self.nameLineEdit.currentText() == "or" or self.nameLineEdit.currentText() == "nor" or self.nameLineEdit.currentText() == "slt":

            self.layout.addRow(QLabel("Reg 1:"), self.regf)

            self.layout.addRow(QLabel("Value:"), self.regfSpinBar)

            self.layout.addRow(QLabel("Reg 2:"), self.regs)

            self.layout.addRow(QLabel("Value:"), self.regsSpinBar)
            self.layout.addRow(QLabel("Reg 3:"), self.regd)
        elif self.nameLineEdit.currentText() == "addi" or self.nameLineEdit.currentText() == "andi" or self.nameLineEdit.currentText() == "ori" or self.nameLineEdit.currentText() == "sll":

            self.layout.addRow(QLabel("Reg 1:"), self.regf)


            self.layout.addRow(QLabel("Reg 2:"), self.regs)

            self.layout.addRow(QLabel("Value:"), self.regsSpinBar)
            self.layout.addRow(QLabel("Immediate(offset):"), self.regdSpinBar)
        elif self.nameLineEdit.currentText() == "lw" or self.nameLineEdit.currentText() == "beq" or self.nameLineEdit.currentText() == "sw":
            self.layout.addRow(QLabel("Reg 1:"), self.regf)

            self.layout.addRow(QLabel("Value:"), self.regfSpinBar)

            self.layout.addRow(QLabel("Reg 2:"), self.regs)

            self.layout.addRow(QLabel("Value:"), self.regsSpinBar)
            self.layout.addRow(QLabel("Immediate(offset):"), self.regdSpinBar)
        elif self.nameLineEdit.currentText() == "jr":
            self.layout.addRow(QLabel("Reg:"), self.regf)

            self.layout.addRow(QLabel("Value:"), self.regfSpinBar)
        else:
            self.layout.addRow(QLabel("Address:"), self.regfSpinBar)


    def getInfo(self):
        self.formGroupBox.setTitle("MIPS Simulator: Double Click to view information")
        self.button.hide()
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)
        self.lines = Control()
        if self.nameLineEdit.currentText() == "add":
            self.PC += 4
            self.lines.r("add")
            reg1 = int(self.regfSpinBar.text())
            reg2 = int(self.regsSpinBar.text())
            self.regfile[self.regd.currentText()] = bin(reg1 + reg2)
            self.regfile[self.regf.currentText()] = bin(reg1)
            self.regfile[self.regs.currentText()] = bin(reg2)
        elif self.nameLineEdit.currentText() == "beq":
            self.PC += 4
            self.lines.b()
            reg1 = int(self.regfSpinBar.text())
            reg2 = int(self.regsSpinBar.text())
            if (reg1-reg2) == 0:
                self.PC = self.PC + int(self.regdSpinBar.text())

        elif self.nameLineEdit.currentText() == "addi":
            self.PC += 4
            self.lines.i("addi")
            reg1 = int(self.regsSpinBar.text())
            im = int(self.regdSpinBar.text())
            self.regfile[self.regf.currentText()] = bin(reg1 + im)
            self.regfile[self.regs.currentText()] = bin(reg1)
            # here goes i type func
        elif self.nameLineEdit.currentText() == "slt":
            self.PC += 4
            self.lines.r("slt")
            reg1 = int(self.regfSpinBar.text())
            reg2 = int(self.regsSpinBar.text())
            if reg1 < reg2:
                self.regfile[self.regd.currentText()] = bin(1)
            else:
                self.regfile[self.regd.currentText()] = bin(0)
        elif self.nameLineEdit.currentText() == "and":
            self.lines.rtype()
            self.PC += 4
            reg1 = (int(self.regfSpinBar.text()))
            reg2 = (int(self.regsSpinBar.text()))
            self.regfile[self.regd.currentText()] = bin(reg1 & reg2)
            self.regfile[self.regf.currentText()] = bin(reg1)
            self.regfile[self.regs.currentText()] = bin(reg2)
        elif self.nameLineEdit.currentText() == "andi":
            self.PC += 4
            self.lines.i("andi")
            reg1 = int(self.regsSpinBar.text())
            im = int(self.regdSpinBar.text())
            self.regfile[self.regf.currentText()] = bin(reg1 & im)
            self.regfile[self.regs.currentText()] = bin(reg1)
        elif self.nameLineEdit.currentText() == "or":
            self.PC += 4
            self.lines.r("or")
            reg1 = (int(self.regfSpinBar.text()))
            reg2 = (int(self.regsSpinBar.text()))
            self.regfile[self.regd.currentText()] = bin(reg1 | reg2)
            self.regfile[self.regf.currentText()] = bin(reg1)
            self.regfile[self.regs.currentText()] = bin(reg2)
        elif self.nameLineEdit.currentText() == "ori":
            self.PC += 4
            self.lines.i("ori")
            reg1 = int(self.regsSpinBar.text())
            im = int(self.regdSpinBar.text())
            self.regfile[self.regf.currentText()] = bin(reg1 | im)
            self.regfile[self.regs.currentText()] = bin(reg1)
        elif self.nameLineEdit.currentText() == "nor":
            self.PC += 4
            self.lines.r("nor")
            reg1 = (int(self.regfSpinBar.text()))
            reg2 = (int(self.regsSpinBar.text()))
            self.regfile[self.regd.currentText()] = bin(~(reg1 | reg2))
            self.regfile[self.regf.currentText()] = bin(reg1)
            self.regfile[self.regs.currentText()] = bin(reg2)
        elif self.nameLineEdit.currentText() == "sll":
            self.PC += 4
            self.lines.r("sll")
            reg1 = int(self.regsSpinBar.text())
            im = int(self.regdSpinBar.text())
            self.regfile[self.regf.currentText()] = bin(reg1 << im)
            self.regfile[self.regs.currentText()] = bin(reg1)
        elif self.nameLineEdit.currentText() == "lw":
            self.PC += 4
            self.lines.i("lw")
            reg1 = int(self.regfSpinBar.text())
            reg2 = int(self.regsSpinBar.text())
            im = int(self.regdSpinBar.text())
            address = bin(reg2 + im)
            seed(1)
            placeMem = randint(0, 175)
            self.regfile[self.regf.currentText()] = self.memfile[placeMem]
            self.regfile[self.regs.currentText()] = bin(reg2)
        elif self.nameLineEdit.currentText() == "sw":
            self.PC += 4
            self.lines.i("sw")
            reg1 = int(self.regfSpinBar.text())
            reg2 = int(self.regsSpinBar.text())
            im = int(self.regdSpinBar.text())
            address = int(reg2 + im, 2)
            seed(1)
            placeMem = randint(0, 175)
            self.memfile[placeMem] = reg1
            self.regfile[self.regf.currentText()] = bin(reg1)
        elif self.nameLineEdit.currentText() == "j":
            self.PC += 4
            self.lines.j()
            address = int(self.regfSpinBar.text())
            address <<= 2
            address = bin(address)
            nPC = "0000"
            for i in range(26 - len(address)):
                    nPC += "0"
            for i in range(len(address)-2):
                    nPC += address[i+2]
            self.PC = int(nPC, 2)
        elif self.nameLineEdit.currentText() == "jal":
            self.lines.j()
            address = int(self.regfSpinBar.text())
            address <<= 2
            address = str(address)
            self.regfile[len(self.regfile) - 1] = self.PC
            nPC = "0000"
            for i in range(26 - len(address)):
                nPC += "0"
            for i in range(len(address) - 2):
                nPC += address[i + 2]
            self.PC = int(nPC, 2)
        elif self.nameLineEdit.currentText() == "jr":
            self.lines.j()
            self.PC = self.regfile[len(self.regfile) - 1]


        self.layout.addRow(QLabel("Pick Register:"), self.regf)

        self.line = QComboBox()
        self.line.addItems(
            ["RegDst", "JToPC", "Branch", "MemRead", "MemToReg", "ALUOp", "MemWrite", "ALUSrc", "RegWrite", "Funct",
             "ALUControl", "ReadShamt", "JumpR"])
        self.regf.view().pressed.connect(self.regvalue)
        self.layout.addRow(QLabel("Value:"), self.textbox)
        self.layout.addRow(QLabel("Pick Line to View Value:"), self.line)
        self.layout.addRow(QLabel("Value:"), self.textbox1)
        self.line.view().pressed.connect(self.linevalue)
        self.layout.addRow(QLabel("Current PC value:"), self.textbox2)
        self.textbox2.setText(str(self.PC))
        self.ybutton.show()
        self.ybutton.clicked.connect(self.repeat)
        self.ybutton.resize(130, 40)
        self.ybutton.move(205, 245)

    def regvalue(self):
        self.textbox.setText(self.regfile[self.regf.currentText()])

    def linevalue(self):
        x = self.line.currentText()
        x.replace("'", "")
        self.textbox1.setText(str(getattr(self.lines, x)))
    def repeat(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)
        self.layout.addRow(QLabel("Instruction"), self.nameLineEdit)
        self.pybutton.show()
        self.ybutton.hide()





class Control:
    RegDst = "0"
    RegWrite = "0"
    ALUSrc = "0"
    ALUOp = "000"
    MemWrite = "0"
    MemRead = "0"
    MemToReg = "0"
    JToPC = "0"
    Branch = "0"
    ReadShamt = "00000"
    JumpR = "0"
    Funct = "0"
    ALUControl = "0"

    def __init__(self):
        self.RegDst = "0"
        self.RegWrite = "0"
        self.ALUSrc = "0"
        self.ALUOp = "000"
        self.MemWrite = "0"
        self.MemRead = "0"
        self.MemToReg = "0"
        self.JToPC = "0"
        self.Branch = "0"
        self.JumpR = "0"
        self.ReadShamt = "0"
        self.Funct = "XXXXXX"
        self.ALUControl = "XXXX"


    def b(self):
        self.RegDst = "X"
        self.RegWrite = "0"
        self.ALUSrc = "0"
        self.ALUOp = "110"
        self.MemWrite = "0"
        self.MemRead = "0"
        self.MemToReg = "X"
        self.JToPC = "0"
        self.Branch = "1"
        self.ALUControl = "0110"

    def j(self):
        self.RegDst = "X"
        self.RegWrite = 0
        self.ALUSrc = "X"
        self.ALUOp = "X"
        self.MemWrite = 0
        self.MemRead = 0
        self.MemToReg = "X"
        self.JToPC = 1
        self.Branch = 0

    def jal(self):
        self.j()
        self.RegDst = "10"
        self.MemToReg = "10"
        self.RegWrite = 1

    def jr(self):
        self.RegDst = "X"
        self.MemToReg = "X"
        self.ALUOp = "X"
        self.ALUSrc = "X"
        self.JumpR = 1

    def rtype(self):
        self.RegDst = 1
        self.RegWrite = 1
        self.ALUSrc = 0
        self.MemWrite = 0
        self.MemRead = 0
        self.MemToReg = 0
        self.JToPC = 0
        self.Branch = 0

    def r(self, rInstruction):
        self.rtype()

        if rInstruction == "add":
            self.ALUOp = "010"
            self.Funct = "100000"
            self.ALUControl = "0010"
        elif rInstruction == "or":
            self.ALUOp = "001"
            self.Funct = "100101"
            self.ALUControl = "0001"
        elif rInstruction == "slt":
            self.ALUOp = "111"
            self.Funct = "101010"
            self.ALUControl = "0111"
        elif rInstruction == "nor":
            self.ALUOp = "010"
            self.Funct = "100111"
            self.ALUControl = "1100"
        elif rInstruction == "sll":
            self.ALUOp = "010"
            self.ReadShamt = 1
            self.Funct = "000000"
            self.ALUControl = "0100"

    def i(self, iInstruction):
        if iInstruction == "addi":
            self.ALUOp = "100"
            self.ALUSrc = 1
            self.RegWrite = 1
            self.ALUControl = "0010"
        elif iInstruction == "lw":
            self.MemRead = 1
            self.MemToReg = "01"
            self.ALUSrc = 1
            self.RegWrite = 1
            self.ALUControl = "0010"
        elif iInstruction == "sw":
            self.RegDst = "X"
            self.MemToReg = "X"
            self.MemWrite = 1
            self.ALUSrc = 1
            self.ALUControl = "0010"
        elif iInstruction == "andi":
            self.ALUOp = "100"
            self.ALUSrc = 1
            self.RegWrite = 1
            self.ALUControl = "0000"
        elif iInstruction == "ori":
            self.ALUOp = "100"
            self.ALUSrc = 1
            self.RegWrite = 1
            self.ALUControl = "0001"


def Start():
    m = window()
    m.show()
    return m
if __name__ == '__main__':
    app = QApplication([])
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    mainWin = Start()
    sys.exit(app.exec_())
