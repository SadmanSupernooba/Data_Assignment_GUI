import sys
from PyQt4 import QtGui
import pandas as pd
import json
import numpy as np
import random
from collections import defaultdict,OrderedDict

var = pd.read_excel("Data_Assignment.xlsx","raw_data")
rowN, colN = var.shape
#print(var)
#run_id = var['run_id'].values.tolist()
#print(run_id)


data_arr = []
data_arr_keys = ["run_id", "flange_id", "bolt_size", "bolt_number", "flange_t", "flange_D", "flange_d2", "bolt_PCD_inner",
"wrench_size", "bolt_spacing_calculated", "Failure_mode", "SME_Petersen_Seidel", "fastener_mass_total", "flange_connection_mass_total_machined",
"connection_mass_total", "fastener_cost_total", "flange_connection_cost_total", "preload_labour_cost_total", "connection_cost_total",
"Failure_mode_A_valid", "Failure_mode_B_valid", "Failure_mode_C_valid", "Failure_mode_D_valid", "Failure_mode_E_valid", 
"Failure_mode_A_Fu", "Failure_mode_B_Fu", "Failure_mode_C_Fu", "Failure_mode_D_Fu", "Failure_mode_E_Fu", 
"positive_margin_extreme", "bolt_reserve_factor", "bolt_damage", "positive_margin_fatigue", "SN_test_value", "SN_valid", 
"clamp_length_bolt_d_ratio", "optimize_inner_diameter", "update_fatigue", "bolt_damage_old", "update_siedel", 
"flange_d_old", "flange_d3", "Petersen_a_old", "Petersen_a", "valid", "lowest_valid_thickness"]


#Assumptions: randomly 3 selected for each case to be positive
p2 = random.randint(0,69)
q2 = random.randint(0,69)
r2 = random.randint(0,69)
#print(var['SME_Petersen_Seidel'][p2])
var['SME_Petersen_Seidel'][p2] = abs(var['SME_Petersen_Seidel'][p2])
var['SME_Petersen_Seidel'][q2] = abs(var['SME_Petersen_Seidel'][q2])
var['SME_Petersen_Seidel'][r2] = abs(var['SME_Petersen_Seidel'][r2])

p3 = random.randint(70,70+44)
q3 = random.randint(70,70+44)
r3 = random.randint(70,70+44)
var['SME_Petersen_Seidel'][p3] = abs(var['SME_Petersen_Seidel'][p3])
var['SME_Petersen_Seidel'][q3] = abs(var['SME_Petersen_Seidel'][q3])
var['SME_Petersen_Seidel'][r3] = abs(var['SME_Petersen_Seidel'][r3])

p4 = random.randint(115,115+100)
q4 = random.randint(115,115+100)
r4 = random.randint(115,115+100)
var['SME_Petersen_Seidel'][p4] = abs(var['SME_Petersen_Seidel'][p4])
var['SME_Petersen_Seidel'][q4] = abs(var['SME_Petersen_Seidel'][q4])
var['SME_Petersen_Seidel'][r4] = abs(var['SME_Petersen_Seidel'][r4])

data_dictionary = OrderedDict(defaultdict(list))

def createDictionary(_dictionary, _data, _keys):
    it = 0
    for i in _keys:
        _dictionary[i] = _data[it]
        it += 1
    #print(_dictionary)

def convertToString(list):
    list = [str(item) for item in list]
    return list
def convertToFloat(list):
    list = [float(item) for item in list]
    return list
#variables

run_id = var['run_id'].values.tolist()
run_id = convertToString(run_id)
data_arr.append(run_id)

flange_id = var['flange_id'].values.tolist()
flange_id = convertToString(flange_id)
data_arr.append(flange_id)

bolt_size = var['bolt_size'].values.tolist()
bolt_size = convertToString(bolt_size)
data_arr.append(bolt_size)

bolt_number = var['bolt_number'].values.tolist()
bolt_number = convertToString(bolt_number)
data_arr.append(bolt_number)

flange_t = var['flange_t'].values.tolist()
flange_t = convertToString(flange_t)
data_arr.append(flange_t)

flange_D = var['flange_D'].values.tolist()
flange_D = convertToString(flange_D)
data_arr.append(flange_D)

flange_d2 = var['flange_d2'].values.tolist()
flange_d2 = convertToString(flange_d2)
data_arr.append(flange_d2)

