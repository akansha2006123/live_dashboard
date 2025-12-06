import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px
import cv2
import json
from utils.heatmap import apply_heatmap
from utils.zones import get_zone
#from streamlit_autorefresh import st_autorefresh
st.set_page_config(
    page_title='Crowd Count Dahboard',
    page_icon= None,
    layout='wide'
)
#st_autorefresh(interval=1000,key="auto")

st.title("Live Crowdcount Dashboard")

def load_data():
    with open("data/crowd_count.json","r") as g:
        return json.load(g)
data= load_data()
total_people = data["total_people"]
zone_data= data["zone_count"]
points= data["points"]
col1 ,col2=st.columns(2)
with col1:
    st.metrics("Total people",total_people)
with col2:
    if total_people>30:
        st.error("Crowd Overloaded! Action Required!")
    else:
        st.success("Crowd Under Control")
st.subheader("Zone_wise Population")
st.bar_chart(zone_data)

if "history" not in st.session_state:
    st.session_state["history"]=[]

st.session_state["history"].append(total_people)
st.line_chart(st.session_state["history"])

st.subheader("Heatmap Overlay")

frame = np.zeros((480,640,3),dtype=np.uint8)
heatmap_frame = apply_heatmap(frame,points)
st.image(heatmap_frame,channels="BGR")