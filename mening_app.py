#Import 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pickle as pkl
from sklearn.preprocessing import MinMaxScaler

st.header("MENINGITIS PREDICTION SYSTEM")


model = pkl.load(open('model_pkl_1','rb'))
gender = st.sidebar.text_input('Input gender of applicant, either male or female')
age = st.sidebar.number_input("Input the patient's age")
settlement = st.sidebar.text_input('Input the patients settlement, either rural or urban')
season = st.sidebar.text_input('Input season either winter or summer')
age_group = st.sidebar.text_input('Input the age group of the patient either, child, adult or old')
geo_pol = st.sidebar.text_input('Input geo political zone of the patient either north_central, north_west, north east')

sex = None
if gender.lower() == 'male' :
    sex = 1
elif gender.lower() == 'female' :
    sex = 0
else :
    sex = "Incorrect Input"

sec = None
if settlement.lower() == 'rural' :
    sec = 0
elif settlement.lower() == 'urban' :
    sec = 1
else :
    sec = "Incorrect Input"

hsec = None
if season.lower() == 'winter' :
    hsec = 0
elif season.lower() == 'summer' :
    hsec = 1
else :
    hsec = "Incorrect Input"

hsec_s_science = None
hsec_s_Commercial = None
hsec_s_arts = None
if geo_pol.lower() == 'north_east' :
    hsec_s_science = 1
    hsec_s_Commercial = 0
    hsec_s_arts = 0
elif geo_pol.lower() == 'north_west' :
    hsec_s_science = 0
    hsec_s_Commercial = 1
    hsec_s_arts = 0
elif geo_pol.lower() == 'north_central' :
    hsec_s_science = 0
    hsec_s_Commercial = 1
    hsec_s_arts = 0
else :
    hsec_s_science = "Invalid Input"
    hsec_s_Commercial = "Invalid Input"
    hsec_s_arts = "Invalid Input"

college_t_science = None
college_t_management = None
college_t_others = None
if  age_group.lower() == 'child' :
    college_t_science = 1
    college_t_management = 0
    college_t_others = 0
elif age_group.lower() == 'adult' :
    college_t_science = 0
    college_t_management = 1
    college_t_others = 0
elif age_group.lower() == 'old' :
    college_t_science = 0
    college_t_management = 0
    college_t_others = 1
else :
    college_t_science = 'Invalid Input'
    college_t_management = 'Invalid Input'
    college_t_others = 'Invalid Input'

data = pd.DataFrame()
data['gender'] = [sex]
data['age'] = [age]
data['settlement'] = [sec]
data['season'] = [hsec]
data['north_central'] = [hsec_s_arts]
data['north_west'] = [hsec_s_Commercial]
data['north_east'] = [hsec_s_science]
data['adult'] = [college_t_management]
data['old'] = [college_t_others]
data['child'] = [college_t_science]


st.success("The data to use for prediction")

st.write(data)

st.success("Meningitis prediction below")
if model.predict(data) == 1 :
    st.write("The patient has meningitis")
else :
    st.write("congrats no mening")


st.success("Probability of having meningitis")
st.write(f'probability of  having meningitis is {model.predict_proba(data)[:,1]}')