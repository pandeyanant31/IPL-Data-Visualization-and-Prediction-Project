import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('top10scorer.png')
st.title('Top 10 Scorer')
if st.button('Display the Graph'):
        st.image(imagg, width=None)