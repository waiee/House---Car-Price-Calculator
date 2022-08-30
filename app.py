import streamlit as st
from PIL import Image

st.title("House & Car Price Calculator")
salary = st.number_input("Enter your salary (RM)")

#find dsr
dsr = 1
if salary < 3000:
    dsr = dsr*salary*0.60
elif salary > 5000:
    dsr = dsr*salary*0.75
else:
    dsr = dsr*salary*0.70

st.success(f"""Salary: RM {salary} 
            \nDSR (Debt Service Ratio): RM {dsr}""")

#find commitment
bankCom = st.number_input("Enter your bank commitment (Car, personal loan etc.)")
totalLoan = dsr - bankCom

#Hide streamlit trademark
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
 