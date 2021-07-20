import pandas as pd
import numpy as np
import joblib
import streamlit

model = open("./model/linear_regression_model.pkl", "rb")
lr = joblib.load(model)


def lr_prediction(variables):
    pred_arr = np.array(variables)
    preds = pred_arr.reshape(1, -1)
    preds = preds.astype(int)
    mprediction = lr.predict(preds)
    return mprediction


def run():
    streamlit.title("Linear Regression Model")
    html_temp = """
    """
    streamlit.markdown(html_temp)
    variables = [streamlit.text_input("Variable {}".format(i)) for i in range(1, 6)]
    prediction = ""
    if streamlit.button("Predict"):
        prediction = lr_prediction(variables)
    streamlit.success("The prediction by Model: {}".format(prediction))

if __name__ == '__main__':
    run()