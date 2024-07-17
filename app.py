import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

with open("C:\\Users\\abhin\\PycharmProjects\\House_Price_Project\\model\\house_price_.pkl", "rb") as f:
    etr=pickle.load(f)
def main():
    st.title('House Price Prediction')


    numbers = [str(i) for i in range(30, 43,1)]
    latitude = st.selectbox('Latitude',numbers)
    long=[str(i) for i in range(-124,-109,1)]
    longitude = st.selectbox('Longitude',long)
    med_age=[str(i) for i in range(0, 53,1)]
    housing_median_age = st.selectbox('Housing Median Age',med_age)
    rooms=[str(i) for i in range(1,10,1)]
    total_rooms = st.selectbox('Total Rooms',rooms)
    bedrooms=[str(i) for i in range(0,10,1)]
    total_bedrooms = st.selectbox('Total Bedrooms',bedrooms)
    pops=[str(i) for i in range(0,10,1)]
    population = st.selectbox('Population',pops)
    house=[str(i) for i in range(1,10,1)]
    households = st.selectbox('Households',house)
    med_in=[str(i) for i in range(0,15,1)]
    median_income = st.selectbox('Median Income',med_in)
    ocean_proximity = st.selectbox('Ocean Proximity', ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])
    bedroom_ratio = float(total_bedrooms) / float(total_rooms)
    household_rooms = float(total_rooms) / float(households)


    if st.button('Predict'):

        input_data = pd.DataFrame({

            'longitude': [longitude],
            'latitude': [latitude],
            'housing_median_age': [housing_median_age],
            'total_rooms': [total_rooms],
            'total_bedrooms': [total_bedrooms],
            'population': [population],
            'households': [households],
            'median_income': [median_income],
            'ocean_proximity_<1H OCEAN': [1 if ocean_proximity == '<1H OCEAN' else 0],
            'ocean_proximity_INLAND': [1 if ocean_proximity == 'INLAND' else 0],
            'ocean_proximity_ISLAND': [1 if ocean_proximity == 'ISLAND' else 0],
            'ocean_proximity_NEAR BAY': [1 if ocean_proximity == 'NEAR BAY' else 0],
            'ocean_proximity_NEAR OCEAN': [1 if ocean_proximity == 'NEAR OCEAN' else 0],
            'bedroom_ratio':[bedroom_ratio],
            'household_rooms':[household_rooms]
        })
        prediction = etr.predict(input_data)
        st.write(f'Predicted House Price: ${prediction}')

if __name__ == '__main__':
    main()
