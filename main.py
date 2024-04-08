import gspread

# Documentation: https://docs.gspread.org/en/v6.0.0/index.html

# Get service account credentials
serviceAccount = gspread.service_account()

# Optional: Different way of configuring credentials (add this import `from google.oauth2.service_account import Credentials`)
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# json_key_path = "" # Paste absolute file path here
# creds = Credentials.from_service_account_file(json_key_path, scopes=scope)
# client = gspread.authorize(creds)

# Name of created Google Sheet it has access to (remember to add service account email to that shared list)
spreadsheet = serviceAccount.open("Python Tester")

# Get the the sheet by it's name 
sheet1 = spreadsheet.worksheet("Sheet1")

# Update the sheets data
sheet1.update(
  [
    ["Hunter is cool!", "What about tyler?", "Hmmm idkkkkkk"]
  ]
)

# Create a new worksheet in "Python Tester" spreadsheet
new_worksheet = spreadsheet.add_worksheet(title="A new worksheet", rows=100, cols=20)

# View all available worksheets for "Pyton Tester" spreadsheet
worksheet_list = spreadsheet.worksheets()
print("Worksheets: ", worksheet_list)

# Create a new spreadsheet
new_spreadsheet = serviceAccount.create('NewSpreadsheet') # Disclaimer: This will only be available for the service account so you will need to add your actual google account to instantly share this so you can view it. Feel like this should be automatic... weird Google shit
new_spreadsheet.share('<your-google-account-email-here>', perm_type='user', role='writer') # maybe be able to change role='writer' to role='owner' just to see if this works too.




# Example Calls to Google Sheets for above code
# =====================================================
# print("Rows: ", sheet1.row_count)
# print("Cols: ", sheet1.col_count)
# print(sheet1.acell("A9").value)
# print(sheet1.cell(3,4).value) 
# print(sheet1.get("A7:E9"))
# print(sheet1.get_all_records())
