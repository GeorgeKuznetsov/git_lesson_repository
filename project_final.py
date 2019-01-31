import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


#Наше окно(без функционала), созданное в PyQt Designer, скачанное в отдельный файл
#Но в конце, при окончании основной программы перенесеное в файл с кодом функционала
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(461*2, 382*2)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(20)
        font.setItalic(True)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_to_winner = QtWidgets.QLabel(self.centralwidget)
        self.text_to_winner.setGeometry(QtCore.QRect(0, 0, 301*2, 31*2))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.text_to_winner.setFont(font)
        self.text_to_winner.setObjectName("text_to_winner")
        self.btn_try_again = QtWidgets.QPushButton(self.centralwidget)
        self.btn_try_again.setGeometry(QtCore.QRect(310*2, 337*2, 141*2, 24*2))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        font.setItalic(True)
        self.btn_try_again.setFont(font)
        self.btn_try_again.setObjectName("btn_try_again")
        self.btn_playerfight = QtWidgets.QPushButton(self.centralwidget)
        self.btn_playerfight.setGeometry(QtCore.QRect(0, 330*2, 121*2, 31*2))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        font.setItalic(True)
        self.btn_playerfight.setFont(font)
        self.btn_playerfight.setObjectName("btn_playerfight")
        self.btn_compfight = QtWidgets.QPushButton(self.centralwidget)
        self.btn_compfight.setGeometry(QtCore.QRect(130*2, 330*2, 171*2, 31*2))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        font.setItalic(True)
        self.btn_compfight.setFont(font)
        self.btn_compfight.setObjectName("btn_compfight")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310*2, 28*2, 131*2, 20*2))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_playernum = QtWidgets.QLabel(self.centralwidget)
        self.label_playernum.setGeometry(QtCore.QRect(314*2, 5*2, 131*2, 20*2))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        font.setItalic(True)
        self.label_playernum.setFont(font)
        self.label_playernum.setObjectName("label_playernum")
        self.nameinput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameinput.setGeometry(QtCore.QRect(310*2, 50*2, 141*2, 21*2))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nameinput.setFont(font)
        self.nameinput.setAcceptDrops(False)
        self.nameinput.setText("")
        self.nameinput.setDragEnabled(True)
        self.nameinput.setClearButtonEnabled(False)
        self.nameinput.setObjectName("nameinput")
        self.choicetext = QtWidgets.QTextEdit(self.centralwidget)
        self.choicetext.setGeometry(QtCore.QRect(309*2, 116*2, 144*2, 55*2))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.choicetext.setFont(font)
        self.choicetext.setUndoRedoEnabled(False)
        self.choicetext.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.choicetext.setReadOnly(True)
        self.choicetext.setAcceptRichText(False)
        self.choicetext.setObjectName("choicetext")
        self.btn_stupidgame = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stupidgame.setGeometry(QtCore.QRect(310*2, 178*2, 141*2, 25*2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_stupidgame.setFont(font)
        self.btn_stupidgame.setObjectName("btn_stupidgame")
        self.btn_easygame = QtWidgets.QPushButton(self.centralwidget)
        self.btn_easygame.setGeometry(QtCore.QRect(310*2, 210*2, 141*2, 25*2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_easygame.setFont(font)
        self.btn_easygame.setObjectName("btn_easygame")
        self.btn_unrealgame = QtWidgets.QPushButton(self.centralwidget)
        self.btn_unrealgame.setGeometry(QtCore.QRect(310*2, 306*2, 141*2, 25*2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_unrealgame.setFont(font)
        self.btn_unrealgame.setObjectName("btn_unrealgame")
        self.btn_hardgame = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hardgame.setGeometry(QtCore.QRect(310*2, 274*2, 141*2, 25*2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_hardgame.setFont(font)
        self.btn_hardgame.setObjectName("btn_hardgame")
        self.btn_normalgame = QtWidgets.QPushButton(self.centralwidget)
        self.btn_normalgame.setGeometry(QtCore.QRect(310*2, 242*2, 141*2, 25*2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_normalgame.setFont(font)
        self.btn_normalgame.setObjectName("btn_normalgame")
        self.btn_00 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_00.setGeometry(QtCore.QRect(0, 30*2, 101*2, 101*2))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_00.setFont(font)
        self.btn_00.setText("")
        self.btn_00.setObjectName("btn_00")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btn_00)
        self.btn_accept = QtWidgets.QPushButton(self.centralwidget)
        self.btn_accept.setGeometry(QtCore.QRect(310*2, 80*2, 141*2, 31*2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_accept.setFont(font)
        self.btn_accept.setObjectName("btn_accept")
        self.btn_01 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_01.setGeometry(QtCore.QRect(0, 130*2, 101*2, 101*2))
        self.btn_01.setText("")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_01.setFont(font)
        self.btn_01.setObjectName("btn_01")
        self.buttonGroup.addButton(self.btn_01)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_01.setFont(font)
        self.btn_02 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_02.setGeometry(QtCore.QRect(0, 230*2, 101*2, 101*2))
        self.btn_02.setText("")
        self.btn_02.setObjectName("btn_02")
        self.buttonGroup.addButton(self.btn_02)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_02.setFont(font)
        self.btn_10 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_10.setGeometry(QtCore.QRect(100*2, 30*2, 101*2, 101*2))
        self.btn_10.setText("")
        self.btn_10.setObjectName("btn_10")
        self.buttonGroup.addButton(self.btn_10)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_10.setFont(font)
        self.btn_20 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_20.setGeometry(QtCore.QRect(200*2, 30*2, 101*2, 101*2))
        self.btn_20.setText("")
        self.btn_20.setObjectName("btn_20")
        self.buttonGroup.addButton(self.btn_20)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_20.setFont(font)
        self.btn_11 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_11.setGeometry(QtCore.QRect(100*2, 130*2, 101*2, 101*2))
        self.btn_11.setText("")
        self.btn_11.setObjectName("btn_11")
        self.buttonGroup.addButton(self.btn_11)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_11.setFont(font)
        self.btn_21 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_21.setGeometry(QtCore.QRect(200*2, 130*2, 101*2, 101*2))
        self.btn_21.setText("")
        self.btn_21.setObjectName("btn_21")
        self.buttonGroup.addButton(self.btn_21)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_21.setFont(font)
        self.btn_12 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_12.setGeometry(QtCore.QRect(100*2, 230*2, 101*2, 101*2))
        self.btn_12.setText("")
        self.btn_12.setObjectName("btn_12")
        self.buttonGroup.addButton(self.btn_12)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_12.setFont(font)
        self.btn_22 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_22.setGeometry(QtCore.QRect(200*2, 230*2, 101*2, 101*2))
        self.btn_22.setText("")
        self.btn_22.setObjectName("btn_22")
        self.buttonGroup.addButton(self.btn_22)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_22.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_to_winner.setText(_translate("MainWindow", "Победил"))
        self.btn_try_again.setText(_translate("MainWindow", "Начать заново"))
        self.btn_playerfight.setText(_translate("MainWindow", "Режим: 2 игрока"))
        self.btn_compfight.setText(_translate("MainWindow", "Режим: против компьютера"))
        self.label_2.setText(_translate("MainWindow", "Введите имя:"))
        self.label_playernum.setText(_translate("MainWindow", "Игрок Первый,"))
        self.choicetext.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monotype Corsiva\'; font-size:14pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Выберите уровень</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">игры компьютера</span></p></body></html>"))
        self.btn_stupidgame.setText(_translate("MainWindow", "Элементарно"))
        self.btn_easygame.setText(_translate("MainWindow", "Легко"))
        self.btn_hardgame.setText(_translate("MainWindow", "Сложно"))
        self.btn_normalgame.setText(_translate("MainWindow", "Нормально"))
        self.btn_unrealgame.setText('Невозможно')
        self.btn_accept.setText(_translate("MainWindow", "Подтвердить"))

 
# функционирующее окно, унаследованное от чисто декоративного
class MyWidget(QMainWindow,Ui_MainWindow):
    def __init__(self):
        #введём начальные значения и привяжем кнопки к функциям
        super().__init__()
        self.setupUi(self)
        #атрибут "кто ходит первым в новой игре: Х или О"
        self.first = 'X'
        #атрибут "чей ход в этой партии" - нужен только для режима: "2 игрока"
        self.step = 'X'
        #атрибут "стоит ли продолжать партию или она закончена
        self.continue_game = True
        #атрибут, указывающий на режим: "2 игорка"
        self.duel = False
        #словарь-атрибут, указывающий кто ходит за крестик, а кто за нолик(при инициализации пока никто)
        self.players = {'X':'', 'O':''}
        #запасной словарь, помогающий не потерять имена игорков режима:"2 игрока"
        self.prev = {}
        self.against_comp = False
        #атрибут, настраивающий уровень игры компьютера
        self.comp_level = None
        #атрибут, указывающий имя последнего игрока, игравшего против компьютера
        self.player = ''
        #создаём поле для игры с удобной(координатной) ориентацией по клеткам
        box1 = [self.btn_00, self.btn_01, self.btn_02]
        box2 = [self.btn_10, self.btn_11, self.btn_12]
        box3 = [self.btn_20, self.btn_21, self.btn_22]
        self.box = [box1, box2, box3]
        #соединяем кнопку "начать заново" и её функцию
        self.btn_try_again.clicked.connect(self.try_again)
        #привяжем все кнопки игорвого поля к одной функции
        for i in self.box:
            for j in i:
                j.clicked.connect(self.make_a_move)
        #соединяем кнопки режимов игры: "2 игрока" и "против компьютера" с функциями
        self.btn_playerfight.clicked.connect(self.duel_game)
        self.btn_compfight.clicked.connect(self.computer_game)
        self.btn_accept.clicked.connect(self.greet)
        #наделим функионалом кнопки уровня игры компьютера
        self.btn_stupidgame.clicked.connect(self.get_level)
        self.btn_easygame.clicked.connect(self.get_level)
        self.btn_hardgame.clicked.connect(self.get_level)
        self.btn_normalgame.clicked.connect(self.get_level)
        self.btn_unrealgame.clicked.connect(self.get_level)
        #заранее заблокируем игровое поле и спрячем лишние кнопки
        self.block()
        self.hide_all()
    def try_again(self):
        #функция начать с начала
        #меняем очередность хода Х и О
        if self.first == 'X':
            self.first = 'O'
        else:
            self.first = 'X'
        #пусть первым ходит тот, кто и должен
        self.step = self.first
        #очистим поле и разблокируем его клетки
        self.clean()
        #вернём в дефолтное значение:
        #уровень игры компьютера
        self.comp_level = None
        #разрешение на продолжение партии
        self.continue_game = True
        #спрячем теперь лишние кнопки
        self.hide_all()
        #заблокируем игровое поле
        self.block()
        #оставим лишь кнопки режимов игры
        self.btn_compfight.setVisible(True)
        self.btn_playerfight.setVisible(True)
        self.btn_compfight.setEnabled(True)
        self.btn_playerfight.setEnabled(True)
        
    def block(self):
        #функция блокирования поля
        for i in range(3):
            for j in range(3):
                self.box[i][j].setDisabled(True)
    def clean(self):
        #функция очистки игрового поля и результата партии
        #и разблокирования клеток поля
        for i in range(3):
            for j in range(3):
                self.box[i][j].setText('')
                self.box[i][j].setEnabled(True)
        self.text_to_winner.setVisible(False)

    def hide_all(self):
        #функция: "спрятать и заблокировать все кнопки, кроме игорвого поля
        self.text_to_winner.setVisible(False)
        self.btn_stupidgame.setVisible(False)
        self.btn_easygame.setVisible(False)
        self.btn_hardgame.setVisible(False)
        self.btn_normalgame.setVisible(False)
        self.btn_accept.setVisible(False)
        self.label_2.setVisible(False)
        self.label_playernum.setVisible(False)
        self.choicetext.setVisible(False)
        self.btn_stupidgame.setDisabled(True)
        self.btn_easygame.setDisabled(True)
        self.btn_hardgame.setDisabled(True)
        self.btn_normalgame.setDisabled(True)
        self.btn_accept.setDisabled(True)
        self.btn_try_again.setDisabled(True)
        self.btn_try_again.setVisible(False)
        self.nameinput.setDisabled(True)
        self.nameinput.setVisible(False)
        self.btn_unrealgame.setDisabled(True)
        self.btn_unrealgame.setVisible(False)
        
    
    def check_out(self):
        #функция: "проверим не победил ли кто-нибудь или, может, уже ничья"
        #флажок: "продолжать проверку"
        flag = True
        for i in range(3):
            if self.box[i][0].text() == self.box[i][1].text() == self.box[i][2].text():
                if self.box[i][0].text() in ['X', 'O']:
                    self.text_to_winner.setText('победил(-a) ' + self.players[self.box[i][0].text()])
                    self.text_to_winner.setVisible(True)
                    self.block()
                    flag = False
                    break
            if self.box[0][i].text() == self.box[1][i].text() == self.box[2][i].text():
                if self.box[0][i].text() in ['X', 'O']:
                    self.text_to_winner.setText('победил(-a) ' + self.players[self.box[0][i].text()])
                    self.text_to_winner.setVisible(True)
                    self.block()
                    flag = False
                    break
        if flag:
            if self.box[0][0].text() == self.box[1][1].text() == self.box[2][2].text() or self.box[0][2].text() == self.box[1][1].text() == self.box[2][0].text():
                if self.box[1][1].text() in ['X', 'O']:
                    self.text_to_winner.setText('победил(-a) ' + self.players[self.box[1][1].text()])
                    self.text_to_winner.setVisible(True)
                    self.block()
                    flag = False
            else:
                free = []
                for i in self.box:
                    for j in i:
                        free.append(j.isEnabled())
                if not any(free):
                    self.text_to_winner.setText('ничья          ')
                    self.text_to_winner.setVisible(True)
                    flag = False
        #теперь укажем, надо ли нам играть дальше
        self.continue_game = flag
        #компьютер - это точно он, в отличие от игрока
        if "компьютер" in self.text_to_winner.text():
            self.text_to_winner.setText(self.text_to_winner.text().replace('(-a)', ''))
                                         
    def make_a_move(self):
        #функция деланья хода для разных режимов
        if self.duel is True:
            #тут всё просто: фиксируем ход игрока и меняем очерёдность хода
            active = self.sender()
            active.setText(self.step)
            if self.step == "X":
                self.step = 'O'
            else:
                self.step = 'X'
            active.setDisabled(True)
            self.check_out()
        elif self.against_comp is True:
            #а здесь подключим искуственный интеллект
            active = self.sender()
            active.setText('X')
            active.setDisabled(True)
            self.check_out()
            if self.continue_game:
                #пусть ИИ действует только, когда можно
                self.comp_choice(self.comp_level)
                self.check_out()
            
    def duel_game(self):
        #сделаем всё как полагается для данного режима и отключим другой
        #выдадим ввод имени игрока
        self.nameinput.setEnabled(True)
        self.nameinput.setVisible(True)      
        self.duel = True
        #позволим его подтверждать
        self.btn_accept.setVisible(True)
        #подскажем, кому и что делать
        #(ввести имя)
        self.label_2.setVisible(True)
        self.label_playernum.setVisible(True)
        #(какому игроку вводить)
        self.label_playernum.setText('Игрок Первый(X),')
        self.btn_accept.setEnabled(True)
        self.btn_try_again.setEnabled(True)
        self.btn_try_again.setVisible(True)
        self.text_to_winner.setVisible(True)
        self.text_to_winner.setText('Первый ходит ' + self.step)
        #кнопки режимов уберём
        self.btn_compfight.setVisible(False)
        self.btn_playerfight.setVisible(False)
        self.btn_compfight.setDisabled(True)
        self.btn_playerfight.setDisabled(True)
        if self.against_comp is True:
            #если надо, то вспомним имена последних игроков
            self.players = self.prev.copy()
            if self.players == {}:
                self.players = {'X':'', 'O':''}
            self.prev = {}
            self.against_comp = False
        #позволим игроку не перезаписывать то же самое имя
        self.nameinput.setText(self.players['X'])

    def greet(self):
        #функция "приветствия" с игроком
        if self.duel is True:
            #попросим игроков ввести имя, любое кроме "компьютер"(оно всегда остаётся за компьютером)
            if 'Первый' in self.label_playernum.text() and self.nameinput.text() != 'компьютер':
                self.label_playernum.setText('Игрок Второй(O),')
                self.players['X'] = self.nameinput.text()
                if self.nameinput.text() == '':
                    #если первый игрок не хочет вводить имя, то пусть будет просто "Игрок Первый"
                    self.players['X'] = 'Игрок Первый'
                self.nameinput.setText(self.players['O'])
            elif self.nameinput.text() != self.players['X'] and self.nameinput.text() != 'компьютер':
                #имена должны быть разными!
                self.players['O'] = self.nameinput.text()
                if self.nameinput.text() == '':
                    #если второй игрок не хочет вводить имя, то пусть будет просто "Игрок Второй"
                    self.players['O'] = 'Игрок Второй'
                self.hide_all()
                #уберём все лишние кнопки, и да начнётся игра(может быть заново без единого хода игрока)
                self.btn_try_again.setEnabled(True)
                self.btn_try_again.setVisible(True)
                self.nameinput.setText(self.players['X'])
                self.clean()
        elif self.against_comp is True and self.nameinput.text() != 'компьютер':
            #Попросим игрока ввести имя
            self.players['X'] = self.nameinput.text()
            if self.nameinput.text() == '':
                #если игрок не хочет вводить имя, то пусть будет просто "Игрок"
                self.players['X'] = 'Игрок'
            self.player = self.players['X']
            #компьютер - он и есть "компьютер"
            self.players['O'] = 'компьютер'
            #спрячем уже не нужные кнопки
            self.hide_all()
            #заранее дадим пользователю возможность начать заново
            self.btn_try_again.setEnabled(True)
            self.btn_try_again.setVisible(True)
            #перед игрой спросим желаемый уровень игры компьютера
            self.btn_stupidgame.setVisible(True)
            self.btn_easygame.setVisible(True)
            self.btn_hardgame.setVisible(True)
            self.btn_normalgame.setVisible(True)
            self.choicetext.setVisible(True)
            self.btn_stupidgame.setEnabled(True)
            self.btn_easygame.setEnabled(True)
            self.btn_hardgame.setEnabled(True)
            self.btn_normalgame.setEnabled(True)
            self.btn_unrealgame.setEnabled(True)
            self.btn_unrealgame.setVisible(True)

    def computer_game(self):
        #сделаем всё, как и полагается для данного режима и отключим другой
        if self.duel is True:
            #запомним имена игроков из режима: "2 Игрока", если надо
            self.prev = self.players.copy()
        self.players = {}
        self.against_comp = True
        self.duel = False
        #дадим игроку возможность представиться
        self.nameinput.setEnabled(True)
        self.nameinput.setVisible(True)
        self.nameinput.setText(self.player)
        self.btn_accept.setVisible(True)
        self.label_2.setVisible(True)
        self.label_playernum.setVisible(True)
        self.label_playernum.setText('Вы ходите за Х,')
        self.btn_accept.setEnabled(True)
        self.btn_try_again.setEnabled(True)
        self.btn_try_again.setVisible(True)
        self.text_to_winner.setVisible(True)
        self.text_to_winner.setText('Первый ходит ' + self.first)
        #кнопки режимов уберём
        self.btn_compfight.setVisible(False)
        self.btn_playerfight.setVisible(False)
        self.btn_compfight.setDisabled(True)
        self.btn_playerfight.setDisabled(True)

    def get_level(self):
        #функция: "узнаем желаемый уровень игры компьютера"
        self.comp_level = self.sender().text()
        self.hide_all()
        self.btn_try_again.setEnabled(True)
        self.btn_try_again.setVisible(True)
        self.clean()
        if self.first == 'O':
            self.comp_choice(self.comp_level)
                
    def comp_choice(self, level):
        #функция делающая ход от лица компьютера на соответствующем уровне
        #пеменная chosen - это та клетка, которую выбирает компьютер для хода
        #переменная flag присутствует во всех режимах, кроме элементарного
        #она определяет необходимость продолжения работы ИИ
        #уровни "Нормально" и "Сложно" крайне похожи по коду на уровень "Невозможно"
        #и по сути являются его "испорченными" версиями
        if level == "Элементарно":
            #что может быть проще рандома?
            chosen = random.choice(self.buttonGroup.buttons())
            while not chosen.isEnabled():
                chosen = random.choice(self.buttonGroup.buttons())
        elif level == 'Легко':
            chosen = None
            #варианты выбранной клетки
            variants = []
            flag = True
            #составим все возможные ряды клеток, необходимые для победы
            #т.е ряды, при заполнение которых одинаковыми знаками следует победа их "заполнителя"
            main_box = self.box[:]
            box1 = [self.box[0][0], self.box[1][0], self.box[2][0]]
            box2 = [self.box[0][1], self.box[1][1], self.box[2][1]]
            box3 = [self.box[0][2], self.box[1][2], self.box[2][2]]
            box4 = [self.box[0][0], self.box[1][1], self.box[2][2]]
            box5 = [self.box[0][2], self.box[1][1], self.box[2][0]]
            main_box.extend((box1, box2, box3, box4, box5))
            #проверим, не может ли выиграть компьютер
            for i in main_box:
                if flag:
                    look = [j.text() for j in i]
                    if look.count('O') == 2 and look.count('') == 1:
                        #если может, пусть победит
                        chosen = i[look.index('')]
                        flag = False
            #но прежде всего проверим, не может ли игрок выиграть
            for i in main_box:
                    look = [j.text() for j in i]
                    if look.count('X') == 2 and look.count('') == 1:
                        #если может, пусть компьютер помешает(при случае вместо того, чтобы победить)
                        variants.append(i[look.index('')])
                        flag = False
            if chosen in variants:
                #поскольку компьютер должен играть легко, то он должен сделать глупость
                #а именно не выиграть, не давая сделать победный(или один из) ход
                variants.remove(chosen)
            if variants:
                chosen = random.choice(variants)
            #просканируем, где компьютер может попытаться выиграть
            for i in main_box:
                if flag:
                    #для удобства узнаем значения на кнопках ряда
                    look = [j.text() for j in i]
                    if look.count('O') == 1 and look.count('') == 2:
                        chosen = i[look.index('')]
                        flag = False
            if flag:
                #если же у нас ничего не выходит с проверками, то используем рандом
                chosen = random.choice(self.buttonGroup.buttons())
                while not chosen.isEnabled():
                    chosen = random.choice(self.buttonGroup.buttons())
        elif level == 'Нормально':
            flag = True
            variants = []
            main_box = self.box[:]
            box1 = [self.box[0][0], self.box[1][0], self.box[2][0]]
            box2 = [self.box[0][1], self.box[1][1], self.box[2][1]]
            box3 = [self.box[0][2], self.box[1][2], self.box[2][2]]
            box4 = [self.box[0][0], self.box[1][1], self.box[2][2]]
            box5 = [self.box[0][2], self.box[1][1], self.box[2][0]]
            main_box.extend((box1, box2, box3, box4, box5))
            if random.choice((True, False)):
                for i in main_box:
                    look = [j.text() for j in i]
                    if look.count('X') == 2 and look.count('') == 1:
                        variants.append(i[look.index('')])
                        flag = False
            if variants:
                chosen = random.choice(variants)
            if flag:
                for i in main_box:
                    if flag:
                        look = [j.text() for j in i]
                        if look.count('O') == 2 and look.count('') == 1:
                            chosen = i[look.index('')]
                            flag = False
                if flag:
                    for i in main_box:
                        look = [j.text() for j in i]
                        if look.count('X') == 2 and look.count('') == 1:
                            variants.append(i[look.index('')])
                            flag = False
                    if variants:
                        chosen = random.choice(variants)
                    if flag:
                        free = []
                        main_box = [self.box[0][0], self.box[0][2], self.box[2][0], self.box[2][2], self.box[1][1]]
                        for j in main_box:
                            free.append(j.isEnabled())
                        if any(free):
                            chosen = random.choice(main_box)
                            while not chosen.isEnabled():
                                chosen = random.choice(main_box)
                        else:
                            chosen = random.choice(self.buttonGroup.buttons())
                            while not chosen.isEnabled():
                                chosen = random.choice(self.buttonGroup.buttons())
        elif level == 'Сложно':
            flag = True
            main_box = self.box[:]
            box1 = [self.box[0][0], self.box[1][0], self.box[2][0]]
            box2 = [self.box[0][1], self.box[1][1], self.box[2][1]]
            box3 = [self.box[0][2], self.box[1][2], self.box[2][2]]
            box4 = [self.box[0][0], self.box[1][1], self.box[2][2]]
            box5 = [self.box[0][2], self.box[1][1], self.box[2][0]]
            main_box.extend((box1, box2, box3, box4, box5))
            for i in main_box:
                if flag:
                    look = [j.text() for j in i]
                    if look.count('O') == 2 and look.count('') == 1:
                        chosen = i[look.index('')]
                        flag = False
            if flag:
                for i in main_box:
                    if flag:
                        look = [j.text() for j in i]
                        if look.count('X') == 2 and look.count('') == 1:
                            chosen = i[look.index('')]
                            flag = False
                if flag:
                    free = []
                    main_box = [self.box[0][0], self.box[0][2], self.box[2][0], self.box[2][2]]
                    look = [j.text() for j in main_box]
                    main_look = [i.text() for i in self.buttonGroup.buttons()]
                    if random.choice((True, False)) and not self.box[1][1].isEnabled():
                        if look.count('X') == main_look.count('X') == 2 and self.box[1][1].text() == 'O':
                            chosen = random.choice((box1[1], box2[0], box2[2], box3[1]))
                    for y in main_box:
                        free.append(y.isEnabled())
                    if self.box[1][1].isEnabled():
                        chosen = self.box[1][1]
                    elif main_look.count('X') == 2 and self.box[1][1].text() == 'O' and look.count('X') == 1:
                        chosen = random.choice(main_box)
                        while chosen in (main_box[-look.index('X')-1], main_box[look.index('X')]):
                            chosen = random.choice(main_box)
                    elif any(free) and not self.box[1][1].isEnabled():
                        chosen = random.choice(main_box)
                        while not chosen.isEnabled():
                            chosen = random.choice(main_box)
                    elif not any(free) and not self.box[1][1].isEnabled():
                        chosen = random.choice(self.buttonGroup.buttons())
                        while not chosen.isEnabled():
                            chosen = random.choice(self.buttonGroup.buttons())
        elif level == 'Невозможно':
            #составим все возможные ряды клеток, необходимые для победы
            #т.е ряды, при заполнение которых одинаковыми знаками следует победа их "заполнителя"
            flag = True
            main_box = self.box[:]
            box1 = [self.box[0][0], self.box[1][0], self.box[2][0]]
            box2 = [self.box[0][1], self.box[1][1], self.box[2][1]]
            box3 = [self.box[0][2], self.box[1][2], self.box[2][2]]
            box4 = [self.box[0][0], self.box[1][1], self.box[2][2]]
            box5 = [self.box[0][2], self.box[1][1], self.box[2][0]]
            main_box.extend((box1, box2, box3, box4, box5))
            #прежде всего проверим, не может ли победить компьютер
            for i in main_box:
                if flag:
                    #упростим задачу, узнав тексты на кнопках ряда
                    look = [j.text() for j in i]
                    if look.count('O') == 2 and look.count('') == 1:
                        #если может, пусть победит
                        chosen = i[look.index('')]
                        flag = False
            if flag:
                #и только после этого, провери не может ли победить игрок 
                for i in main_box:
                    if flag:
                        look = [j.text() for j in i]
                        if look.count('X') == 2 and look.count('') == 1:
                            #если может, пусть компьютер помешает
                            chosen = i[look.index('')]
                            flag = False
                if flag:
                    free = []
                    main_box = [self.box[0][0], self.box[0][2], self.box[2][0], self.box[2][2]]
                    #просмотрим текстурки углов поля
                    look = [j.text() for j in main_box]
                    #и текстурки всего поля
                    main_look = [i.text() for i in self.buttonGroup.buttons()]
                    for y in main_box:
                        #проанализируем, какие углы поля свободны
                        free.append(y.isEnabled())
                    if self.box[1][1].isEnabled():
                        #ключевая позиция поля - серединка, если можно, то пусть компьютер захватит её
                        chosen = self.box[1][1]
                    elif look.count('X') == main_look.count('X') == 2 and self.box[1][1].text() == 'O':
                        #есть одна вилка против любителей ставить в углы и середину:
                        #если вы ходите первым, ставите крестик в угол, а противник ставит в ответ нолик
                        #в середину, то поставьте второй крестик в противоположный угол, и если противник
                        #поставит свой нолик в угол, то поставьте крестик в оставшийся угол.
                        #Но есть и выход из неё:просто не ставить знак в угол, так поможем компьютеру
                        chosen = random.choice((box1[1], box2[0], box2[2], box3[1]))
                    elif main_look.count('X') == 2 and self.box[1][1].text() == 'O' and look.count('X') == 1:
                        #есть и другая вилка против тех же товарищей, но менее удачная:
                        #если вы ходите первым, ставите крестик в угол, а противник ставит в ответ нолик
                        #в середину, то поставьте второй крестик в боковую клетку, и если противник
                        #поставит свой нолик в угол(не соседний с клеткой второго крестика),
                        #то поставьте крестик в угол, противоположный углу, выбранному противником.
                        #Но и от неё надо гарантированно уберечь компьютер(он же непопедим у нас)
                        chosen = main_box[-look.index('X')-1]
                    elif any(free) and not self.box[1][1].isEnabled():
                        #другие ключевые позиции поля - углы, пусть компьютер не забудет и про них
                        chosen = random.choice(main_box)
                        while not chosen.isEnabled():
                            chosen = random.choice(main_box)
                    else:
                        #если более разумного хода нет, то почему бы и не порандомить?
                        chosen = random.choice(self.buttonGroup.buttons())
                        while not chosen.isEnabled():
                            chosen = random.choice(self.buttonGroup.buttons())
        
                        
                            
        #ну и конечно утвердим наш выбор на поле
        chosen.setText('O')
        chosen.setDisabled(True)
                

        
                    
        
#выводим наше окно на экран
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

