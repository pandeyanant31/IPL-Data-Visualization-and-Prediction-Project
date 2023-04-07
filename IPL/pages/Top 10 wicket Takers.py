import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('top10wkt.png')
st.title('Top 10 wicket takers')
if st.button('Display the Graph'):
        st.image(imagg, width=None)