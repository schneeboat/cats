import streamlit as st
import requests
from PIL import Image
import urllib.request

st.title('Random Cats')
response = requests.get("https://aws.random.cat/meow")
for i,j in response.json().items():
	urllib.request.urlretrieve(j, 'cat')
	img = Image.open('cat')
	(width, height) = (img.width//2,img.height//2)
	st.image(img.resize((width,height), Image.ANTIALIAS))

