import streamlit as st
import pandas as pd
import numpy as np
import SessionState 

# https://gist.githubusercontent.com/tvst/036da038ab3e999a64497f42de966a92/raw/f0db274dd4d295ee173b4d52939be5ad55ae058d/SessionState.py

# Create an empty dataframe
data = pd.DataFrame(columns=["Random"])
st.text("Original dataframe")

# with every interaction, the script runs from top to bottom
# resulting in the empty dataframe
st.dataframe(data) 

# persist state of dataframe
session_state = SessionState.get(df=data)

# random value to append; could be a num_input widget if you want
random_value = np.random.randn()

if st.button("Append random value"):
    # update dataframe state
    session_state.df = session_state.df.append({'Random': random_value}, ignore_index=True)
    st.text("Updated dataframe")
    st.dataframe(session_state.df)

# still empty as state is not persisted
st.text("Original dataframe")
st.dataframe(data)