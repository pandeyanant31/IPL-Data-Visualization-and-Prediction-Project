import streamlit as st
import webbrowser
st.title('IPL Score Predictor')
url = 'https://ipl-score-predictor-xn20.onrender.com/'
if st.button('Open Score Predictor'):
    webbrowser.open_new_tab(url)