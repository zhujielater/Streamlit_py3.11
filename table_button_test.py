# ref: https://discuss.streamlit.io/t/make-streamlit-table-results-hyperlinks-or-add-radio-buttons-to-table/7883/3
import streamlit as st
import pandas as pd

# Create a dataframe
df = pd.DataFrame({
    'ID': [25, 30, 35],
    'EPROB_ID': ['EPROB123456', 'EPROB987654', 'EPROB456789'],
    'BT_FILE': ['A', 'B', 'C'],
    'REDRESS_CALC': ['True', 'False', 'True'],
    'SHOW_STATE': [False, False, False],
})

# Convert dataframe to dictionary
user_table = df.to_dict()

# # Show user table 
colms = st.columns((1, 2, 2, 1, 1))
fields = ["ID", 'EPROB_ID', 'Category', 'Status', "BT_FILE"]
for col, field_name in zip(colms, fields):
    # header
    col.write(field_name)

for x, email in enumerate(user_table['EPROB_ID']):
    col1, col2, col3, col4, col5 = st.columns((1, 2, 2, 1, 1))
    col1.write(x)  # index
    col2.write(user_table['EPROB_ID'][x])  # email
    col3.write(user_table['BT_FILE'][x])  # unique ID
    col4.write(user_table['REDRESS_CALC'][x])   # email status
    show_state = user_table['SHOW_STATE'][x]  # flexible type of button
    button_text = "BT_File" if show_state else "BT_File"
    button_phold = col5.empty()  # create a placeholder
    do_action = button_phold.button(button_text, key=x)

    if 'show_ind' not in st.session_state:
        st.session_state['show_ind'] = False

    if do_action:
        if not st.session_state['show_ind']: # NEED TO SHOW
            detail_phold = st.empty()
            detail_phold.write(user_table['EPROB_ID'][x])
        else:
            detail_phold = st.empty()
        st.session_state['show_ind'] = not st.session_state['show_ind']