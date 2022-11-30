import streamlit as st
import pandas as pd

data = {
    'Series-1': [1,2,3,4,5,6],
    'Series-2':[10,30,100,250, 120, 300]
}

# création du DataFrame
df = pd.DataFrame(data=data)


st.title('App avec Streamlit')
st.subheader('Présentation d\'un dashboard')
st.write('''Ceci est ma première application avec streamlit.
         Profitez du moment
         ''')
st.write(df) # fait apparaître le tableau à partir du df
st.line_chart(df) # fait apparaître un graph ligne
st.area_chart(df) # graph de zones

# création d'un slide conversion celsius en Fahrenheit
my_slider = st.slider('Celsius')
st.write(my_slider, 'in Farenheit is ', my_slider*9/5+32)