FROM python:latest

RUN pip3 install streamlit

COPY app2.py /app/app.py

