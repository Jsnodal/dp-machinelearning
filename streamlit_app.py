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
  

  data = {
    'island': island,
    'bill_length_mm':bill_length_mm,
    'bill_depth_mm':bill_depth_mm,
    'Flipper_length_mm':Flipper_length_mm,
    'body_mass_g':body_mass_g,
    ' gender': gender 
  }

  input_data = pd.DataFrame(data, index = [0])
  input_penguins = pd.concat([input_data,X], axis = 0)

with st.expander('Input features'):
  st.write('**Input penguin**')
  input_data
  st.write('**combined penguins data**')
  input_penguins

encode = ['species', 'island'] 
data_penguins = pd.get_dummies(input_penguins)


 

# Set page configuration
st.set_page_config(
    page_title="Beautiful Streamlit App",
    page_icon="✨",
    layout="wide",
)

# Sidebar
st.sidebar.title("Navigation")
pages = ["Home", "Data", "Visualize", "About"]
page = st.sidebar.radio("Select a page:", pages)

st.sidebar.write("---")
st.sidebar.write("This is a beautiful Streamlit app. Enjoy exploring!")

# Custom style
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f0f5;
    }
    .sidebar .sidebar-content {
        background-color: #282828;
        color: #f0f0f5;
    }
    .stButton>button {
        background-color: #008CBA;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #005f6b;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if page == "Home":
    st.title("Welcome to the Beautiful Streamlit App ✨")
    st.write("This app demonstrates how to create a beautiful and interactive web app using Streamlit.")
    st.image("https://source.unsplash.com/800x400/?nature,water")  # Sample image from Unsplash

elif page == "Data":
    st.title("Data Section")
    st.write("Here you can view and explore the dataset.")
    
    # Sample data
    data = pd.DataFrame({
        'A': np.random.rand(100),
        'B': np.random.rand(100),
        'C': np.random.rand(100),
    })
    
    st.dataframe(data)

elif page == "Visualize":
    st.title("Visualization Section")
    st.write("Here you can create beautiful visualizations.")
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    
    st.line_chart(chart_data)

elif page == "About":
    st.title("About This App")
    st.write("This app is built with Streamlit to demonstrate how to create beautiful and interactive web applications.")
    st.write("Feel free to explore and customize the code to make it your own!")

# Footer
st.markdown(
    """
    <footer style="text-align:center; padding:10px; position:fixed; bottom:0; width:100%; background-color:rgba(0, 140, 186, 0.9); color:white;">
    Built with ❤️ using Streamlit
    </footer>
    """,
    unsafe_allow_html=True,
)




  
