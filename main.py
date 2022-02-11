import streamlit as st
import requests
import json
import datetime
import pandas as pd
import re
import pytz

st.title("大分県関係の番組")
now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
lst=[]
for i in range(0,7):
    dayy = now+datetime.timedelta(days=i)
    du = dayy.strftime('%Y-%m-%d')
    ap="https://api.nhk.or.jp/v2/pg/list/440/tv/"+du+".json?key=2GD6o07t1gARYpXF19gsfbYgJwbjnDNP"
    url = requests.get(ap)
    text = url.text
    data = json.loads(text)
    b=data.keys()
    print(b)
    ke=data["list"]
    tv = ke["g1"]+ke["e1"]+ke["s1"]+ke["s3"]
    lst.extend(tv)
    
df = pd.DataFrame((list(lst)), columns = ['start_time','title','subtitle','act','content'])
z=("大分")
az=(df.query('title.str.contains(@z)|\
              subtitle.str.contains(@z)|\
              content.str.contains(@z)|\
              act.str.contains(@z)', engine='python'))
st.dataframe(az)
