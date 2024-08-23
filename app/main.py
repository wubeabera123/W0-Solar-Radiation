import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Title of the dashboard
st.title('Exploratory Data Analysis for Solar Installation in Benin, Sierra Leone, and Togo')

# Sidebar for user input
st.sidebar.header('Countries')
option = st.sidebar.selectbox('Select country:', ["Benin", "Sierra Leone", "Togo"])

# Display the selected option
st.write('You selected:', option)

# Generate some random data for demonstration purposes
np.random.seed(42)
if option == 'Benin':
    data = {
        'Year': pd.date_range(start='2015', periods=9, freq='Y'),
        'GHI': np.random.randint(300, 500, 9),
        'DNI': np.random.randint(150, 300, 9),
        'DHI': np.random.randint(100, 250, 9),
        'Tamb': np.random.randint(25, 35, 9)
    }
elif option == 'Sierra Leone':
    data = {
        'Year': pd.date_range(start='2015', periods=9, freq='Y'),
        'GHI': np.random.randint(200, 400, 9),
        'DNI': np.random.randint(120, 250, 9),
        'DHI': np.random.randint(80, 200, 9),
        'Tamb': np.random.randint(20, 30, 9)
    }
else:  # Togo selected
    data = {
        'Year': pd.date_range(start='2015', periods=9, freq='Y'),
        'GHI': np.random.randint(250, 450, 9),
        'DNI': np.random.randint(140, 280, 9),
        'DHI': np.random.randint(90, 220, 9),
        'Tamb': np.random.randint(22, 32, 9)
    }

df = pd.DataFrame(data)

# Display the DataFrame
st.write('Solar Installation Data for', option)
st.write(df)

# Display basic statistics using df.describe()
st.write('Basic statistics:')
st.write(df.describe())

# Time series analysis
st.write('### Time Series Analysis')

# Plot the time series data using Plotly for interactive visualization
fig = px.line(df, x='Year', y=['GHI', 'DNI', 'DHI', 'Tamb'], title=f'Time Series Analysis for {option}')

# Display the plot in Streamlit
st.plotly_chart(fig)
