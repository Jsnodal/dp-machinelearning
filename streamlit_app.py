import streamlit as st
import pandas as pd

st.title('🎈 MachineLearning App')

st.info('This is app builds a machine leaning model!')

data = pd.read_csv("penguins_cleaned.csv")
data
