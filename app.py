
####### Install #######
# pip install --upgrade google-cloud-storage
# pip install nltk
# pip install spacy==2.3.5
# pip install https://github.com/explosion/spacymodels/releases/download/en_core_we_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
# pip install pyresparser

####### Imports #######

import streamlit as st
import requests

###################################
######### Streamlit Code ##########
###################################



## Theme
font = 'Open Sans'

## Initial Images

st.image('banner.jpg', output_format="auto")
st.image('question.jpg', output_format="auto")

## First titles

st.markdown('''
# Job Predictor
##### If you're rethinking your career or making a move in your work life, describe and find your next ideal jobs.
##
''')


### 1st User interaction ###


## Choosing one of the possible industry options

option = st.selectbox('What you want to consider for your future?',
                        ['Choose career path',
                         'Data Science',
                         'Management',
                         'Marketing',
                         'Sales',
                         'Tourism'])

#option = st.radio('What you want to consider for your future?',
#     ['Computer Science/IT', 'Data Science', 'Management', 'Marketing', 'Sales', 'Tourism'])


if option == 'Data Science':
    area_choice = 'data science'
elif option == 'Management':
    area_choice = 'management'
elif option == 'Marketing':
    area_choice = 'marketing'
elif option == 'Tourism':
    area_choice = 'tourism'
elif option == 'Sales':
    area_choice = 'Tourism'
else:
    area_choice = 0


## Create empty space
st.write("##")

#### 2nd User interaction ###


describe_your_job = st.text_input('Describe your job:', 'Management Consulting in FREESCG - Food Consultant - Management consultancy specialized in food and beverage - Consulting services for restaurants, bars and similar - Project developed with specialization to each client through a diagnosis and an action plan put into practice, with analysis of the obtained results - Areas of expertise: Financial, Logistics, Human Resources, Marketing, Administrative Backoffice, Production and Operation Analysis and Management of Purchasing and Logistics in MADPIZZA - Evaluation, restructuring and monitoring of existing logistics department - Establish two-way communication procedures with an emphasis on motivation and teamwork - Consumption forecast - Supplier assessment, prospecting and monitoring.')
button_2 = st.button('Find your next job!')


if button_2 and describe_your_job is not None and area_choice in ['data science', 'management', 'marketing', 'sales', 'tourism']:


    url_api = 'https://job-predictor-ba4corpqra-no.a.run.app/job_titles'

    params = {
        'describe_your_job': describe_your_job,
        'area_choice': area_choice
    }

    response = requests.get(url=url_api, params=params).json()

    st.write("##")
    st.markdown('''
    ##### Your results:
    ''')

    col1, col2 = st.columns(2)

    list_titles=[]

    with col1:
        job_title_1 = response.get('Job #1').get('Title').title()
        st.info(job_title_1)
        list_titles.append(job_title_1)

        job_title_2 = response.get('Job #2').get('Title').title()
        if job_title_2 not in list_titles:
            st.info(job_title_2)
            list_titles.append(job_title_2)
            jtc_1 = 1
        else:
            jtc_1 = 0

        job_title_3 = response.get('Job #3').get('Title').title()
        if job_title_3 not in list_titles:
            st.info(job_title_3)
            list_titles.append(job_title_3)
            jtc_2 = 1
        else:
            jtc_2 = 0

        job_title_4 = response.get('Job #4').get('Title').title()
        if job_title_4 not in list_titles:
            st.info(job_title_4)
            list_titles.append(job_title_4)
            jtc_3 = 1
        else:
            jtc_3 = 0

        job_title_5 = response.get('Job #5').get('Title').title()
        if job_title_5 not in list_titles:
            st.info(job_title_5)
            jtc_4 = 1
        else:
            jtc_4 = 0



    with col2:
        prox_sc_1 = str(response.get('Job #1').get('Proximity Score')) + ' % match'
        st.info(prox_sc_1)

        prox_sc_2 = str(response.get('Job #2').get('Proximity Score')) + ' % match'
        if jtc_1 == 1:
            st.info(prox_sc_2)


        prox_sc_3 = str(response.get('Job #3').get('Proximity Score')) + ' % match'
        if jtc_2 == 1:
            st.info(prox_sc_3)


        prox_sc_4 = str(response.get('Job #4').get('Proximity Score')) + ' % match'
        if jtc_3 == 1:
            st.info(prox_sc_4)


        prox_sc_5 = str(response.get('Job #5').get('Proximity Score')) + ' % match'
        if jtc_4 == 1:
            st.info(prox_sc_5)

    st.write("#####")
    st.write("Thank you for trusting Job Predictor!")
    st.write("Click here to start your new career! 😉")
    st.image('landing_jobs.jpg', output_format="auto")
    url_janding_jobs = "https://www.landing.jobs/"
    st.write(url_janding_jobs)
