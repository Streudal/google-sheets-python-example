# google-sheets-python-example
A sandbox for testing Google Sheets API stuff with Python.


## Google Account Setup
* Ensure you have a Google Cloud Account
* Create a project (i.e: "Python Google Tester").
    * Make sure it is selected.
* Enable “Google Drive API”
* Enable “Google Sheets API”
* Make sure “Apis & Services” is selected from top left hamburger menu
* Select “Credentials” on left hand side menu
* Select “Manage Service Accounts” 
    * Should be in page on the right hand side in blue
* Select “Create Service Account” at the top
    * Give it a name (Optional - give a description)
    * Select “Create and Continue”
    * Select “Continue”
    * Select “Done”
* Copy generated email (should end in <i>.iam.gserviceaccount.com</i>)
* Create a Sheet in Google Sheets (i.e: “Python Tester”)
* Select “Share” button
* Paste in the copied generated email
* Go back to Google Cloud Account and you should still be under the Service accounts page
* Select the three dots under the “Actions” column and select “Manage keys”
* Select “Add Key” -> “Create new key” -> select “JSON” -> “Create”
    * Private Key should download automatically


## Config Setup
* Store downloaded JSON private key to a different directory
  * Windows:
    * Open File Explorer
    * In address bar type in %APPDATA%
    * Create a new directory in here called “gspread”
    * Move downloaded JSON private key file to the newly created “gspread” directory and rename it to “service_account.json”
  * Mac:
    * `mkdir ~/.config/gspread`
    * `mv ~/Downloads/<downloaded-json-file> ~/.config/gspread/service_account.json`

## Python Setup
* Install packages: 
  * pip install gspread

<b><i>Optional:</i></b> I use a virtual environment for Python (pyenv) so I usually do a `pip freeze > requirements.txt` so I know which packages I need to install. Then just `pip install -r ./requirements.txt` from terminal if inside the same directory.
