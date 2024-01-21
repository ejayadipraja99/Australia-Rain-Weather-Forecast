import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load Model
with open('pipeline.pkl', 'rb') as file_1:
    pipeline = pickle.load(file_1)

def run():
    # Create Form
    with st.form('Form_rain_prediction'):
        st.title('Rain Prediction')
        location = st.text_input('Location', value='', help='Cobar,CoffsHarbour, Moree, NorfolkIsland, Sydney,SydneyAirport, WaggaWagga, Williamtown,Canberra, Sale,MelbourneAirport, Melbourne, Mildura, Portland, Watsonia,Brisbane,Cairns,Townsville,MountGambier,Nuriootpa,Woomera,PerthAirport,Perth, Hobart,AliceSprings,Darwin')
        maxtemp = st.number_input('MaxTemp',
                                  min_value=7,
                                  max_value=48,
                                  help='Degree Celsius')
        rainfall =st.number_input('Rainfall',
                                  min_value=0,
                                  max_value=183,
                                  help='Milimeters')
        evaporation = st.number_input('Rainfall',
                                  min_value=0,
                                  max_value=81,
                                  help='Milimeters')
        sunshine = st.number_input('Sunshine',
                                  min_value=0,
                                  max_value=14,
                                  help='Hours')
        windgustdir = st.text_input('WindGustDir', value='', help='16 compass point (N,S,W,E)')
        windgustspeed = st.number_input('WindGustSpeed',
                                  min_value=0,
                                  max_value=14,
                                  help='Kilometers per hour')
        winddir9am = st.text_input('WindDir9am', value='', help='Compass point(N,S,W,E)')
        winddir3pm = st.text_input('WindDir3pm', value='', help='Compass point(N,S,W,E)')
        humidity9am = st.slider('Humidity9am',0,100,0)
        humidity3pm = st.slider('Humidity3pm',0,100,0)
        pressure9am = st.number_input('Pressure9am',
                                  min_value=980,
                                  max_value=1040,
                                  help='Hectopascals')
        pressure3pm = st.number_input('Pressure3pm',
                                  min_value=978.2,
                                  max_value=1037.3,
                                  help='Hectopascals')
        cloud9am = st.slider('Cloud9am',0,8,0)
        cloud3pm = st.slider('Cloud3pm',0,8,0)
        temp3pm = st.number_input('Temp3pm',
                                  min_value=4.3,
                                  max_value=46.1,
                                  help='Degree Celsius')
        raintoday = st.radio('RainToday',['No','Yes'])
        raintomorrow =  st.slider('RainTomorrow',0,1,0)
        st.markdown('---')
        submitted = st.form_submit_button('Predict Rain')

    data_inf ={ 
        'Location': location,
        'MaxTemp': maxtemp,
        'Rainfall': rainfall,
        'Evaporation':evaporation,
        'Sunshine': sunshine,
        'WindGustDir': windgustdir,
        'WindGustSpeed': windgustspeed,
        'WindDir9am': winddir9am,
        'WindDir3pm': winddir3pm, 
        'Humidity9am': humidity9am,
        'Humidity3pm':humidity3pm,
        'Pressure9am':pressure9am,
        'Pressure3pm':pressure3pm,
        'Cloud9am': cloud9am,
        'Cloud3pm': cloud3pm,
        'Temp3pm': temp3pm,
        'RainToday': raintoday,
        'RainTomorrow': raintomorrow
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)


    if submitted:
        # Predict
        y_inf_pred = pipeline.predict(data_inf)

        st.write('Prediction Rain Tomorrow : ',str(int(y_inf_pred)))
        st.write('1 = Yes it rains and 0 = No rain ')

if __name__=='__main__':
    run()