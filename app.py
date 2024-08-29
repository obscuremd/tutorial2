from pathlib import Path
from excel_automation import add_new_chart

path = Path()
excel_sheet = ''
for files in path.glob('transactions.xlsx'):
    excel_sheet = files


add_new_chart(excel_sheet)


print(excel_sheet)

# print(path.glob('*.py'))