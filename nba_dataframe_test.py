import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from nba_api.stats.endpoints import shotchartdetail
import pandas

player_id = 2554
season_id = "2022-23"

response = shotchartdetail.ShotChartDetail(
  team_id=0,
  player_id=player_id,
  season_nullable=season_id,
  season_type_all_star="Regular Season"
).get_data_frames()

# Extract the shot data from the response and create a DataFrame
shots = response[0]
print(shots)
df = pandas.DataFrame(shots)

# Export DataFrame to Google Sheet
# Setup credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
json_key_path = "" # Paste absolute file path here
creds = Credentials.from_service_account_file(json_key_path, scopes=scope)
client = gspread.authorize(creds)

# Open the Google Sheet and write DataFrame to it
# - Create new Google Sheet
# - Name it "LebronJames"
# - Share the sheet with the service account email created.
sheet_name = "LebronJames"
sheet = client.open(sheet_name).sheet1
set_with_dataframe(sheet,df)
