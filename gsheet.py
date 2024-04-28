import os
import pandas as pd
import sqlite3
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_gsheet():
    # Authenticate the API using the JSON key file
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.getcwd() + '/key.json', scope)
    client = gspread.authorize(creds)

    # Open the worksheet by name and collect all data
    sheet = client.open('physical_activities').worksheet('data')
    sheet = sheet.get_all_records()
    sheet = pd.DataFrame(sheet)
    sheet['date'] = pd.to_datetime(sheet['date'], format='%m/%d/%Y')
    sheet['workout_time'] = pd.to_timedelta(sheet['workout_time'])
    sheet['workout_time'] = sheet['workout_time'].dt.total_seconds()/60
    return sheet

def create_data_base():
    connection = sqlite3.connect(database='sports.db')
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Sports(
            activity varchar(255),
            date datetime,
            workout_time float,
            total_calories int,
            activated_calories int,
            average_heart_rate int
        );
        '''
    )
    connection.commit()
    connection.close()
    return

def insert_values(values, table_name):
    connection = sqlite3.connect(database='sports.db')
    values.to_sql(table_name, con=connection, index=False, if_exists='replace')
    connection.commit()
    connection.close()
    return

def sports_data():
    create_data_base()
    physical = read_gsheet()
    insert_values(physical, 'Sports')
    return

if __name__ == '__main__':
    sports_data()