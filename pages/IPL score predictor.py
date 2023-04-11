import streamlit as st
# import webbrowser
st.title('IPL Score Predictor')
# url = 'https://ipl-score-predictor-xn20.onrender.com/'
# if st.button('Open Score Predictor'):
#     webbrowser.open_new_tab(url)

import streamlit as st

url = 'https://ipl-score-predictor-xn20.onrender.com/'

st.markdown(f'''
<a href={url}><button style="background-color:White;">Score Predictor</button></a>
''',
unsafe_allow_html=True)