
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Assuming df_sample is the dataframe loaded from the file
df_sample = pd.read_csv('Imports_Exports_Dataset.csv')  
category_data = df_sample['Category'].value_counts()

# Set up the Streamlit dashboard
st.title('Category and Value Data Dashboard')

# Sidebar filters
st.sidebar.header('Filter Data')

# Category filter
categories = st.sidebar.multiselect(
    'Select Category',
    options=df_sample['Category'].unique(),
    default=df_sample['Category'].unique()
)

# Date range filter
min_date = pd.to_datetime(df_sample['Date'], format='%d-%m-%Y').min()
max_date = pd.to_datetime(df_sample['Date'], format='%d-%m-%Y').max()
selected_dates = st.sidebar.date_input(
    'Select Date Range',
    [min_date, max_date]
)

# Filter the dataframe based on user input
df_filtered = df_sample[
    (df_sample['Category'].isin(categories)) &
    (pd.to_datetime(df_sample['Date'], format='%d-%m-%Y') >= pd.to_datetime(selected_dates[0])) &
    (pd.to_datetime(df_sample['Date'], format='%d-%m-%Y') <= pd.to_datetime(selected_dates[1]))
]


# Bar Chart: Frequency of Categories
st.subheader('Bar Chart: Frequency of Categories')
category_data = df_filtered['Category'].value_counts()
fig_bar = px.bar(category_data, x=category_data.index, y=category_data.values, labels={'x':'Category', 'y':'Frequency'}, 
                 color=category_data.index, title="Bar Chart of Category")
st.plotly_chart(fig_bar)

# Pie Chart: Distribution of Categories
st.subheader('Pie Chart: Distribution of Categories')
fig_pie = px.pie(df_filtered, names='Category', title='Pie Chart of Category', hole=0.3, 
                 color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig_pie)

# Histogram: Distribution of Values
st.subheader('Histogram: Distribution of Values')
fig_hist = px.histogram(df_filtered, x='Value', nbins=20, title='Histogram of Value', color_discrete_sequence=['lightblue'])
st.plotly_chart(fig_hist)

# Scatter Plot: Weight vs Value
st.subheader('Scatter Plot: Weight vs Value')
fig_scatter = px.scatter(df_filtered, x='Weight', y='Value', color='Category', title='Scatter Plot: Weight vs Value',
                         labels={'Weight': 'Weight', 'Value': 'Value'})
st.plotly_chart(fig_scatter)

# Line Plot: Quantity Over Time (with proper Date conversion)
st.subheader('Line Plot: Quantity Over Time')
df_filtered['Date'] = pd.to_datetime(df_filtered['Date'], format='%d-%m-%Y')
fig_line = px.line(df_filtered, x='Date', y='Quantity', title='Line Plot: Quantity Over Time', markers=True, 
                   color_discrete_sequence=['orange'])
fig_line.update_layout(xaxis_title='Date', yaxis_title='Quantity', xaxis=dict(tickformat='%d-%m-%Y'))
st.plotly_chart(fig_line)

# Box-and-Whisker Plot for 'Value'
st.subheader('Box-and-Whisker Plot: Distribution of Value')
fig_box = px.box(df_filtered, y='Value', title='Box-and-Whisker Plot: Distribution of Value', 
                 color_discrete_sequence=['lightgreen'])
fig_box.update_traces(boxmean=True, marker_color='green', marker_size=6, line_color='green', 
                      whiskerwidth=0.8)
fig_box.update_layout(yaxis_title='Value', showlegend=False)
st.plotly_chart(fig_box)
