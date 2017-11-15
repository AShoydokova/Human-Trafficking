import json, requests
import pandas as pd
from datetime import datetime
import pymongo
import sys

def doj_press_releases(db_name,collection_name):

    url='http://www.justice.gov/api/v1/press_releases.json?'
    
    for i in range(900,965):
        print('page', i)
        params = dict(
            page = i,
            pagesize=100,
        )

        client = pymongo.MongoClient()
        db = client[db_name]
        
        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)

        for doc in data['results']:
            if doc['created'] is not None: 
                doc['created_timestamp'] = datetime.fromtimestamp(int(doc['created']))
            if doc['date'] is not None: 
                doc['date_timestamp'] = datetime.fromtimestamp(int(doc['date']))
            if doc['changed'] is not None: 
                doc['changed_timestamp'] = datetime.fromtimestamp(int(doc['changed']))
            db[collection_name].update_one({'uuid': doc['uuid']},{'$set': doc},upsert=True)
        
    return 1

doj_press_releases(db_name='ht',collection_name='doj_pr')

