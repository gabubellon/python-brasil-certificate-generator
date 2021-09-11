from decouple import Csv, config

GOOGLE_SERVICE_ACCOUNT = config("GOOGLE_SERVICE_ACCOUNT")
SHEET_ID = config("SHEET_ID")

SHEET_DATA_RANGE = config("SHEET_DATA_RANGE")
SHEET_DATA_HEADER = config("SHEET_DATA_HEADER", cast=Csv())

SHEET_CERT_RANGE = config("SHEET_CERT_RANGE")
SHEET_CERT_HEADER = config("SHEET_CERT_HEADER", cast=Csv())

DRIVE_FOLDER_CERT_ID = config("DRIVE_FOLDER_CERT_ID")