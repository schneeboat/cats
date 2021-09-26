import streamlit as st
import requests
from PIL import Image
import urllib.request
st.title('Random Cats')
response = requests.get("https://aws.random.cat/meow")
for i,j in response.json().items():
	urllib.request.urlretrieve(j, 'cat')
	st.image(Image.open('cat'))
