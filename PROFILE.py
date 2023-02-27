import streamlit as st
import os
from matplotlib import image
st.title(":green[PROFILE]")

btn_click = st.button("Click HERE TO SEE MY PROFILE")

if btn_click == True:
    # absolute path to this file
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    # absolute path to this file's root directory
    PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
    # absolute path of directory_of_interest
    dir_of_interest = os.path.join(PARENT_DIR, "resources")
    DATA_PATH = os.path.join(dir_of_interest, "images", "C:\\Users\\NAGENDRA VOORA\\Desktop\\INTERNSHIP\\PROJECT_WORK\\resources\\images\\my_img.jpg")
    images=image.imread(DATA_PATH)
    st.image(images)
    st.subheader(":blue[NAME]")
    st.write("VOORA NAGENDRA BHASKARA SWAMY")
    st.subheader(":blue[QUALIFICATION]")
    st.write("B.TECH CSE 3 rd year")
    st.subheader(":blue[COLLEGE]")
    st.write("RGUKT Srikakulam")
    st.subheader(":blue[AREA OF EXPERTISE]")
    st.write("Python")
    st.write("C")
    st.write("MachineLearning")
    st.write("DataScience")
    st.subheader(":blue[CONTACT DETAILS]")
    st.write("phone number: 9705823166")
    st.write("mail id: vooranagendra1729@gmail.com")
    st.write("linkedin: linkedin/nagendravoora")

st.header(":green[THANKS FOR VISITING THE PAGE]")


