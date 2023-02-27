import streamlit as st
from matplotlib import image
import matplotlib
import os
import pandas as pd
import seaborn

st.title(":red[CAMPAIGN DATA]")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "C:\\Users\\NAGENDRA VOORA\\Desktop\\INTERNSHIP\\PROJECT_WORK\\resources\\data\\Xtrain_Feature.csv")

Data=pd.read_csv(DATA_PATH)
st.dataframe(Data)

col= st.selectbox("Select the COLUMNS:", Data.columns)

st.write(Data[col].describe())



