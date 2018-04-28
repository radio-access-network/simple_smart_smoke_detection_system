import sys, time, urllib.request, urllib.error

from PyQt5 import QtWidgets, QtGui, QtCore
from smoke_detector_ui import Ui_MainWindow
from set_ip_dialog import Ui_Dialog


class Check_Detector_IPs(QtCore.QThread):

    alarmsignal = QtCore.pyqtSignal(str)
    notconsignal = QtCore.pyqtSignal(str)
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.running = False
        self._ips = ["","",""]
        
    def set_ips(self, xx):
        self._ips = xx
        print(xx)
        
    def run(self):
        while self.running:
            # melder 1
            try:
                req_melder1 = urllib.request.Request(self._ips[0])
                res_melder1 = urllib.request.urlopen(req_melder1, timeout = 5).read()
                
            except urllib.error.URLError as err:
                self.notconsignal.emit("d1")
            else:
                tmp_str = res_melder1.decode(encoding = "utf-8").split(" ")
                #print(tmp_str)
                is_alert = tmp_str[2]
                if is_alert == "alarm":
                    self.alarmsignal.emit("m1")
                else:
                    self.notconsignal.emit("c1 " + tmp_str[4])
                time.sleep(20)
                
            # melder 2
            try:
                req_melder2 = urllib.request.Request(self._ips[1])
                res_melder2 = urllib.request.urlopen(req_melder2, timeout = 5).read()
                
            except urllib.error.URLError as err:
                self.notconsignal.emit("d2")
            else:
                tmp_str = res_melder2.decode(encoding = "utf-8").split(" ")
                #print(tmp_str)
                is_alert = tmp_str[2]
                if is_alert == "alarm":
                    self.alarmsignal.emit("m2")
                else:
                    self.notconsignal.emit("c2 " + tmp_str[4])
                time.sleep(20)
                
            # melder 3
            try:
                req_melder3 = urllib.request.Request(self._ips[2])
                res_melder3 = urllib.request.urlopen(req_melder3, timeout = 5).read()
            
            except urllib.error.URLError as err:
                self.notconsignal.emit("d3")
            else:
                tmp_str = res_melder3.decode(encoding = "utf-8").split(" ")
                #print(tmp_str)
                is_alert = tmp_str[2]
                if is_alert == "alarm":
                    self.alarmsignal.emit("m3")
                else:
                    self.notconsignal.emit("c3 " + tmp_str[4])
                time.sleep(20)
                
        
