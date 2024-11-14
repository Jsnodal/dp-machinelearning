import streamlit as st
import pandas as pd

st.title('🎈 MachineLearning App')

st.info('This is app builds a machine leaning model!')

data = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
data
