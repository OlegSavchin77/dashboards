import streamlit as st
import pandas as pd
import os
import pathlib
pd.set_option('display.max_colwidth', 1000)

st.set_page_config(page_title="Ex-stream-ly Cool App", page_icon="🧊", layout="wide", initial_sidebar_state="expanded")
idx = 1

link = '[Please login to NEXUS ](https://nexus.seetrue.ai/repository/data-image-snippets/welcome_page/welcome.png)'
st.markdown(link, unsafe_allow_html=True)

# list sub_directories
output = [name for name in os.listdir('.') if os.path.isdir(os.path.join('.', name))]
filtered_output = [dir for dir in output if dir in ['XRAY', 'CT', 'analyze']]
sub_directories = st.sidebar.selectbox('Select folder', filtered_output)


# File Filter
folder_path = pathlib.Path(__file__).parent.resolve()
filenames = [f for f in os.listdir(sub_directories) if '.csv' in f]
selected_filename = st.sidebar.selectbox('Select a file', filenames)
csv_selected = os.path.join(sub_directories, selected_filename)

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
                col.code(filtered.iloc[idx, 0].split('/')[-1])
                idx += 1
