FROM python:latest

RUN pip3 install streamlit joblib sklearn

EXPOSE 8501:8501
WORKDIR /app
COPY app2.py /app/app.py
COPY lrm/model /app/model/

CMD ["streamlit", "run", "app.py"]