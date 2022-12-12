import streamlit as st
from modules.formater import Title, Footer
# from modules.importer import DataImport

title = "start page"
t = Title().page_config(title)
f = Footer()

col1, col2 = st.columns(2)
with col1:
    st.markdown("<h4 style='text-align: center;'>Accuracy</h4>", unsafe_allow_html=True)
with col2:
    container1 = st.container()
    with container1:
        st.markdown("<h4 style='text-align: center;'>Transaction</h4>", unsafe_allow_html=True)
    container2 = st.container()
    with container2:
        st.markdown("<h4 style='text-align: center;'>Wood Type</h4>", unsafe_allow_html=True)
        tab1, tab2= st.tabs(["Percent", "Amount"])
        with tab1:
            st.markdown("<h4 style='text-align: center;'>1</h4>", unsafe_allow_html=True)
        with tab2:
            st.markdown("<h4 style='text-align: center;'>2</h4>", unsafe_allow_html=True)