bolt_PCD_inner = var['bolt_PCD_inner'].values.tolist()
bolt_PCD_inner = convertToString(bolt_PCD_inner)
data_arr.append(bolt_PCD_inner)

wrench_size = var['wrench_size'].values.tolist()
wrench_size = convertToString(wrench_size)
data_arr.append(wrench_size)

bolt_spacing_calculated = var['bolt_spacing_calculated'].values.tolist()
bolt_spacing_calculated = convertToString(bolt_spacing_calculated)
data_arr.append(bolt_spacing_calculated)

Failure_mode = var['Failure_mode'].values.tolist()
Failure_mode = convertToString(Failure_mode)
data_arr.append(Failure_mode)

SME_Petersen_Seidel = var['SME_Petersen_Seidel'].values.tolist()
SME_Petersen_Seidel = convertToString(SME_Petersen_Seidel)
data_arr.append(SME_Petersen_Seidel)

fastener_mass_total = var['fastener_mass_total'].values.tolist()
fastener_mass_total = convertToString(fastener_mass_total)
data_arr.append(fastener_mass_total)

flange_connection_mass_total_machined = var['flange_connection_mass_total_machined'].values.tolist()
flange_connection_mass_total_machined = convertToString(flange_connection_mass_total_machined)
data_arr.append(flange_connection_mass_total_machined)

connection_mass_total = var['connection_mass_total'].values.tolist()
connection_mass_total = convertToString(connection_mass_total)
data_arr.append(connection_mass_total)

fastener_cost_total = var['fastener_cost_total'].values.tolist()
fastener_cost_total = convertToString(fastener_cost_total)
data_arr.append(fastener_cost_total)

flange_connection_cost_total = var['flange_connection_cost_total'].values.tolist()
flange_connection_cost_total = convertToString(flange_connection_cost_total)
data_arr.append(flange_connection_cost_total)

preload_labour_cost_total = var['preload_labour_cost_total'].values.tolist()
preload_labour_cost_total = convertToString(preload_labour_cost_total)
data_arr.append(preload_labour_cost_total)

connection_cost_total = var['connection_cost_total'].values.tolist()
connection_cost_total = convertToString(connection_cost_total)
data_arr.append(connection_cost_total)

Failure_mode_A_valid = var['Failure_mode_A_valid'].values.tolist()
Failure_mode_A_valid = convertToString(Failure_mode_A_valid)
data_arr.append(Failure_mode_A_valid)

Failure_mode_B_valid = var['Failure_mode_B_valid'].values.tolist()
Failure_mode_B_valid = convertToString(Failure_mode_B_valid)
data_arr.append(Failure_mode_B_valid)

Failure_mode_C_valid = var['Failure_mode_C_valid'].values.tolist()
Failure_mode_C_valid = convertToString(Failure_mode_C_valid)
data_arr.append(Failure_mode_C_valid)

Failure_mode_D_valid = var['Failure_mode_D_valid'].values.tolist()
Failure_mode_D_valid = convertToString(Failure_mode_D_valid)
data_arr.append(Failure_mode_D_valid)

Failure_mode_E_valid = var['Failure_mode_E_valid'].values.tolist()
Failure_mode_E_valid = convertToString(Failure_mode_E_valid)
data_arr.append(Failure_mode_E_valid)

Failure_mode_A_Fu = var['Failure_mode_A_Fu'].values.tolist()
Failure_mode_A_Fu = convertToString(Failure_mode_A_Fu)
data_arr.append(Failure_mode_A_Fu)

Failure_mode_B_Fu = var['Failure_mode_B_Fu'].values.tolist()
Failure_mode_B_Fu = convertToString(Failure_mode_B_Fu)
data_arr.append(Failure_mode_B_Fu)

Failure_mode_C_Fu = var['Failure_mode_C_Fu'].values.tolist()
Failure_mode_C_Fu = convertToString(Failure_mode_C_Fu)
data_arr.append(Failure_mode_C_Fu)

Failure_mode_D_Fu = var['Failure_mode_D_Fu'].values.tolist()
Failure_mode_D_Fu = convertToString(Failure_mode_D_Fu)
data_arr.append(Failure_mode_D_Fu)

Failure_mode_E_Fu = var['Failure_mode_E_Fu'].values.tolist()
Failure_mode_E_Fu = convertToString(Failure_mode_E_Fu)
data_arr.append(Failure_mode_E_Fu)

