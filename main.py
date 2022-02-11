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
for i in range(0,8):
    dayy = now+datetime.timedelta(days=i)
    du = dayy.strftime('%Y-%m-%d')
    ap="https://api.nhk.or.jp/v2/pg/list/440/tv/"+du+".json?key=xQUIY1xXNVtrG9AQ1OWCdfHh4kD9iW1e"
    url = requests.get(ap)
    text = url.text
    data = json.loads(text)["list"]
    lst.append(data)

df1 = pd.DataFrame(lst)
tv = df1["g1"]+df1["e1"]+df1["s1"]+df1["s3"]
df = pd.DataFrame((list(df1)), columns = ['start_time','title','subtitle','act','content'])
z=("大分")
az=(df.query('title.str.contains(@z)|\
              subtitle.str.contains(@z)|\
              content.str.contains(@z)|\
              act.str.contains(@z)', engine='python'))
st.dataframe(az)
