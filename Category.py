from googleapiclient.discovery import build
from config import api_key

youtube = build('youtube', 'v3', developerKey=api_key)

response = youtube.videoCategories().list(
    part='snippet',
    regionCode='PL'
).execute()


for category in response['items']:
    print(category['id'] + " : " + category['snippet']['title'])


#     Wyświetlanie wsyztskich kategorii z yt