positive_margin_extreme = var['positive_margin_extreme'].values.tolist()
positive_margin_extreme = convertToString(positive_margin_extreme)
data_arr.append(positive_margin_extreme)

bolt_reserve_factor = var['bolt_reserve_factor'].values.tolist()
bolt_reserve_factor = convertToString(bolt_reserve_factor)
data_arr.append(bolt_reserve_factor)

bolt_damage = var['bolt_damage'].values.tolist()
bolt_damage = convertToString(bolt_damage)
data_arr.append(bolt_damage)

positive_margin_fatigue = var['positive_margin_fatigue'].values.tolist()
positive_margin_fatigue = convertToString(positive_margin_fatigue)
data_arr.append(positive_margin_fatigue)

SN_test_value = var['SN_test_value'].values.tolist()
SN_test_value = convertToString(SN_test_value)
data_arr.append(SN_test_value)

SN_valid = var['SN_valid'].values.tolist()
SN_valid = convertToString(SN_valid)
data_arr.append(SN_valid)

clamp_length_bolt_d_ratio = var['clamp_length_bolt_d_ratio'].values.tolist()
clamp_length_bolt_d_ratio = convertToString(clamp_length_bolt_d_ratio)
data_arr.append(clamp_length_bolt_d_ratio)

optimize_inner_diameter = var['optimize_inner_diameter'].values.tolist()
optimize_inner_diameter = convertToString(optimize_inner_diameter)
data_arr.append(optimize_inner_diameter)

update_fatigue = var['update_fatigue'].values.tolist()
update_fatigue = convertToString(update_fatigue)
data_arr.append(update_fatigue)

bolt_damage_old = var['bolt_damage_old'].values.tolist()
bolt_damage_old = convertToString(bolt_damage_old)
data_arr.append(bolt_damage_old)

update_siedel = var['update_siedel'].values.tolist()
update_siedel = convertToString(update_siedel)
data_arr.append(update_siedel)

flange_d_old = var['flange_d_old'].values.tolist()
flange_d_old = convertToString(flange_d_old)
data_arr.append(flange_d_old)

flange_d3 = var['flange_d3'].values.tolist()
flange_d3 = convertToString(flange_d3)
data_arr.append(flange_d3)

Petersen_a_old = var['Petersen_a_old'].values.tolist()
Petersen_a_old = convertToString(Petersen_a_old)
data_arr.append(Petersen_a_old)

Petersen_a = var['Petersen_a'].values.tolist()
Petersen_a = convertToString(Petersen_a)
data_arr.append(Petersen_a)

valid = var['valid'].values.tolist()
valid = convertToString(valid)
data_arr.append(valid)

lowest_valid_thickness = var['lowest_valid_thickness'].values.tolist()
lowest_valid_thickness = convertToString(lowest_valid_thickness)
data_arr.append(lowest_valid_thickness)

createDictionary(data_dictionary, data_arr, data_arr_keys)



