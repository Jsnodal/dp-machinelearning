import streamlit as st
import pandas as pd

st.title('🎈 MachineLearning App')

st.info('This is app builds a machine leaning model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  data = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  data

  st.write('**X**')
  X = data.drop('species',axis = 1)
  X

  st.write('**y**')
  y = data.species
  y

with st.expander('Data Visualization'):
  st.scatter_chart(data = df, X = 'bill_length_mm',y= 'body_mass_g', color = 'species')
  
