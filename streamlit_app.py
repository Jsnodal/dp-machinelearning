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
  st.scatter_chart(data , x = 'bill_length_mm',y= 'body_mass_g', color = 'species')
  
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island',('Biscore','Dream','Torgersen'))
  gender = st.selectbox('Gender',('male','female'))
  bill_length_mm = st.slider('Bill Length (mm)',32.1,59.6,43.9)
  bill_depth_mm = st.slider('Bill Length (mm)', 13.1,21.5,17.2)
  Flipper_length_mm = st.slider('Flipper length(mm)',172.0,231.0,201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0,6300.0,4207.0)
  gender = st.selectbox('Gender',('male','female'))

  data = {
    'island': island,
    'bill_length_mm':bill_length_mm,
    'bill_depth_mm':bill_depth_mm,
    'Flipper_length_mm':Flipper_length_mm,
    'body_mass_g':body_mass_g,
    ' gender': gender 
  }

  input_data = pd.DataFrame(data, index = [0])
  input_penguins = pd.concat([input_df,X], axis = 0)

with st.expander('Input features'):
  st.write('**Input penguin**')
  input_df
  st.write('**combinedpenguins data**')
  input_penguins

encode = ['island','gender']
data_penguina =pd.get_dummies(input_penguins, prefix = encode)






  
