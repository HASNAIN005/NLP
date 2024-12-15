import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle

from streamlit import title, button

model = pickle.load(open('.venv/KMEAN.pkl', 'rb'))

st.title("Scikit Learn By Teacher Noor")

Age = st.selectbox(
    "Select Age",
    options=list(range(18, 66))
)

# Average Spend: Float between 5 and 50
Average_Spend = st.slider(
    "Select Average Spend",
    min_value=5.0,
    max_value=50.0,
    value=37.010388,
    step=0.01
)

# Visits per Week: Float between 1 and 7
Visits_per_week = st.slider(
    "Select Visits per Week",
    min_value=1.0,
    max_value=7.0,
    value=1.577059,
    step=0.01
)

# Promotion Interest: Integer between 1 and 10
Promotion_Interset = st.selectbox(
    "Select Promotion Interest",
    options=list(range(1, 11))
)


def Predict_Cluster(Age, Average_Spend, Visits_per_week, Promotion_Interset):
    new_customer = np.array([[Age, Average_Spend, Visits_per_week, Promotion_Interset]])
    predicted_clusters = model.predict(new_customer)

    return  predicted_clusters



if button('Predict'):
    predicted_cluster=Predict_Cluster(Age, Average_Spend, Visits_per_week, Promotion_Interset)

    if predicted_cluster == [0]:
        st.markdown(
            """
            ### 🎉 **Congratulations!**  
            **Reward:** Give him **Loyalty Reward** 🏆  
            Thank you for being a loyal customer!
            """
        )
    elif predicted_cluster == [1]:
        st.markdown(
            """
            ### 🌟 **Great Choice!**  
            **Reward:** Give him **Weekend Warrior Reward** 🎯  
            Enjoy exclusive perks this weekend!
            """
        )
    else:
        st.markdown(
            """
            ### 💸 **Special Offer!**  
            **Reward:** Give him a **Discount on Off Promotion Days** 🛍️  
            Don't miss out on these savings!
            """
        )