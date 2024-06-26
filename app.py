import streamlit as st

st.title('This is title')

st.header('This is header')

st.subheader('This is subheader')

st.text('This is example text')

st.success('This is success')

st.warning('This is warning')

st.info('This is information')

st.error('This is error')

if st.checkbox('Select/UnSelect'): # by default it is false
    st.text('User selected checkbox')
else:
    st.text('User has not selected checkbox')

# radio button

state=st.radio('What is your favourite color',('Red','Blue','Yellow'))        

if state == 'Blue':
    st.success("Thats my favorite color as well")

occupation=st.selectbox('What do you do',('Student','Ai engineer','Vlogger','Youtuber'))   

st.text(f'Selected options is {occupation}')

# button

if st.button('Example'):
    st.info('You clicked it')

st.sidebar.header('This is siderbar header')
st.sidebar.text('Akash Mukherjee ')

