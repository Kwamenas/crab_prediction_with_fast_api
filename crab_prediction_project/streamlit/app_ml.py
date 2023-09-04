import streamlit as st
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import joblib
import os
import time


def load_model():
    cwd=os.getcwd()
    #print (cwd)
    os.chdir('../')
    newd=os.getcwd()
    print (newd)
    pipe_destination=os.path.join(newd,"Notebooks and Pipelines","Pipelines")
    model_dest=os.path.join(pipe_destination,"model.joblib")
    model=joblib.load(model_dest)
    org_path=os.path.join(newd,"streamlit")
    os.chdir(org_path)
    return model

#print(new_cwd)




def predict_age(input_data):
    model=load_model()
    prediction=model.predict(input_data)
    return("Age of your crab is :",prediction)


def main():
    st.title("Crab Age Predictor :crab:")
    
    #How to use
    st.sidebar.title("How to use")
    st.sidebar.markdown('1.Adjust Input Parameter on the left side.')
    st.sidebar.markdown('2.Click "Predict" button to initiate the prediction.')
    st.sidebar.markdown('3.Progress bar will display the simulation process.')
    st.sidebar.markdown('4.When Prediction is complete, the results will be displayed below.')

    st.sidebar.title("Input Parameters")

    st.sidebar.markdown('**Length:** Length of Crab')
    Length=st.sidebar.number_input('Length',value=0.0)
    
    st.sidebar.markdown('**Diameter:** Diameter of Crab')
    Diameter=st.sidebar.number_input('Diameter',value=0.0)

    st.sidebar.markdown('**Height:** Height of Crab')
    Height=st.sidebar.number_input('Height',value=0.0)

    st.sidebar.markdown('**Weight:** Weight of Crab')
    Weight=st.sidebar.number_input('Weight',value=0.0)

    st.sidebar.markdown('**Shucked_Weight:** Shucked_Weight of Crab')
    Shucked_Weight=st.sidebar.number_input('Shucked_Weight',value=0.0)

    st.sidebar.markdown('**Viscera_Weight:** Viscera_Weight of Crab')
    Viscera_Weight=st.sidebar.number_input('Viscera_Weight',value=0.0)

    st.sidebar.markdown('**Shell_Weight:** Shell_Weight of Crab')
    Shell_Weight=st.sidebar.number_input('Shell_Weight',value=0.0)

    st.sidebar.markdown('**Sex:** Sex of Crab')
    Sex=st.sidebar.selectbox('Sex',['M','F'])

    input_data={'Length':Length,'Diameter':Diameter,'Height':Height,'Weight':Weight,
          'Shucked_Weight':Shucked_Weight,'Viscera_Weight':Viscera_Weight,
          'Shell_Weight':Shell_Weight,'Sex':Sex}
    data_in=DataFrame(input_data,index=[0])
    

    if st.sidebar.button('Predict'):
        with st.spinner("Predicting > > > > >"):
            progress_bar=st.progress(0)
            for i in range(100):
                time.sleep(0.1)
                progress_bar.progress(i+1)
            
            Age=predict_age(data_in)

            st.subheader('Predicted Age is:?')
            st.write(str Age)








main()
