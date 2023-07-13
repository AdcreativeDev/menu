import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('bobo.png'))

st.header('David Cheung, Developer')

st.info('Have fun with ChatGPT')

icon_size = 20
# Import and Query



st_button('medium', 'https://pdf-chat.streamlit.app', '🤖 Pdf Chat', icon_size)
st_button('medium', 'https://simple-docs-chat.streamlit.app', '🤖 Simple Document Chat', icon_size)

st_button('medium', 'https://import-2-vector.streamlit.app', '📥 NewsAPI extraction and query', icon_size)
st_button('medium', 'https://simple-summary.streamlit.app', '📄 Text Summarize ', icon_size)




 
 
 
