


#.........................................

import streamlit as st
import pandas as pd
import joblib


# =========================================================
# LOAD MODEL
# =========================================================

saved_data = joblib.load("random_forest.pkl")

model = saved_data["model"]
scaler = saved_data["scaler"]
feature_columns = saved_data["feature_columns"]
category_options = saved_data["category_options"]


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="MediClaim",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    st.title("🏥 MediClaim")
    st.write("Health Insurance Claim Prediction")
    
    st.divider()
    
    st.subheader("About")
    st.write(
        "MediClaim estimates the expected health insurance "
        "claim amount based on the information provided."
    )


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================
   REMOVE STREAMLIT TOP BAR
========================================= */

header[data-testid="stHeader"] {
    background-color: transparent !important;
    height: 0rem !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

[data-testid="stDecoration"] {
    display: none !important;
}


/* =========================================
   MAIN PAGE
========================================= */

.stApp {
    background-color: #f4f6f9;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =========================================
   TITLE
========================================= */

.title {
    font-size: 38px;
    font-weight: 700;
    color: #172554;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 15px;
    margin-bottom: 25px;
}


/* =========================================
   INFORMATION BOX
========================================= */

.info-box {
    background-color: #ffffff;
    padding: 16px 20px;
    border-radius: 10px;

    border-left: 4px solid #008f83;

    color: #475569;

    margin-bottom: 25px;
}


/* =========================================
   SECTION HEADINGS
========================================= */

.section {
    color: #172554;
    font-size: 19px;
    font-weight: 700;

    margin-top: 25px;
    margin-bottom: 12px;
}


/* =========================================
   TEXT INPUTS
========================================= */

div[data-baseweb="input"] {
    background-color: #808080 !important;

    border: 1px solid #d7e4f7 !important;

    border-radius: 7px !important;
}

div[data-baseweb="input"] input {
    background-color: #808080 !important;

    color: #172554 !important;
}


/* =========================================
   SELECT BOXES
========================================= */

div[data-baseweb="select"] > div {
    background-color: #808080 !important;

    border: 1px solid #d7e4f7 !important;

    border-radius: 7px !important;

    color: #172554 !important;
}


/* =========================================
   SELECTED TEXT
========================================= */

div[data-baseweb="select"] span {
    color: #172554 !important;
}


/* =========================================
   LABELS
========================================= */

label {
    color: #172554 !important;

    font-weight: 600 !important;

    font-size: 13px !important;
}


/* =========================================
   BUTTON
========================================= */


div.stButton > button {
    background-color: #24252d !important;
    color: white !important;
    border: none !important;
    box-shadow: none !important;
    border-radius: 8px !important;
}

div.stButton > button:hover {
    background-color: #24252d !important;
    color: white !important;
    border: none !important;
}



/* =========================================
   RESULT
========================================= */

.result {
    background-color: white;

    padding: 28px;

    border-radius: 12px;

    text-align: center;

    margin-top: 25px;

    box-shadow:
        0px 5px 20px rgba(0, 0, 0, 0.06);
}

.result-label {
    color: #64748b;

    font-size: 13px;

    margin-bottom: 5px;
}

.amount {
    color: #172554;

    font-size: 36px;

    font-weight: 700;
}


/* =========================================
   FOOTER
========================================= */

.footer {
    text-align: center;

    color: #94a3b8;

    font-size: 12px;

    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🏥 MediClaim</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Smart health insurance claim estimation'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# INFORMATION
# =========================================================

st.markdown(
    """
    <div class="info-box">
        Enter the person's personal, health and lifestyle
        information to estimate the expected health insurance
        claim amount.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PERSONAL INFORMATION
# =========================================================

st.markdown(
    '<div class="section">👤 Personal Information</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=30
    )

    sex = st.selectbox(
        "Sex",
        category_options["sex"]
    )

    bmi = st.number_input(
        "BMI",
        min_value=1.0,
        max_value=55.0,
        value=24.0
    )


with col2:

    hereditary_diseases = st.selectbox(
        "Hereditary Diseases",
        category_options["hereditary_diseases"]
    )

    city = st.selectbox(
        "City",
        category_options["city"]
    )

    job_title = st.selectbox(
        "Job Title",
        category_options["job_title"]
    )


# =========================================================
# HEALTH INFORMATION
# =========================================================

st.markdown(
    '<div class="section">🩺 Health Information</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


with col1:

    smoker = st.selectbox(
        "Smoker",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    diabetes = st.selectbox(
        "Diabetes",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )


with col2:

    regular_ex = st.selectbox(
        "Regular Exercise",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    bloodpressure = st.number_input(
        "Blood Pressure",
        min_value=1,
        max_value=250,
        value=75
    )


# =========================================================
# PREDICT BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)


if st.button("Predict Claim Amount"):

    # Create input dataframe
    input_data = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "hereditary_diseases": hereditary_diseases,
        "smoker": smoker,
        "city": city,
        "bloodpressure": bloodpressure,
        "diabetes": diabetes,
        "regular_ex": regular_ex,
        "job_title": job_title
    }])


    # Categorical columns
    categorical_columns = [
        "sex",
        "hereditary_diseases",
        "city",
        "job_title"
    ]


    # Match training categories
    for col in categorical_columns:

        input_data[col] = pd.Categorical(
            input_data[col],
            categories=category_options[col]
        )


    # One-hot encoding
    dummy_data = pd.get_dummies(
        input_data[categorical_columns],
        drop_first=True,
        dtype=int
    )


    # Combine numerical and categorical data
    input_data = pd.concat(
        [
            input_data.drop(
                columns=categorical_columns
            ),
            dummy_data
        ],
        axis=1
    )


    # Match training features
    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )


    # Scale
    scaled_input = scaler.transform(
        input_data
    )


    # Predict
    prediction = model.predict(
        scaled_input
    )[0]


    # Result
    st.html(
        f"""
        <div class="result">
            <div class="result-label">
                ESTIMATED HEALTH INSURANCE CLAIM
            </div>

            <div class="amount">
                ₹ {prediction:,.2f}
            </div>
        </div>
        """
    )


    st.success("Prediction completed successfully.")


    st.caption(
        "This is an estimated claim amount generated by "
        "the trained Random Forest model."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        MediClaim • Health Insurance Claim Prediction
    </div>
    """,
    unsafe_allow_html=True
)


#.......................................

