
import streamlit as st
import json

st.title("Latest AI News")

try:
    with open("news.json", "r") as f:
        news = json.load(f)

    for article in news:
        st.subheader(article["title"])
        st.write(article["description"])
        st.markdown(f"[Read more]({article['url']})")
except FileNotFoundError:
    st.write("No news available yet. Please run the updater script.")
