import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

def run():
    # Create tittle
    st.title('Rain Prediction in Australia')

    # Add Image
    image = Image.open('australia.jpg')
    st.image(image, caption= 'Sydney Opera House in Australia')

    # Create Outline
    st.write(' # Australia Weather Dataset')

    # Create markdown line
    st.markdown('--- ')

    # Show dataframe
    df = pd.read_csv('https://raw.githubusercontent.com/ejayadipraja/dataset_m2/main/Weather_Data.csv')
    st.dataframe(df)

    st.markdown('--- ')

    # Visualization
    st.write(' # Visualization')

    # Create Barplot
    st.write(' ## Rain Tomorrow  ')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='RainTomorrow', data=df)
    st.pyplot(fig)
    st.write('From the plot above, it can be seen that the distribution of the RainTomorrow or target columns data is more than half to `0` data. And the distribution of the data slightly balance.')

if __name__=='__main__':
    run()