# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:25:57 2017

@author: gologius

Slackで保存しているURL付きのメッセージをJSON形式でファイルに書き出す．

1. get token
https://api.slack.com/custom-integrations/legacy-tokens

2. get target channel ID
Last of URL.
https://api.slack.com/methods/channels.list/test

"""

import urllib
import urllib.request, urllib.error
import json

token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" #your token
channel = "xxxxxxxxxxx" #target channel id
savePath = "urls.json"

def sendMessage(channelID, sendText):
    u"""
    指定されたチャンネルにメッセージを投稿する    
    
    Parameters
    -----
    channelID (string)
        送信対象のチャンネルのID文字列    
    sendText (string)
        送信するメッセージの内容
    
    Returns
    -----
    None
    """        
    params = {
        'token':token,
        'channel':channelID,
        'text': sendText
    }
    
    params = urllib.urlencode(params)
    req = urllib.request("https://slack.com/api/chat.postMessage")
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_data(params)
    
    res = urllib.urlopen(req)
    head = res.info()
    body = res.read()
    return
    
def getMessage(channelID, count = 100):
    u"""
    https://api.slack.com/methods/channels.history
    
    指定されたチャンネルのメッセージを取得して必要なデータのみ抽出する    
    
    Parameters
    -----
    channelID (string)
        送信対象のチャンネルのID文字列    
    count=100 (int)
        取得するメッセージの数．最大1000
    
    Returns
    -----
    messages and times (dict in list)
        メッセージと投稿時間を保持したdict型のリスト
    """        

    params = {
        'token':token,
        'channel':channelID,
        'count':count
    }
    
    #最高1000件ずつしか取得できない
    params = urllib.urlencode(params)
    req = urllib.request("https://slack.com/api/channels.history")
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_data(params)
    
    res = urllib.urlopen(req)
    body = res.read()
            
    #必要なデータ(本文と投稿時間)のみ抽出
    decoded = json.loads(body)
    results = []
    for m in decoded["messages"]:
        d = {}
        d["text"] = m["text"]                
        d["time"] = m["ts"]
        
        #<>で囲まれている場合は削除する
        if d["text"][0] == "<" and d["text"][-1] == ">":
            d["text"] = d["text"][1:-1]
        else:
            continue #囲まれていない=URLではない                        
        results.append(d)        
    
    #結果をファイルに保存    
    f = open(savePath,'w')
    json.dump(results,f,indent=4)

    return results
    
b = getMessage(channel, 1000)
print(b)
