import numpy as np
import streamlit as st
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

st.set_page_config(page_title="Ex-stream-ly Cool App", page_icon="🧊",layout="wide", initial_sidebar_state="expanded")
idx = 1
a = pd.read_csv('scans_2.csv')


folder_name = pd.DataFrame(pd.Series([item[0].split('/')[-2] for item in a.values]).drop_duplicates())
folder_name.columns=['scans']
short_name = pd.DataFrame([item[0].split('_IDSS')[-1] for item in folder_name.values])


### USER CONTORL
scan_ID = st.sidebar.selectbox("Please select scan", short_name)
st.write('You selected:', scan_ID)
st.sidebar.table(short_name)



if st.button('Next Folder'):
    short_name.columns = ['scan']
    short_name_index = short_name[short_name['scan'].str.contains(scan_ID, na=False)].index.values.astype(int) + 1
    scan_ID = short_name.get_value(short_name_index[0], 'scan')
    st.write('You selected:', scan_ID)


filtered = a[a["scans"].str.contains(scan_ID, na=False)]

for i in range(len(filtered)):
    with st.beta_container():
        for col in st.beta_columns(4):
            if idx >= len(filtered):
                break
            else:
                col.image(filtered.iloc[idx, 0], use_column_width=True)
                idx += 1
