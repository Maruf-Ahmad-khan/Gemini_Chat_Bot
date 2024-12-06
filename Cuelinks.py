import streamlit as st
import streamlit.components.v1 as components  # Explicit import for components.v1

# Set page title
st.set_page_config(
    page_title="Cuelinks Power BI Report",
    layout="wide",  # Use the wide layout for better utilization of screen space
)

# Add title
st.title("Cuelinks Report")

# Power BI Embed URL
power_bi_embed_url = "https://app.fabric.microsoft.com/reportEmbed?reportId=c71a2be3-ad0c-4c17-ac14-a6895c4e7bc4&autoAuth=true&ctid=4a36bb2f-1c55-49e0-9a23-6281dfd38c6b"

# HTML code to embed Power BI in an iframe
html_code = f"""
<iframe 
    title="Power BI Dashboard" 
    width="100%" 
    height="800"  # Increased height for better viewing
    src="{power_bi_embed_url}" 
    frameborder="0" 
    allowFullScreen="true">
</iframe>
"""

# Render the iframe in Streamlit
components.html(html_code, height=800)  # Match the iframe height here

st.title("Aliexpress and Flipshope(Aug, Sept And Nov) Report")
power_bi_embed_url = "https://app.powerbi.com/reportEmbed?reportId=269f99fa-f477-4ce4-968c-8dc43b1c1959&autoAuth=true&ctid=4a36bb2f-1c55-49e0-9a23-6281dfd38c6b"

# HTML code to embed Power BI in an iframe
html_code = f"""
<iframe 
    title="Power BI Dashboard" 
    width="100%" 
    height="800"  # Increased height for better viewing
    src="{power_bi_embed_url}" 
    frameborder="0" 
    allowFullScreen="true">
</iframe>
"""

# Render the iframe in Streamlit
components.html(html_code, height=800)  # Match the iframe height here
