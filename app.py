import streamlit as st
from multipage import MultiPage
from pagess import prediction, techinfo

# Creating an instance of the app
app = MultiPage()

# Title of the main page
st.title("Detecting Alzheimer's Disease")

# All pages here
app.add_page("Prediction", prediction.app)
app.add_page("Technical Info", techinfo.app)

# Running the main app
app.run()
