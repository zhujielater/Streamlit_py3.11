import streamlit as st


st.title("My Two-Column Streamlit App")
st.write("Welcome to my app!")

# Set up the two columns
col1, col2 = st.columns(2)

# Column 1
with col1:
    st.header("Column 1")
    col1_left, col1_right = st.columns(2)
    contract = col1_left.selectbox("Select a contract", ["Contract A", "Contract B", "Contract C"], key="contract_select")
    clause = col1_right.selectbox("Select a clause", ["Clause 1", "Clause 2", "Clause 3"], key="clause_select")

    # Add "Prev" and "Next" buttons
    if col1.button("Prev"):
        pass  # Replace "pass" with your code for going to the previous contract/clause
    
    st.text_area("", value = 'para1', height=100, key="para1")
    st.divider()
    st.text_area("", value = 'para2', height=100, key="para2")
    st.divider()
    st.text_area("", value = 'para3', height=100, key="para3")
    
    if col1.button("Next"):
        pass  # Replace "pass" with your code for going to the next contract/clause



# Column 2
with col2:
    st.header("Column 2")
    st.text_area("", value = 'chat area', height=400, key="chat")