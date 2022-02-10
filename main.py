import streamlit as st
import requests
import json
import datetime
import pandas as pd
import re

st.title("大分県関係の番組")

z=("大分")

t_delta = datetime.timedelta(hours=9)  
JST = datetime.timezone(t_delta, 'JST')  
dt = datetime.datetime.now(JST)
du = dt.strftime('%Y-%m-%d')
ap="https://api.nhk.or.jp/v2/pg/list/440/tv/"+du+".json?key=t4fDaYNIS6qmUqAhy3ihGdWTh8Lf1N5M"

url = requests.get(ap)
text = url.text
data = json.loads(text)["list"]
tv = data["g1"]+data["g2"]+data["e1"]+data["s1"]+data["s3"]

pd.set_option("display.max_colwidth", 80)
df = pd.DataFrame((list(tv)), columns = ['title','start_time','subtitle','act','content'])
az=(df.query('title.str.contains(@z)', engine='python'))
st.dataframe(az.style.wrap_text=True)
