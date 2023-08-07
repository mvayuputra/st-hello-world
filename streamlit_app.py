import streamlit as st
st.write("hello world")
number = st.slider("Pick a number", 0, 100)
st.write(number+5)
