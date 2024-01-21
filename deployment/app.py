import pandas as pd
import streamlit as st
import eda
import prediction
from PIL import Image
page = st.sidebar.selectbox('Choose Page:', ('Landing Page','Data Exploration','Data Prediction'))

if page == 'Landing Page':
    st.title('Milestone 2')
    st.write('')
    st.write('Name : Erlangga Jayadipraja')
    st.write('Batch : SBY-002')
    st.write('Objective: Create a model to predict whether it will rain tomorrow or not in Australia ')
    st.write('')
    st.write('Please select menu on the left bar !')
    st.write('')
elif page == 'Data Exploration':
    eda.run()
else:
    prediction.run()