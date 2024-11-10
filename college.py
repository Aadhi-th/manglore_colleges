import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Colleges in Mangalore", page_icon="🏫", layout="wide")

# Custom fonts and background styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    /* Global settings */
    body, .main {
        background-color: #f3f4f6;
        color: #333333;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Page Title styling */
    .title {
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        color: #FFFFFF;
        padding: 15px;
        border-radius: 8px;
        background: linear-gradient(to right, #6a11cb, #2575fc);
        margin-bottom: 20px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    
    /* College card styling */
    .college-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.8), rgba(255,255,255,0.6));
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    .college-card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.3);
    }
    
    /* College name styling */
    .college-name {
        font-size: 1.7em;
        font-weight: 700;
        color: #4b6584;
        margin-bottom: 8px;
    }
    
    /* Info styling */
    .program-info, .contact-info {
        color: #8e44ad;
        font-weight: 500;
    }
    
    /* Link styling */
    a {
        color: #1abc9c;
        text-decoration: none;
        font-weight: bold;
    }
    a:hover {
        color: #16a085;
    }
    
    /* Footer styling */
    .footer {
        font-size: 1em;
        text-align: center;
        color: #FFFFFF;
        margin-top: 50px;
        padding: 10px;
        border-radius: 5px;
        background: linear-gradient(to right, #16a085, #2ecc71);
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown("<div class='title'>Explore Top Colleges in Mangalore</div>", unsafe_allow_html=True)

# Sample Data for Colleges in Mangalore with lat-long for map display, institute pictures, and additional details
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
    "Contact": [
        "+91 824 2449700",
        "+91 824 2474000",
        "+91 824 2287276",
        "+91 824 2225533",
        "+91 824 2492366",
        "+91 824 2204668",
        "+91 824 2274722",
        "+91 824 2277677",
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
    "Website": [
        "https://staloysius.edu.in",
        "https://www.nitk.ac.in",
        "https://mangaloreuniversity.ac.in",
        "http://ajims.edu.in",
        "https://canaracollege.edu.in",
        "https://yenepoya.edu.in",
        "https://srinivasgroup.com",
        "https://sahyadri.edu.in",
    ],
    "Ranking": [
        "Ranked #10 in Karnataka",
        "Ranked #2 for Engineering in Karnataka",
        "NAAC Accredited A+",
        "Top Medical College in Mangalore",
        "Notable for Science Programs",
        "Renowned Medical University",
        "Top Institute for Engineering in Mangalore",
        "Top Engineering & Management College",
    ],
    "Latitude": [12.8703, 13.0117, 12.8136, 12.8895, 12.8654, 12.8217, 12.8363, 12.8724],
    "Longitude": [74.8434, 74.7943, 74.9049, 74.8491, 74.8382, 74.8785, 74.8723, 74.8706],
    "Image URL": [
        "https://staloysius.edu.in/storage/files/images/New%20College%20Logo%20ESTD.jpg",
        "https://styles.redditmedia.com/t5_2voja/styles/communityIcon_1s85lpu2lcy51.jpg?format=pjpg&s=420e4b0de418e5eec223ddd8a94c1fc8417237b9",
        "https://static.toiimg.com/thumb/msid-66877080,imgsize-108816,width-400,resizemode-4/66877080.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFbGKXGX2Cxl9j1P1iKkJcO4qI_H6qNUtZiw&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4baZhZeW2w6hC18ddnvG71chM3k3YWfL6wQ&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSo_GM4B5EeMoeF4qnarWjp_KA9uOq1yFGpKw&s",
        "https://upload.wikimedia.org/wikipedia/en/e/e1/Srinivas_University_logo.gif",
        "https://res.cloudinary.com/dfxpdpbvs/image/upload/v1720181979/Sayhadri-Logo-02.jpg",
    ],
}

# Create DataFrame
df = pd.DataFrame(data)

# Sidebar - Filter by College Name
st.sidebar.header("Filter by College")
selected_college = st.sidebar.selectbox("Select college:", ["All"] + df["College Name"].tolist())

# Sidebar - Filters for Programs
st.sidebar.header("Filter by Programs Offered")
selected_program = st.sidebar.multiselect("Select program(s):", df["Programs Offered"].unique())

# Filter Data Based on Selections
df_filtered = df.copy()
if selected_college != "All":
    df_filtered = df_filtered[df_filtered["College Name"] == selected_college]
if selected_program:
    df_filtered = df_filtered[df_filtered["Programs Offered"].isin(selected_program)]

# Map of Colleges
st.subheader("Map of Colleges in Mangalore")
df_filtered = df_filtered.rename(columns={"Latitude": "latitude", "Longitude": "longitude"})
st.map(df_filtered[['latitude', 'longitude']])

# Display College Information
for _, row in df_filtered.iterrows():
    st.markdown(f"<div class='college-card'>", unsafe_allow_html=True)
    st.image(row["Image URL"], width=80, caption=row["College Name"], use_column_width=False)
    st.markdown(f"<div class='college-name'>{row['College Name']}</div>", unsafe_allow_html=True)
    st.write(f"**Address:** {row['Address']}")
    with st.expander("More Details"):
        st.write(f"<span class='program-info'><strong>Programs Offered:</strong> {row['Programs Offered']}</span>", unsafe_allow_html=True)
        st.write(f"<span class='contact-info'><strong>Contact:</strong> {row['Contact']}</span>", unsafe_allow_html=True)
        st.write(f"<span class='contact-info'><strong>Website:</strong> <a href='{row['Website']}' target='_blank'>{row['Website']}</a></span>", unsafe_allow_html=True)
        st.write(f"**Ranking:** {row['Ranking']}")
    st.markdown("</div>", unsafe_allow_html=True)
    st.write("---")

# Footer
st.markdown(
    """
    <div class='footer'>FUTURE IN YOUR HANDS</div>
    """,
    unsafe_allow_html=True
)
