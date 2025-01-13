import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Kamesh S - Portfolio", layout="wide", initial_sidebar_state="collapsed")

# Define CSS for light and dark themes
def set_css(dark_mode):
    if dark_mode:
        st.markdown(
            """
            <style>
            body {
                background-color: #1e1e1e;
                color: #ffffff;
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
            }
            .header {
                text-align: center;
                padding: 40px;
                margin-bottom: 20px;
            }
            .header h1 {
                font-size: 3em;
                color: #00BFFF;
            }
            .header p {
                font-size: 1.2em;
                color: #B0C4DE;
            }
            .card {
                background: linear-gradient(145deg, #333333, #1e1e1e);
                border-radius: 15px;
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5), -5px -5px 15px rgba(50, 50, 50, 0.2);
                padding: 20px;
                width: 300px;
                text-align: center;
                margin: 10px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .card:hover {
                transform: scale(1.1);
                box-shadow: 5px 5px 25px rgba(0, 0, 0, 0.7), -5px -5px 25px rgba(50, 50, 50, 0.3);
                cursor: pointer;
            }
            a {
                text-decoration: none;
                color: #1E90FF;
                font-weight: bold;
            }
            .container {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 20px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            body {
                background-color: #ffffff;
                color: #000000;
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
            }
            .header {
                text-align: center;
                padding: 40px;
                margin-bottom: 20px;
            }
            .header h1 {
                font-size: 3em;
                color: #1E90FF;
            }
            .header p {
                font-size: 1.2em;
                color: #696969;
            }
            .card {
                background: linear-gradient(145deg, #f0f0f0, #e0e0e0);
                border-radius: 15px;
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.1), -5px -5px 15px rgba(255, 255, 255, 0.7);
                padding: 20px;
                width: 300px;
                text-align: center;
                margin: 10px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .card:hover {
                transform: scale(1.1);
                box-shadow: 5px 5px 25px rgba(0, 0, 0, 0.2), -5px -5px 25px rgba(255, 255, 255, 0.8);
                cursor: pointer;
            }
            a {
                text-decoration: none;
                color: #1E90FF;
                font-weight: bold;
            }
            .container {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 20px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

# Toggle for dark mode
def toggle_dark_mode():
    if "dark_mode" not in st.session_state:
        st.session_state["dark_mode"] = True
    if st.sidebar.button("Toggle Dark Mode"):
        st.session_state["dark_mode"] = not st.session_state["dark_mode"]
    return st.session_state["dark_mode"]

# Initialize dark mode
is_dark_mode = toggle_dark_mode()
set_css(is_dark_mode)

# Page header
st.markdown(
    """
    <div class="header">
        <h1>Kamesh S - Portfolio</h1>
        <p>Data Scientist | Developer | Innovator</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Data for cards
cards = [
    {
        "title": "Machine Learning Projects",
        "description": "Explore my work in regression, classification, pipelines, and innovative hybrid models.",
        "link": "https://github.com/your-github/ml-projects"
    },
    {
        "title": "Web Applications",
        "description": "Showcasing full-stack projects with cloud deployment and integration of machine learning models.",
        "link": "https://github.com/your-github/web-apps"
    },
    {
        "title": "AR/VR Effects",
        "description": "Interactive effects and immersive designs, including character tracking and Native UI Picker effects.",
        "link": "https://github.com/your-github/ar-vr-effects"
    },
    {
        "title": "Research Papers",
        "description": "Contributions to reverse forecasting, medicinal plant classification, and innovative data science techniques.",
        "link": "https://github.com/your-github/research-papers"
    },
    {
        "title": "To-Do List Automation",
        "description": "Advanced to-do list features like location tracking, email task monitoring, and intelligent alerts.",
        "link": "https://github.com/your-github/todo-automation"
    }
]

# Render cards
st.markdown('<div class="container">', unsafe_allow_html=True)
for card in cards:
    st.markdown(
        f"""
        <div class="card">
            <h3>{card['title']}</h3>
            <p>{card['description']}</p>
            <a href="{card['link']}" target="_blank">Go to GitHub</a>
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)
