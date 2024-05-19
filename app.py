import streamlit as st
import numpy as np
import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__),'data', 'Municipalities_with_topo.csv'))

# Lista de variables
#vars = df.columns[5:]
#vars
#table = df.groupby(by="CVE_ENT")['tri1k_mean'].mean().reset_index()

#if st.checkbox('Show dataframe'):
#df.columns
st.dataframe(df)
