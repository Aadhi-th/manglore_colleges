import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Colleges in Mangalore", page_icon=":college board:", layout="wide")

# Background styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f8ff;
        background-image: linear-gradient(to bottom right, #FF5733, #33B5FF);
        color: white;
    }
    .title {
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        color: #FFFFFF;
    }
    .college-list {
        background: rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    .college-header {
        font-size: 2em;
        color: #FFE333;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown("<div class='title'>Explore Colleges in Mangalore</div>", unsafe_allow_html=True)

# Sample Data for Colleges in Mangalore with lat-long for map display
data = {
    "College Name": [
        "St. Aloysius College",
        "NITK Surathkal",
        "Mangalore University",
        "A.J. Institute of Medical Sciences",
        "Canara College",
        "Yenepoya University",
        "Srinivas Institute of Technology",
        "Sahyadri College of Engineering and Management",
    ],
    "Address": [
        "Light House Hill Rd, Kodialbail, Mangaluru, Karnataka",
        "NH 66, Srinivas Nagar, Surathkal, Mangalore, Karnataka",
        "Konaje, Mangaluru, Karnataka",
        "NH 66, Kuntikana, Mangalore, Karnataka",
        "Kodialbail, Mangalore, Karnataka",
        "University Rd, Deralakatte, Karnataka",
        "Valachil, Mangalore, Karnataka",
        "Adyar, Mangalore, Karnataka",
    ],
    "Programs Offered": [
        "Undergraduate, Postgraduate",
        "Engineering, Sciences",
        "Science, Arts, Commerce",
        "Medical, Nursing",
        "Science, Commerce, Management",
        "Medical, Dental, Nursing",
        "Engineering, MBA",
        "Engineering, MBA",
    ],
    "Latitude": [12.8703, 13.0117, 12.8136, 12.8895, 12.8654, 12.8217, 12.8363, 12.8724],
    "Longitude": [74.8434, 74.7943, 74.9049, 74.8491, 74.8382, 74.8785, 74.8723, 74.8706]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sidebar - Filters for Programs
st.sidebar.header("Filter by Programs Offered")
selected_program = st.sidebar.multiselect("Select program(s):", df["Programs Offered"].unique())

# Filter Data Based on Selection
if selected_program:
    df_filtered = df[df["Programs Offered"].isin(selected_program)]
else:
    df_filtered = df

# Display Map of Colleges
# Display Map of Colleges
st.subheader("Map of Colleges in Mangalore")

# Rename columns to match Streamlit's requirements
df_filtered = df_filtered.rename(columns={"Latitude": "latitude", "Longitude": "longitude"})

st.map(df_filtered[['latitude', 'longitude']])


# Display College Information
st.markdown("<div class='college-list'>", unsafe_allow_html=True)
for i, row in df_filtered.iterrows():
    st.markdown(f"<div class='college-header'>{row['College Name']}</div>", unsafe_allow_html=True)
    with st.expander("View Details"):
        st.write(f"**Address:** {row['Address']}")
        st.write(f"**Programs Offered:** {row['Programs Offered']}")
    st.write("---")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <style>
    .footer {
        font-size: 1em;
        text-align: center;
        color: #FFFFFF;
        margin-top: 50px;
    }
    </style>
    <div class='footer'>Made with ❤️ in Mangalore | Powered by Streamlit</div>
    """,
    unsafe_allow_html=True
)
