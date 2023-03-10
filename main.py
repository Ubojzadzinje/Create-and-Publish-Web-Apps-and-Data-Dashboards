import streamlit as st
import pandas

data = {'Series_1': [1, 3, 4, 5, 7], 'Series_2': [10, 30, 40, 100, 250]}

df = pandas.DataFrame(data)

st.title("Streamlit app")
st.subheader("Streamlit automate Everything")
st.write(
    """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
""")
st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Fahreneit is', myslider * 9 / 5 + 32)
