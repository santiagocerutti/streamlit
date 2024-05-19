import streamlit as st
import numpy as np
import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Municipalities_with_topo.csv'))

# Lista de variables
vars = ['tri1k_mean'	,'tri1k_stde'	,'tri1k_max'	,'vrm1k_mean'	,'vrm1k_stde'	,'vrm1k_max'	,'tpi1k_mean'	,'tpi1k_stde'	,'tpi1k_max'	,'slp1k_mean'	,'slp1k_stde'	,'slp1k_max'	,'rou1k_mean'	,'rou1k_stde'	,'rou1k_max'	,'ele1k_mean'	,'ele1k_stde'	,'ele1k_max']

table = df.groupby(by="CVE_ENT")[vars].mean().reset_index()

#if st.checkbox('Show dataframe'):
#df.columns
st.dataframe(table)
