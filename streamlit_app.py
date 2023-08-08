import streamlit as st
st.write("PRINCE EDUCATION")
with st.form("my_form"):
    option = st.selectbox(
    'prince profession',
    ('killer', 'hunter', 'none of the above'))

    option_two = st.radio(
        'prince character',
        ['good','worse','neutral'])
    scale = st.slider("rating for prince",0,10)
    
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        if option_two == 'good' and option == 'killer':
            st.write('you won')
            st.write('score : ',scale*10)
        else:
            st.write('you lost')
        st.write("slider", option)

st.write("reload for another game ")
