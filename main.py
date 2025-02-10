import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title='predection of outbreaks of diseases' , page_icon='doctor' , layout='wide')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to models
diabetes_model = pickle.load(open(os.path.join(BASE_DIR, 'models', 'diabetes_model.sav'), 'rb'))
parkinsons_model = pickle.load(open(os.path.join(BASE_DIR, 'models', 'parkinsons_model.sav'), 'rb'))
heart_model = pickle.load(open(os.path.join(BASE_DIR, 'models', 'heart_model.sav'), 'rb'))

# diabetes_model = pickle.load(open('models\diabetes_model.sav' , 'rb'))
# parkinsons_model = pickle.load(open('models\parkinsons_model.sav' , 'rb'))
# heart_model = pickle.load(open('models\heart_model.sav' , 'rb'))

with st.sidebar :
    selected = option_menu('predection of disease outbreak system' , ['Heart Disease Predection' , 'Diabetes predections' , 'Parkinson predection'] , menu_icon='hospital-fill' , icons=['activity' , 'heart' , 'person'], default_index=0)

if selected == 'Diabetes predections':
    st.title('Diabetes Predictions using ML')

    # Define the columns
    col1, col2, col3 = st.columns(3)

    with col1:
        pregenacies = st.number_input("Number of Pregnancies")
        SkinThickness = st.number_input("Skin Thickness Value")
        DiabetestPredigreefunction = st.number_input('Diabetes Pedigree Function Value')

    with col2:
        Glucose = st.number_input('Glucose level')
        Insulin = st.number_input('Insulin Level')
        Age = st.number_input('Age of the person')

    with col3:
        BloodPressure = st.number_input('Blood Pressure value')
        BMI = st.number_input('BMI value')

    # Button and prediction logic
    diabetes_diagonis = ''
    if st.button('Diabetes test Result'):
        user_input = [pregenacies , Glucose , BloodPressure , SkinThickness , Insulin , BMI , DiabetestPredigreefunction , Age]

        user_input = [float(x) for x in user_input]
        diabetes_predection = diabetes_model.predict([user_input])
        if diabetes_predection[0] == 1:
            diabetes_diagonis = 'the person is diabetics'
        else:
            diabetes_diagonis = 'THe person is not Dibetics'
        st.success(diabetes_diagonis)





if selected == 'Parkinson predection':
    st.title("Parkinson's Disease Prediction")

    # Define the columns for input
    col1, col2, col3 = st.columns(3)

    # Column 1
    with col1:
        name = st.number_input("Name of the patient")
        MDVP_Fo = st.number_input("Fundamental Frequency (MDVP:Fo) in Hz")
        MDVP_Fhi = st.number_input("Maximum Frequency (MDVP:Fhi) in Hz")
        MDVP_Flo = st.number_input("Minimum Frequency (MDVP:Flo) in Hz")
        MDVP_Jitter = st.number_input("Jitter (%)")
        MDVP_Jitter_Abs = st.number_input("Jitter (Abs)")

    # Column 2
    with col2:
        MDVP_RAP = st.number_input("Relative Average Perturbation (MDVP:RAP)")
        MDVP_PPQ = st.number_input("Pitch Period Quotient (MDVP:PPQ)")
        Jitter_DDP = st.number_input("Jitter Difference of Successive Periods (Jitter:DDP)")
        MDVP_Shim = st.number_input("Shimmer (MDVP:Shimmer)")
        MDVP_Shim_dB = st.number_input("Shimmer in dB (MDVP:Shimmer(dB))")
        Shimmer_APQ3 = st.number_input("Shimmer:APQ3")

    # Column 3
    with col3:
        Shimmer_APQ5 = st.number_input("Shimmer:APQ5")
        MDVP_APQ = st.number_input("MDVP:APQ")
        Shimmer_DDA = st.number_input("Shimmer:DDA")
        NHR = st.number_input("Noise-to-Harmonics Ratio (NHR)")
        HNR = st.number_input("Harmonics-to-Noise Ratio (HNR)")
        RPDE = st.number_input("Recurrence Period Density Entropy (RPDE)")


    # Additional features
    with col1:
        DFA = st.number_input("Detrended Fluctuation Analysis (DFA)")
        Spread1 = st.number_input("Spread1")
        Spread2 = st.number_input("Spread2")

    with col2:
        D2 = st.number_input("Fractal Dimension (D2)")
        PPE = st.number_input("Probability of Periodic Events (PPE)")

    parkinson_diagonis = ''
    if st.button('parkinson test Result'):
        user_input = [MDVP_Fo ,MDVP_Fhi , MDVP_Flo , MDVP_Jitter , MDVP_Jitter_Abs , MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shim,MDVP_Shim_dB,Shimmer_APQ3 , Shimmer_APQ5 ,  MDVP_APQ , Shimmer_DDA ,  NHR , HNR , RPDE , DFA , Spread1 ,  Spread2 , D2 , PPE]

        user_input = [float(x) for x in user_input]
        parkinson_predection = parkinsons_model.predict([user_input])
        if parkinson_predection[0] == 1:
            parkinson_diagonis = 'the person has Parkinson'
        else:
            parkinson_diagonis = 'The person is has no Parkinson'
        st.success(parkinson_diagonis)



if selected == 'Heart Disease Predection':
    st.title('Heart Disease Prediction using ML')

    # Define the columns
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=1)
        trestbps = st.number_input("Resting Blood Pressure", min_value=1)
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl (1 for Yes, 0 for No)", min_value=0, max_value=1)
        restecg = st.number_input("Resting Electrocardiographic Results (0 for Normal, 1 for Abnormal)", min_value=0, max_value=1)
        thalach = st.number_input("Maximum Heart Rate Achieved", min_value=1)

    with col2:
        sex = st.number_input("Sex (1 for Male, 0 for Female)", min_value=0, max_value=1)
        cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)
        chol = st.number_input("Serum Cholesterol Level", min_value=1)
        exang = st.number_input("Exercise Induced Angina (1 for Yes, 0 for No)", min_value=0, max_value=1)
        oldpeak = st.number_input("Depression Induced by Exercise Relative to Rest", min_value=0.0, step=0.1)

    with col3:
        slope = st.number_input("Slope of Peak Exercise ST Segment (0 for Upsloping, 1 for Flat, 2 for Downsloping)", min_value=0, max_value=2)
        ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy (0-3)", min_value=0, max_value=3)
        thal = st.number_input("Thalassemia (0 for Normal, 1 for Fixed Defect, 2 for Reversible Defect)", min_value=0, max_value=2)

       
    heart_diagonis = ''
    if st.button('heart test Result') :
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
        user_input = [float(x) for x in user_input]
        heart_predection = heart_model.predict([user_input])
        if heart_predection[0] == 1:
            heart_diagonis = 'the person has heart disease'
        else:
            heaart_diagonis = 'The person  has no heart disease'
        st.success(heart_diagonis)
