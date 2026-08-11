import streamlit as st
import joblib
import numpy as np

st.set_page_config("SALARY PREDICTION APP" ,page_icon="💼")
st.divider()

st.markdown("<h1 style='text-align: center; color: #2E86C1;'>💼 Salary Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Based on Years of Experience & Job Rate</p>", unsafe_allow_html=True)



years= st.number_input( "Years of Experience",value=1,step=1,min_value=0)
jobrate = st.number_input("Job rate ",value=3.0,step=0.5,min_value=0.0)


x= [years,jobrate]

model= joblib.load("linearmodel.pkl")

st.divider()
predict =  st.button("Predict")
st.divider()

if predict :
    st.balloons()
    X1=np.array([x])
    prediction= model.predict(X1)
    st.success(f"💰 Predicted Annual Salary: ₹ {prediction[0]:,.0f}")








