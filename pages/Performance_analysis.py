import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('Performance_analysis.png')
st.title('Performance Analysis')
if st.button('Display the Graph'):
        st.image(imagg, width=None)