from openpyxl import Workbook, load_workbook, styles

book = load_workbook("Шаблон отчета о паттернах и транзакциях.xlsx")
wb1 = book.active
wb = wb1["Транзакции"]

data1 = (wb['A2'].font)
data2 = (wb['A2'].fill)
data11 = (wb['B2'].font)
data22= (wb['B2'].fill)
print(data1, data2)
#print(data2)