import os
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import  Image
import base64
#import matplotlib.pyplot as plt
#from matplotlib import pyplot

from multipage import MultiPage
from pages import generate_page, home # import your pages here

# Create an instance of the app 
app = MultiPage()

st.markdown("""# Welcome to the GANdy Warhol project!""")

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

bin_str = get_base64_of_bin_file('design/colorful-plants-abstract-painting-art-website-header.jpeg')
CSS = """
.stApp {
    background-image: url("data:image/png;base64,%s");
    background-repeat: no-repeat;
    background-position: top;
    background-size: cover;
    background-size: 1500px 111px;
}
""" % bin_str
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

# Add all your application here
app.add_page("Generate Images", generate_page.app)
app.add_page("Home Page", home.app)

app.run()