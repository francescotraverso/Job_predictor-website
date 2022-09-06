
####### Install #######
# pip install --upgrade google-cloud-storage
# pip install nltk
# pip install spacy==2.3.5
# pip install https://github.com/explosion/spacymodels/releases/download/en_core_we_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
# pip install pyresparser

####### Imports #######

import streamlit as st
from pdf2image import convert_from_bytes
from pyresparser import ResumeParser
#from google.cloud import storage

###################################
######### Streamlit Code ##########
###################################

## Theme
font = 'Open Sans'

## Initial Images

st.image('/Users/sandragomes/Downloads/jb/banner.jpg', output_format="auto")
st.image('/Users/sandragomes/Downloads/jb/question.jpg', output_format="auto")

## First titles

st.subheader("If you're rethinking your career or you're making a move in your labor life, upload your Resume and infer your next ideal Jobs.")
st.subheader('Are you ready to start?')

### 1st User interaction ###

## Choosing one of the Options
options = st.multiselect('What you want to consider for your future?',
     ['Computer Science/IT', 'Design', 'Engineering', 'Finance', 'Management', 'Media', 'Sales', 'Tourism'])

## Create empty space
st.write("##")

#### 2nd User interaction ###

## Upload Button for CV
received_file = st.file_uploader("Upload your Resume as a PDF File:", type="pdf")
button = st.button("Get Your Resume Image")

## Resume Image is Displayed
if button and received_file is not None:
    if received_file.type == "application/pdf":
        images = convert_from_bytes(received_file.read())
        for page in images:
            st.image(page, use_column_width=True)


#### Results ####

## Model's Results is Displayed
#
#
#
#


####################################################
######### Preprocessing Users Information ##########
####################################################

#### Extract Text from User CV ####
if button and received_file is not None:
    if received_file.type == "application/pdf":
        #try:
            file = ResumeParser(received_file).get_extracted_data()
            st.write (f"Experience: {file['experience']}; Skills: {file['skills']}")
        #except:
        #    st.write ("Sorry, we couldn't process your CV!")


import session_info
session_info.show()



## Resume Storage in GoogleCloud
# storage_client = storage.Client()
#bucket_name = "cv-directory"
#bucket = storage_client.create_bucket(bucket_name)

#Connect Streamlit to Google Cloud Storage
#Introduction. ...
#Create a Google Cloud Storage bucket and add a file. ...
#Enable the Google Cloud Storage API. ...
#Create a service account and key file. ...
#Add the key to your local app secrets. ...
#Copy your app secrets to the cloud. ...
#Add google-cloud-storage to your requirements file.
