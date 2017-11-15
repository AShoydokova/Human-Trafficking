import json, requests
import pandas as pd

def states():
    url='https://api.usa.gov/crime/fbi/ucr/ht/states?'
    
    params = dict(
        page=1,
        per_page=1000,
        output=json,
        api_key='MdzAauXtCO5Tbyy6mHgYiyihDhUxs9p05bRQYj2E'
    )
    
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    df = pd.DataFrame(data['results'])
    df.to_csv('human_trafficking_states.csv')
    
    return 1

def agencies():
    url = 'https://api.usa.gov/crime/fbi/ucr/ht/agencies?'
    
    df = pd.DataFrame()
    for i in range(1,8):

        print(i)    
        params = dict(
            page=i,
            per_page=1000,
            output=json,
            api_key='MdzAauXtCO5Tbyy6mHgYiyihDhUxs9p05bRQYj2E'
        )
        
        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)
        if df.empty:
            df = pd.DataFrame(data['results'])
        else:
            df = df.append(data['results'])
    df.to_csv('human_trafficking_agencies.csv')
    
    return 1

states()
agencies()
