import pandas as pd
import numpy as np
import joblib
import streamlit


model = open("model/linear_regression_model.pkl")
lr = joblib.load(model)
