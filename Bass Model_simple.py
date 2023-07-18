#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go


# In[2]:


def bass_model(p, q, M, periods=1024):
    """
    Implementation of the Bass model for product adoption.
    
    Parameters:
        p (float): Coefficient of innovation.
        q (float): Coefficient of imitation.
        M (int): Total potential market.
        periods (int): Number of time periods to consider. Default is 50.
        
    Returns:
        df (pandas.DataFrame): DataFrame with 'Sales in Period' and 'Cumulative Sales' for each time period.
    """
    # Initialize lists to store sales and cumulative sales
    S_t = [p * M]
    N_t = [p * M]

    # Calculate S(t) and N(t) for each period
    for t in range(2, periods+1):
        S = M * (p + (q * N_t[t-2]) / M) * (1 - N_t[t-2] / M)
        N = N_t[t-2] + S

        S_t.append(S)
        N_t.append(N)
        
    # Create DataFrame
    df = pd.DataFrame({
        'Period': np.arange(1, periods+1),
        'Sales in Period': S_t,
        'Cumulative Sales': N_t
    })
    df = df[df["Sales in Period"] > 0.5]
    df["Sales in Period"] = df["Sales in Period"].astype(int)
    df["Cumulative Sales"] = df["Cumulative Sales"].astype(int)
    return df


# Test the function with p = 0.4, q = 0.15, and M = 16000
df = bass_model(0.4, 0.15, 10000)


# In[3]:




# Create a figure with secondary y-axis
fig = go.Figure()

# Add 'Sales in Period' as a bar chart to the primary y-axis
fig.add_trace(go.Bar(
    x=df["Period"],
    y=df["Sales in Period"],
    name='Sales in Period'
))

# Add 'Cumulative Sales' as a line chart to the secondary y-axis
fig.add_trace(go.Scatter(
    x=df["Period"],
    y=df["Cumulative Sales"],
    name='Cumulative Sales',
    yaxis='y2'
))

# Update layout to include the secondary y-axis
fig.update_layout(
    yaxis2=dict(
        title='Cumulative Sales',
        overlaying='y',
        side='right'
    ),
    yaxis=dict(
        title='Sales in Period'
    )
)

fig.show()