class ValidSolutionsTableWidget(QtGui.QWidget):
    
    def __init__(self):
        super(ValidSolutionsTableWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Valid_Solutions_Table')

        #Grid Layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        table = QtGui.QTableWidget(self)
        table.setRowCount(9)
        table.setColumnCount(colN)
        table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        stylesheet = "::section{Background-color:rgb(0,255,255)}"
        table.horizontalHeader().setStyleSheet(stylesheet)

        
        #Enter data onto Table
        horHeaders = []
        for n, key in enumerate(data_dictionary.keys()):
            horHeaders.append(key)
            cnt = 0
            for m, item in enumerate(data_dictionary[key]):
                if float(data_dictionary['SME_Petersen_Seidel'][m]) > 0.0:
                    newitem = QtGui.QTableWidgetItem(item)
                    table.setItem(cnt, n, newitem)
                    cnt += 1
        
        #Add Header
        table.setHorizontalHeaderLabels(horHeaders)        

        #Adjust size of Table
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        
        #Add Table to Grid
        grid.addWidget(table, 0,0)

class BestSolutionsTableWidget(QtGui.QWidget):
    
    def __init__(self):
        super(BestSolutionsTableWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Best_Solutions_Table') 

        #Grid Layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        table = QtGui.QTableWidget(self)
        table.setRowCount(3)
        table.setColumnCount(colN)
        table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        stylesheet = "::section{Background-color:rgb(0,255,255)}"
        table.horizontalHeader().setStyleSheet(stylesheet)

        
        #Enter data onto Table
        minVal2 = 1000000.0
        minVal3 = 1000000.0
        minVal4 = 1000000.0
        flange_connection_cost_total1 = flange_connection_cost_total
        flange_connection_cost_total2 = convertToFloat(flange_connection_cost_total1)
        itr = 0
        for i in flange_connection_cost_total2:
            #print(i)
            if i < minVal2 and float(data_dictionary['SME_Petersen_Seidel'][itr]) > 0.0:
                if(itr > -1 and itr < 70):
                    minVal2 = i
            if i < minVal3 and float(data_dictionary['SME_Petersen_Seidel'][itr]) > 0.0:
                if(itr > 69 and itr < 115):
                    minVal3 = i
            if i < minVal4 and float(data_dictionary['SME_Petersen_Seidel'][itr]) > 0.0:
                if(itr > 114 and itr < 362):
                    minVal4 = i
            itr += 1

        horHeaders = []
        for n, key in enumerate(data_dictionary.keys()):
            horHeaders.append(key)
            cnt = 0
            for m, item in enumerate(data_dictionary[key]):
                if float(data_dictionary['SME_Petersen_Seidel'][m]) > 0.0:
                    if float(data_dictionary['flange_connection_cost_total'][m]) == minVal2:
                        newitem = QtGui.QTableWidgetItem(item)
                        table.setItem(cnt, n, newitem)
                        cnt += 1
                    if float(data_dictionary['flange_connection_cost_total'][m]) == minVal3:
                        newitem = QtGui.QTableWidgetItem(item)
                        table.setItem(cnt, n, newitem)
                        cnt += 1
                    if float(data_dictionary['flange_connection_cost_total'][m]) == minVal4:
                        newitem = QtGui.QTableWidgetItem(item)
                        table.setItem(cnt, n, newitem)
                        cnt += 1
        #Add Header
        table.setHorizontalHeaderLabels(horHeaders)        

        #Adjust size of Table
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        
        #Add Table to Grid
        grid.addWidget(table, 0,0)




class CustomTableWidget(QtGui.QWidget):
    
    def __init__(self):
        super(CustomTableWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Raw_Data_Table')     
        
        #Grid Layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        
        #Data
        '''data = {'Kitty':['1','2','3','3'], 
                'Cat':['4','5','6','2'], 
                'Meow':['7','8','9','5'],
                'Purr':['4','3','4','8'],}'''
        
        #Create Empty 5x5 Table
        table = QtGui.QTableWidget(self)
        table.setRowCount(rowN)
        table.setColumnCount(colN)
        table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        stylesheet = "::section{Background-color:rgb(0,255,255)}"
        table.horizontalHeader().setStyleSheet(stylesheet)
        
        #Enter data onto Table
        horHeaders = []
        for n, key in enumerate(data_dictionary.keys()):
            horHeaders.append(key)
            for m, item in enumerate(data_dictionary[key]):
                newitem = QtGui.QTableWidgetItem(item)
                table.setItem(m, n, newitem)
        
        #Add Header
        table.setHorizontalHeaderLabels(horHeaders)        

        #Adjust size of Table
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        
        #Add Table to Grid
        grid.addWidget(table, 0,0)

        def on_click_btn1():
            dialog = ValidSolutionsTableWidget()
            self.dialogs.append(dialog)
            dialog.show()
            

        def on_click_btn2():
            #print('clicked')
            dialog = BestSolutionsTableWidget()
            self.dialogs.append(dialog)
            dialog.show()

        btn1 = QtGui.QPushButton('Show Valid Solutions', self)
        btn1.setToolTip('Click here to see all the valid solutions')
        btn1.resize(btn1.sizeHint())
        btn1.move(250, 400)
        btn1.setStyleSheet("background-color: cyan");
        btn1.clicked.connect(on_click_btn1)

        btn2 = QtGui.QPushButton('Show Best Solutions', self)
        btn2.setToolTip('Click here to see all the best solutions for each case')
        btn2.resize(btn1.sizeHint())
        btn2.move(500, 400)
        btn2.setStyleSheet("background-color: cyan");
        btn2.clicked.connect(on_click_btn2)
        self.dialogs = list()
        

        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    w = CustomTableWidget()
    app.exec_()


if __name__ == '__main__':
    main()