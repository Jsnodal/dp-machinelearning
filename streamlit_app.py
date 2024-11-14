import streamlit as st
import pandas as pd

st.title('🎈 MachineLearning App')

st.info('This is app builds a machine leaning model!')

data = pd.read_csv("https://github.com/dataprofessor/palmer-penguins/commit/4dbd79d6ae9f5f97ec9682e79e8ce73c150aca1f")
data
