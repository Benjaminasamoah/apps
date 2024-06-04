import streamlit as st
import pandas as pd
import gspread
st.title("# Sales per Year")

import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "10gfIaCd-eFg2VVQorN3NGrnYENCzafVluU0Sjd0nHdY"
workbook= client.open_by_key(sheet_id)

sheet = workbook.worksheet("sales 2")
cell = sheet.find("gooogo")
print(cell.row,cell.col)
