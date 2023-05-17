import requests

def nimadur(message):
    url = "https://instagram-story-downloader-media-downloader.p.rapidapi.com/index"

    querystring = {"url":f"{message.text}"}

    headers = {
        "X-RapidAPI-Key": "901af23752msh7c051f4139a8db7p13ac8djsn2345135172bb",
        "X-RapidAPI-Host": "instagram-story-downloader-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
