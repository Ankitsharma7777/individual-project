
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Assuming df_sample is the dataframe loaded from the file
df_sample = pd.read_csv("path_to_your_file.csv")  # Replace with your file path
category_data = df_sample['Category'].value_counts()

# Set up the Streamlit dashboard
st.title('Category and Value Data Dashboard')

# Bar Chart for 'Category'
st.subheader('Bar Chart: Frequency of Categories')
fig1, ax1 = plt.subplots(figsize=(8, 6))
category_data.plot(kind='bar', color='skyblue', ax=ax1)
ax1.set_title('Bar Chart of Category')
ax1.set_xlabel('Category')
ax1.set_ylabel('Frequency')
ax1.set_xticklabels(category_data.index, rotation=45)
st.pyplot(fig1)

# Pie Chart for 'Category'
st.subheader('Pie Chart: Distribution of Categories')
fig2, ax2 = plt.subplots(figsize=(8, 8))
category_data.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightblue', 'lightgreen'], ax=ax2)
ax2.set_title('Pie Chart of Category')
ax2.set_ylabel('')  # Hides the y-label for pie chart
st.pyplot(fig2)

# Histogram for 'Value'
st.subheader('Histogram: Distribution of Values')
fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.hist(df_sample['Value'], bins=20, color='lightblue', edgecolor='black')
ax3.set_title('Histogram of Value')
ax3.set_xlabel('Value')
ax3.set_ylabel('Frequency')
st.pyplot(fig3)

