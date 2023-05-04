import streamlit as st
import pandas as pd
from datetime import datetime

st.write('# Online Medal')

if 'data' not in st.session_state:
    data = pd.read_csv('medal.csv')
    st.session_state.data = data

data = st.session_state.data

# Converting links to html tags
def path_to_image_html(path):
    return '<img src="' + path + '" width="60" >'

@st.cache_data
def convert_df(input_df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return input_df.to_html(escape=False, formatters=dict(Medal=path_to_image_html))

html = convert_df(data)

st.markdown(
    html,
    unsafe_allow_html=True
)

# Saving the dataframe as a webpage

st.download_button(
     label="Download data as HTML",
     data=html,
     file_name='output.html',
     mime='text/html',
 )

# FORM START

def add_dfForm():
    row = pd.DataFrame({'Name':[st.session_state.input_Name],
            'Date':[datetime.now().strftime("%Y/%m/%d %H:%M:%S")],
            'Description':[st.session_state.input_Description],
            'Attachment':[st.session_state.input_Attachment],
            'Medal':"https://freeiconshop.com/wp-content/uploads/edd/badge-outline-filled.png"})
    df = pd.concat([st.session_state.data, row])
    st.session_state.data = df
    df.to_csv('medal.csv', index=False)
    

date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

dfForm = st.form(key='dfForm')
with dfForm:
    dfColumns = st.columns(4)
    with dfColumns[0]:
        st.text_input('Name', key='input_Name', value='Kenson Zhu')
    with dfColumns[1]:
        st.text_input('Date', key='input_Date', value=date_time)
    with dfColumns[2]:
        st.text_input('Description', key='input_Description')
    with dfColumns[3]:
        st.text_input('Attachment', key='input_Attachment')
    st.form_submit_button(on_click=add_dfForm)