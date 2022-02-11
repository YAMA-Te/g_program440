import streamlit as st
import requests
import json
import datetime
import pandas as pd
import re

st.title("大分県関係の番組")

now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
for i in range(0,8):
    dayy = now+datetime.timedelta(days=i)
    du = dayy.strftime('%Y-%m-%d')
    ap="https://api.nhk.or.jp/v2/pg/list/440/tv/"+du+".json?key=t4fDaYNIS6qmUqAhy3ihGdWTh8Lf1N5M"
    url = requests.get(ap)
    text = url.text
    data = json.loads(text)["list"]
    tv = data["g1"]+data["e1"]+data["s1"]+data["s3"]

    df = pd.DataFrame((list(tv)), columns = ['start_time','title','subtitle','act','content'])
    z=("大分")
    az=(df.query('title.str.contains(@z)|\
                 subtitle.str.contains(@z)|\
                 content.str.contains(@z)|\
                 act.str.contains(@z)', engine='python'))
st.dataframe(az)
