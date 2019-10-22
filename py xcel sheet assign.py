from openpyxl import Workbook

workbook=Workbook()
sheet=workbook.active

sheet["A1"]="My"
sheet["B1"]="Application!!"

workbook.save(filename="My_Application.xlsx")
