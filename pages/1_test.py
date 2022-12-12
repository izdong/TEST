import streamlit as st
from modules.formater import Title, Footer
# from modules.importer import DataImport

title = "1_test"
t = Title().page_config(title)
f = Footer()

st.write('test 1')