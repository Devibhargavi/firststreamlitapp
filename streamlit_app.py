import streamlit
streamlit.title('My mom\'s new healthy diner')
streamlit.header('Breakfast favourites')
streamlit.text('🥣 omega 3 & bluebeery oatmeal')
streamlit.text('🥗 kale, spinach & rocket smoothie')
streamlit.text('🐔 Hard boiled free range Egg')
streamlit.text('🥑🍞 Avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
