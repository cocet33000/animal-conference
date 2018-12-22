# -*- coding: utf-8 -*-
import requests
import json
url = "https://slack.com/api/channels.history"
token = "xoxp-440767144820-440232906752-441137893685-19c47b9af0aa9b209243eb0f87a90ada"
channel_id = "test"
def main():
    payload = {
        "token": token,
        "channel": channel_id
        }
    response = requests.get(url, params=payload)

    json_data = response.json()
    messages = json_data["messages"]
    for i in messages:
        print(i["text"])
if __name__ == '__main__':
    main()
