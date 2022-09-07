
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

## Choosing one of the possible industry options
option = st.radio('What you want to consider for your future?',
     ['Computer Science/IT', 'Management', 'Marketing', 'Sales', 'Tourism'])

## Create empty space
st.write("##")

#### 2nd User interaction ###

## Upload Button for CV
received_file = st.file_uploader("Upload your Resume as a PDF File:", type="pdf")
button = st.button("Extract CV information")

## Resume Image is Displayed
if button and received_file is not None:
    if received_file.type == "application/pdf":
        images = convert_from_bytes(received_file.read())
        for page in images:
            st.image(page, use_column_width=True)


####################################################
######### Preprocessing Users Information ##########
####################################################

## Message before the extraction of CV information

st.write("This is the information from your Resume we are going to process:")

#### Extract Text from User CV ####
if button and received_file is not None:
    if received_file.type == "application/pdf":
        try:
            file = ResumeParser(received_file).get_extracted_data()
            st.write (f"Experience: {file['experience']}; Skills: {file['skills']}")
        except:
            st.write ("Sorry, we couldn't process your CV!")


####################################################
################ Model Running #####################
####################################################

# API will run this preprocessing text block, put in the model and we'll have results

####################################################
############ Display Found Results #################
####################################################

## Create one empty space
st.write("##")

### Display Model Results ###

## Introduction text for model results
st.write("Here they are! Your expected results:")

## Results from model
#
#
#
#
#

## Create two empty spaces
st.write("##")
st.write("##")

## Ending message
st.write("Thank you for submitting your Resume!")
