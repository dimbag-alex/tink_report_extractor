import datetime
import openpyxl
import os




def main(fname, savefname):
    print("outmain" + savefname)
    wb = openpyxl.load_workbook(fname)
    sheet = wb.active
    need_inf = [7, 11, 12, 19]
    new = []
    for row in list(sheet.rows):
        string = []
        if row[3].value == "incomeLegal":
            for i in need_inf:
                if i == 7:
                    string.append(".".join(str(row[i].value.date()).split("-")))
                    print(row[i].value.date())
                else:
                    string.append(str(row[i].value))
            new.append(string)
    wb = openpyxl.Workbook()
    wb.iso_dates = True
    sheet = wb.active
    sheet["A1"] = "Дата транзакции"
    sheet["B1"] = "Сумма в валюте операции"
    sheet["C1"] = "Контрагент"
    sheet["D1"] = "Назначение платежа"
    sheet.column_dimensions['A'].width = 16
    sheet.column_dimensions['B'].width = 25
    sheet.column_dimensions['C'].width = 80
    sheet.column_dimensions['D'].width = 100
    for row in range(1, len(new) + 1):
        sheet.append(new[row - 1])
    wb.save(f"{savefname}.xlsx")

# main(r"C:\Users\alexa\OneDrive\Рабочий стол\statement.xlsx")