class IP_Picker(Ui_Dialog):

    def __init__(self,dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        
    def get_ips(self):
        return([self.ledt_buero.text(), self.ledt_werkstatt.text(), self.ledt_garage.text()])

        
class Detector_Client(Ui_MainWindow):

    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        
        
        self.ips = ["","",""]
        self.alarm_mode = False
        
        self.img_melder_on = QtGui.QPixmap("./images/melder_on.png")
        self.img_melder_off = QtGui.QPixmap("./images/melder_off.png")
        self.img_melder_dis = QtGui.QPixmap("./images/melder_disconnected.png")
        self.img_unknown = QtGui.QPixmap("./images/fragezeichen.png")
        
        self.iwidth = self.img_melder_off.size().width()
        self.iheight = self.img_melder_off.size().height()
        
        self.scene_m1 = QtWidgets.QGraphicsScene()
        self.scene_m1.addPixmap(self.img_unknown)
        self.scene_m2 = QtWidgets.QGraphicsScene()
        self.scene_m2.addPixmap(self.img_unknown)
        self.scene_m3 = QtWidgets.QGraphicsScene()
        self.scene_m3.addPixmap(self.img_unknown)
        
        self.gview_1.setScene(self.scene_m1)
        self.gview_2.setScene(self.scene_m2)
        self.gview_3.setScene(self.scene_m3)
         
        self.gview_1.setFixedHeight(self.iheight)
        self.gview_2.setFixedHeight(self.iheight)
        self.gview_3.setFixedHeight(self.iheight)
        
        self.gview_1.setFixedWidth(self.iwidth)
        self.gview_2.setFixedWidth(self.iwidth)
        self.gview_3.setFixedWidth(self.iwidth)
        
        self.actionVerbinden.triggered.connect(self.show_ip_dialog)
        self.actionBeenden.triggered.connect(self.end_it)
        self.actionInfo.triggered.connect(self.show_info)
        self.btn_stop.clicked.connect(self.stop_alarm)
        
        self.check_ip_thread = Check_Detector_IPs()
        self.check_ip_thread.alarmsignal.connect(self.alarm_handler)
        self.check_ip_thread.notconsignal.connect(self.notcon_handler)
        
    def show_info(self):
        quit_msg = "Abfrage des Status von Rauchmeldern über Ethernet\n\n Geschrieben von Andreas Fischer © 2018"
        reply = QtWidgets.QMessageBox()
        reply.setFont(QtGui.QFont("Arial",16))
        reply.setText(quit_msg)
        reply.setWindowTitle("Info!")
        reply.setDefaultButton(QtWidgets.QMessageBox.Ok)
        reply.exec()
            
    def notcon_handler(self, xx):
        signal = xx.split(" ")
        str_date = time.strftime("%d.%b. %H:%M:%S")
        if signal[0] == "d1":
            self.scene_m1.addPixmap(self.img_melder_dis)
            self.lbl_info.setStyleSheet("QLabel { background-color : yellow; color : black; }");
            self.lbl_info.setText("Keine Verbindung!: M1\n{}".format(str_date))
        if signal[0] == "d2":
            self.scene_m2.addPixmap(self.img_melder_dis)
            self.lbl_info.setStyleSheet("QLabel { background-color : yellow; color : black; }");
            self.lbl_info.setText("Keine Verbindung!: M2\n{}".format(str_date))
        if signal[0] == "d3":
            self.scene_m3.addPixmap(self.img_melder_dis)
            self.lbl_info.setStyleSheet("QLabel { background-color : yellow; color : black; }");
            self.lbl_info.setText("Keine Verbindung!: M3\n{}".format(str_date))
            
        
        if signal[0] == "c1":
            self.scene_m1.addPixmap(self.img_melder_off)
            self.lbl_info.setStyleSheet("QLabel { background-color : green; color : white; }");
            self.lbl_t1.setText(signal[1])
            self.lbl_info.setText("Alles OK!: M1\n{}".format(str_date))
        if signal[0] == "c2":
            self.scene_m2.addPixmap(self.img_melder_off)
            self.lbl_info.setStyleSheet("QLabel { background-color : green; color : white; }");
            self.lbl_t2.setText(signal[1])
            self.lbl_info.setText("Alles OK!: M2\n{}".format(str_date))
        if signal[0] == "c3":
            self.scene_m3.addPixmap(self.img_melder_off)
            self.lbl_info.setStyleSheet("QLabel { background-color : green; color : white; }");
            self.lbl_t3.setText(signal[1])            
            self.lbl_info.setText("Alles OK!: M3\n{}".format(str_date))
            
        self.lbl_info.setFont(QtGui.QFont("Arial",16))
           
    def stop_alarm(self):
        print("Alarm stoppped!")        
        #pi pin auf low setzen
        
    def alarm_handler(self, signal):
        self.lbl_info.setText("!!!ALARM!!!")
        self.lbl_info.setStyleSheet("QLabel { background-color : red; color : white; }");
        str_date = time.strftime("%d.%b. %H:%M:%S")
        
        if self.alarm_mode == False:
            print("Alarm auf Melder: {} am {} ".format(signal, str_date))
        
        if signal == "m1":
            self.scene_m1.addPixmap(self.img_melder_on)
            if self.alarm_mode == False:
                self.btn_stop.setEnabled(True)
                self.alarm_mode = True
        if signal == "m2":
            self.scene_m2.addPixmap(self.img_melder_on)
            if self.alarm_mode == False:
                self.btn_stop.setEnabled(True)
                self.alarm_mode = True       
        if signal == "m3":
            self.scene_m3.addPixmap(self.img_melder_on)
            if self.alarm_mode == False:
                self.btn_stop.setEnabled(True)
                self.alarm_mode = True
            

        
    def show_ip_dialog(self):
        dlg = QtWidgets.QDialog()
        ip_menu = IP_Picker(dlg)
        dlg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        if dlg.exec_() == QtWidgets.QDialog.Accepted:
            print('Ok')
            self.check_ip_thread.running = False
            self.check_ip_thread.quit()
            while self.check_ip_thread.isRunning():
                print("Waiting for Thread Closing!")
                time.sleep(0.5)
            self.scene_m1.addPixmap(self.img_unknown)
            self.scene_m2.addPixmap(self.img_unknown)
            self.scene_m3.addPixmap(self.img_unknown)
            self.lbl_t1.setText("-")
            self.lbl_t2.setText("-")
            self.lbl_t3.setText("-")
            self.ips = ip_menu.get_ips()
            self.lbl_ip1.setText(self.ips[0])
            self.lbl_ip2.setText(self.ips[1])
            self.lbl_ip3.setText(self.ips[2])
            self.check_ip_thread.set_ips(self.ips)
            self.check_ip_thread.running = True
            self.check_ip_thread.start()
            #self.btn_stop.setEnabled(True)
            
    def end_it(self):
        self.check_ip_thread.running = False
        self.check_ip_thread.quit()
        while self.check_ip_thread.isRunning():
            print("Warte auf Thread-Exit!")
            time.sleep(0.5)
        sys.exit(0)
            
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
 
    prog = Detector_Client(dialog)
 
    dialog.show()
    sys.exit(app.exec_())