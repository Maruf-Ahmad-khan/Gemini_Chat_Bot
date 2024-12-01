import streamlit as st
import streamlit.components.v1 as components  # Explicit import for components.v1

# Set page title
st.title("Power BI Dashboard Integration")

# Power BI Embed URL
power_bi_embed_url = "https://app.fabric.microsoft.com/reportEmbed?reportId=d7bf2537-352b-4035-aa23-bbc023d48418&autoAuth=true&ctid=4a36bb2f-1c55-49e0-9a23-6281dfd38c6b"

# HTML code to embed Power BI in an iframe
html_code = f"""
<iframe 
    title="Power BI Dashboard" 
    width="100%" 
    height="600" 
    src="{power_bi_embed_url}" 
    frameborder="0" 
    allowFullScreen="true">
</iframe>
"""

# Render the iframe in Streamlit
components.html(html_code, height=600)
