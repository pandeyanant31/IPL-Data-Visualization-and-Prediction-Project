import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('Match_places.png')
st.title('Match Places')
if st.button('Display the Graph'):
        st.image(imagg, width=None)