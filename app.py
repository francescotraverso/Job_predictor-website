import streamlit as st
import pandas as pd
import numpy as np

st.title('Given my work experience, what jobs should I consider?')

st.subheader('Simply upload your resume to suggest an ideal Data Science job after Le Wagon bootcamp')

st.header('Ready to start?')
st.file_uploader('Upload your resume')
