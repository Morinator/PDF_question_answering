import os

import streamlit as st

from PaperDistiller import PaperDistiller

st.sidebar.image("Img/sidebar_img.jpeg")

papers = [l.split('.')[0] for l in os.listdir("Papers/") if l.endswith('.pdf')]
selectbox = st.sidebar.radio('Which do you want to use?', papers)


distiller = PaperDistiller(selectbox)
distiller.read_or_create_index()

query = "Was sind mögliche Gründe für einen Klärfall?"

st.header("`Paper Distiller`")

st.subheader(f"Question: {query}")
st.info(distiller.query_and_distill(query))

distiller.cache_answers()
