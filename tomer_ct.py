import streamlit as st
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

st.set_page_config(page_title="Ex-stream-ly Cool App", page_icon="🧊",layout="wide", initial_sidebar_state="expanded")
idx = 1
a = pd.read_csv('scans_ct.csv')



for i in range(len(a)):
    with st.beta_container():
        for col in st.beta_columns(5):
            if idx >= len(a):
                break
            else:
                col.image(a.iloc[idx, 0], use_column_width=True)
                idx += 1
