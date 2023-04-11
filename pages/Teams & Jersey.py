import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('Teams_jersey.png')
st.title('Teams and Jersey(Color)')
if st.button('Display the Graph'):
        st.image(imagg, width=None)