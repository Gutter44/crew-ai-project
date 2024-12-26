from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file'
]

def authenticate_google_services():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials/credentials.json', SCOPES
    )
    creds = flow.run_local_server(port=0)
    return creds
