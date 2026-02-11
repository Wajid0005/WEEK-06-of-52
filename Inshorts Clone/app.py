 pip install --upgrade pip

import streamlit as st
from news_api import get_news

st.set_page_config(
    page_title="Inshorts Clone",
    page_icon = "📰",
    layout= "centered"
)

st.title("📰 Inshorts Clone")

articles = get_news()

if "index" not in st.session_state:
    st.session_state.index = 0


article = articles[st.session_state.index]

st.image(article['urlToImage'])

st.header(article['title'])

st.write(article['description'])

col1, col2, col3 =st.columns(3)

with col1:
    if st.button("⬅️ Previous"):
        if st.session_state.index > 0:
            st.session_state.index -= 1

with col2:
    st.link_button("🔗 Read More", article["url"])

with col3:
    if st.button("Next ➡️"):
        if st.session_state.index < len(articles) - 1:
            st.session_state.index += 1

st.markdown("---")
st.caption("Made by Wajid Iqbal")


