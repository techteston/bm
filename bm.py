#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np

# In[ ]:


st.set_page_config(page_title='NPI with Bass',page_icon=":tada:",layout="wide")

st.title('NPI Forecasts using Bass Diffusion Model')
st.write("This model helps forecast the sales for a new product using the Bass Diffusion Model")

st.subheader('Enter the Parameters')
st.write("These Parameters control the sales per period")

st.subheader('The Sales Profile')

st.subheader('The Sales Data')

