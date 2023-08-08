import streamlit as st
st.write("PRINCE EDUCATION")
number = st.slider("Pick a number", 0, 100)
st.write(number+5)
with st.form("my_form"):
    option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))


   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", optiom)

st.write("Outside the form ",option)
