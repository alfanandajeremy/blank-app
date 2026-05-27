import streamlit as st
import pandas as pd

from services.google_trends import get_google_trends
from services.rss_news import get_news
from services.deepseek_ai import analyze_trends

st.set_page_config(page_title="Indonesia Trend Intelligence")

st.title("🇮🇩 Indonesia Trend Intelligence")

api_key = st.text_input(
    "DeepSeek API Key",
    type="password"
)

if st.button("Cari Trend Terbaru"):

    with st.spinner("Mengambil data trend..."):

        trends = get_google_trends()
        news = get_news()

        combined_text = "\n".join(trends + news)

        result = analyze_trends(
            api_key,
            combined_text
        )

        st.subheader("Top Trend Hari Ini")
        st.write(result)

        st.subheader("Google Trends")
        st.write(trends)

        st.subheader("News Headlines")
        st.write(news)
