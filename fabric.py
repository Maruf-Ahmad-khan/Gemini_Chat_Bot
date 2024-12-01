import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

# Streamlit Dashboard Title
st.title("Fabric Notebook Analytics")

# Step 1: Fetch or Load Data
file_url = "https://app.fabric.microsoft.com/groups/0a3cd20f-7522-4b6b-a71b-f1c9e384332c/synapsenotebooks/91221cf8-37f0-4a3d-a74c-051b549b3577?clientSideAuth=0&experience=power-bi"

st.write("Fetching data from the provided URL...")

try:
    # Fetch the file content
    response = requests.get(file_url)
    response.raise_for_status()  # Check for HTTP errors

    # Read the data using Pandas
    # - Skip problematic lines with `on_bad_lines='skip'`
    # - Allow flexible delimiter guessing with `delim_whitespace=True` as a fallback
    raw_data = response.text
    data = pd.read_csv(io.StringIO(raw_data), on_bad_lines='skip', sep=None, engine='python')  # Flexible parsing
    st.success("Data successfully loaded!")
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data from the URL: {e}")
    st.stop()
except pd.errors.ParserError as e:
    st.error(f"Error parsing the data file: {e}")
    st.stop()

# Step 2: Data Exploration
st.subheader("Data Overview")
st.write(data.head())  # Display first few rows
st.write("Data Shape:", data.shape)

# Step 3: Data Visualization
st.subheader("Visualizations")

# Example: Plotting column distributions
columns = list(data.columns)
selected_column = st.selectbox("Select a column to visualize:", columns)

if data[selected_column].dtype in ['int64', 'float64']:
    st.bar_chart(data[selected_column])
else:
    st.write(f"The selected column '{selected_column}' is not numerical.")

# Step 4: Advanced Analytics
st.subheader("Custom Analytics")
# Example: Show correlations if the data is numerical
if any(data.dtypes == 'int64') or any(data.dtypes == 'float64'):
    correlation = data.corr()
    st.write("Correlation Matrix:")
    st.dataframe(correlation)
    st.write("Heatmap (Top 10 Features):")
    fig, ax = plt.subplots()
    heatmap = ax.imshow(correlation, cmap='coolwarm', interpolation='nearest')
    plt.colorbar(heatmap)
    st.pyplot(fig)

# Step 5: Save Processed Data
if st.button("Export Processed Data"):
    processed_path = "processed_analytics.csv"
    data.to_csv(processed_path, index=False)
    st.success(f"Processed data saved to {processed_path}")
