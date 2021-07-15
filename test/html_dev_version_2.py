import streamlit as st
import pandas as pd
import os

pd.set_option('display.max_colwidth', 1000)

st.set_page_config(page_title="Ex-stream-ly Cool App", page_icon="🧊", layout="wide", initial_sidebar_state="expanded")
idx = 1

link = '[Please login to NEXUS ](http://nexus.int.seetrue.ai:8081/repository/data-image-snippets/quality_val_task/20190415_13133500_H_0017640895_IDSS02_1555326681_356/20190415_13133500_H_0017640895_IDSS02_1555326681_356_v5d0_chan1.png)'
st.markdown(link, unsafe_allow_html=True)

# File Filter
folder_path = folder_path = './'
#folder_path = [f for f in os.listdir('.') if os.path.isfile(f)]
filenames = [f for f in os.listdir(folder_path) if '.csv' in f]
selected_filename = st.sidebar.selectbox('Select a file', filenames)
csv_selected = os.path.join(folder_path, selected_filename)

# Data
a = pd.read_csv(csv_selected)
folder_name = pd.DataFrame(pd.Series([item[0].split('/')[-2] for item in a.values]).drop_duplicates())
folder_name.columns = ['scans']
short_name = pd.DataFrame([item[0].split('_IDSS')[-1] for item in folder_name.values])

# Folder Filter
scan_ID = st.sidebar.selectbox("Please select scan", short_name)
st.write('You selected:', scan_ID)
st.sidebar.table(short_name)

filtered = a[a["scans"].str.contains(scan_ID, na=False)]

for i in range(len(filtered)):
    with st.beta_container():
        for col in st.beta_columns(5):
            if idx >= len(filtered):
                break
            else:
                col.image(filtered.iloc[idx, 0], use_column_width=True)
                idx += 1
