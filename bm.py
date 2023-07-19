#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
# In[4]:

def bass_model(p, q, M, periods=1024):

    S_t = [p * M]
    N_t = [p * M]

    # Calculate S(t) and N(t) for each period
    for t in range(2, periods+1):
        S = M * (p + (q * N_t[t-2]) / M) * (1 - N_t[t-2] / M)
        N = N_t[t-2] + S

        S_t.append(S)
        N_t.append(N)
        
        if S<0.5:
            break
        
    # Create DataFrame
    df = pd.DataFrame({
        'Period': np.arange(1, t+1),
        'Sales in Period': S_t,
        'Cumulative Sales': N_t
    })
    df = df[df["Sales in Period"] > 0.5]
    df["Sales in Period"] = df["Sales in Period"].astype(int)
    df["Cumulative Sales"] = df["Cumulative Sales"].astype(int)
    return df



st.set_page_config(page_title='NPI with Bass',page_icon=":tada:",layout="wide")

with st.container():
    st.title('NPI Forecasts using Bass Diffusion Model')
    st.write("This model helps forecast the sales for a new product using the Bass Diffusion Model")

with st.container():
    st.write("---")
    st.subheader('Model Parameters')
    st.write("These Parameters control the sales per period")
    # Create three text boxes
    p_col,q_col,M_col = st.columns((1,1,1))
    with p_col:
        p = st.number_input('Coefficient of Innovation', format="%.3f", value=0.1)
    with q_col:
        q = st.number_input('Coefficient of Imitation', format="%.3f", value=0.2)
    with M_col:
        M = st.number_input('Total Potential Sales', value=1000)

    # Check if the inputs are numeric
    if not isinstance(p, (float, np.float64)):
        st.error('Coefficient of Innovation must be a number')
    elif not isinstance(q, (float, np.float64)):
        st.error('Coefficient of Imitation must be a number')
    elif not isinstance(M, (int, np.int64)):
        st.error('Total Potential Sales must be an integer')

    df = bass_model(p, q, M)
        
with st.container():
    st.write("---")
    st.header('NPI Forecast')
    chart_col,table_col = st.columns((2,1))
    
    with chart_col:
        st.subheader('The Forecast Profile')
       
        x = [1, 2, 3, 4, 5]
        y = [6, 7, 2, 4, 5]
        
        p = figure(
            title='simple line example',
            x_axis_label='x',
            y_axis_label='y')
        
        p.line(x, y, legend_label='Trend', line_width=2)
        
        st.bokeh_chart(p, use_container_width=True)

    with table_col:
        st.subheader('The Forecast Data')
        df
        
st.write("---")
        

        


    
