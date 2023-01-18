import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
import glob

analyzer = SentimentIntensityAnalyzer()
diary = []

filepaths = glob.glob("diary/*.txt")

for filepath in filepaths:
    date = filepath.split("/")[1].split(".txt")[0]
    with open(filepath, "r") as file:
        content = file.read()
        diary.append((date, content))

diary = sorted(diary)

day = []
pos_scores = []
neg_scores = []

for day_of_week, text in diary:
    day.append(day_of_week.split(".")[1])
    score = analyzer.polarity_scores(text)
    pos_scores.append(score["pos"])
    neg_scores.append(score["neg"])

pos_figure = px.line(x=day, y=pos_scores, labels={"x": "Day of the Week", "y": "Positivity Score"})
neg_figure = px.line(x=day, y=neg_scores, labels={"x": "Day of the Week", "y": "Negativity Score"})

st.title("Daily Tone")

st.subheader("Positivity Scores")
st.plotly_chart(pos_figure)

st.subheader("Negativity Scores")
st.plotly_chart(neg_figure)
