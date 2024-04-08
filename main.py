import gspread

# If you store the JSON private key file in this project then you can just
# reference it by filename here.
# serviceAccount = gspread.service_account(filename="") 
serviceAccount = gspread.service_account() # Get service account
sheet = serviceAccount.open("Python Tester") # Name of created Google Sheet it has access to

worksheet = sheet.worksheet("Sheet1")
worksheet.update([["Hunter is cool", "What about tyler?"]], "A1")




# Example Calls to Google Sheets
# =====================================================
# print("Rows: ", worksheet.row_count)
# print("Cols: ", worksheet.col_count)
# print(worksheet.acell("A9").value)
# print(worksheet.cell(3,4).value) 
# print(worksheet.get("A7:E9"))
# print(worksheet.get_all_records())
