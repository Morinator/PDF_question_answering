import os

import streamlit as st

from PaperDistiller import PaperDistiller

# create page
st.title("Paper Distiller")
st.sidebar.image("https://uploads-eu-west-1.insided.com/xentral-en/attachment/7eb5a51d-1457-4db1-ae76-7b51d36ea392_thumb.png")
papers = [l.split('.')[0] for l in os.listdir("Papers/") if l.endswith('.pdf')]
select_box = st.sidebar.radio('Select a PDF', papers)
st.header("`Paper Distiller`")
query = st.text_input("Ask a question about the paper!", "What is the main idea?")

# create distiller object
distiller = PaperDistiller(select_box)
distiller.read_or_create_index()

# show and cache answer
st.info(distiller.query_and_distill(query), icon="💡")
distiller.cache_answers()
