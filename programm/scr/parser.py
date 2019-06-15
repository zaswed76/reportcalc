
import pandas as pd
import xlrd

# Assign spreadsheet filename to `file`
file = r'D:\service\isystem\projects\reportcalc\doc\test.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Лист1')
print(df1)