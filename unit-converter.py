import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="🌍 Unit Converter Pro",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------- ANIMATED GRADIENT BACKGROUND -------------------
st.markdown(
    """
    <style>
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .stApp {
        background: linear-gradient(-45deg, #ffecd2, #fcb69f, #e0c3fc, #8ec5fc);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 15px;
        transition: transform 0.3s;
    }
    .card:hover {
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------- HEADER -------------------
st.markdown("<h1 style='text-align:center; color:#4B0082;'>🌍 Unit Converter Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Convert Length, Weight, and Time with interactive charts</p>", unsafe_allow_html=True)
st.write("---")

# ------------------- CONVERSION FUNCTION -------------------
def convert_units(conversion_type, value):
    if conversion_type == "Length":
        return {
            "Kilometers ➡ Miles": value * 0.621371,
            "Miles ➡ Kilometers": value / 0.621371
        }
    elif conversion_type == "Weight":
        return {
            "Kilograms ➡ Pounds": value * 2.20462,
            "Pounds ➡ Kilograms": value / 2.20462
        }
    elif conversion_type == "Time":
        return {
            "Seconds ➡ Minutes": value / 60,
            "Minutes ➡ Seconds": value * 60,
            "Minutes ➡ Hours": value / 60,
            "Hours ➡ Minutes": value * 60,
            "Hours ➡ Days": value / 24,
            "Days ➡ Hours": value * 24
        }

# ------------------- SIDEBAR SETTINGS -------------------
st.sidebar.header("⚙️ Conversion Settings")
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Time"])
value = st.sidebar.number_input("Enter Value", min_value=0.0, format="%.4f")

# ------------------- TABS -------------------
tabs = st.tabs(["📊 Results", "📈 Live Chart"])

# ------------------- RESULTS TAB -------------------
with tabs[0]:
    st.subheader(f"{conversion_type} Conversion Results")
    col1, col2 = st.columns(2)

    # Left Column - Cards
    with col1:
        results = convert_units(conversion_type, value)
        for k, v in results.items():
            st.markdown(f"<div class='card'><h3>{k}</h3><p style='font-size:20px'>{value} ➡ {v:.4f}</p></div>", unsafe_allow_html=True)

    # Right Column - Table
    with col2:
        st.markdown("### Conversion Table")
        df_table = pd.DataFrame(list(results.items()), columns=["Conversion", "Result"])
        st.dataframe(df_table, height=300)

# ------------------- LIVE CHART TAB -------------------
with tabs[1]:
    st.subheader(f"📈 Live Chart - {conversion_type}")
    df_chart = pd.DataFrame(list(results.items()), columns=["Conversion", "Result"])
    fig = px.bar(df_chart, x="Conversion", y="Result", text="Result", color="Result",
                 color_continuous_scale="Viridis", template="plotly_white")
    fig.update_traces(texttemplate='%{text:.4f}', textposition='outside', hovertemplate='%{x}: %{y:.4f}')
    fig.update_layout(yaxis_title="Converted Value", xaxis_title="Conversion Type", uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig, use_container_width=True)

# ------------------- FOOTER -------------------
st.write("---")
st.markdown("<p style='text-align:center; color:gray;'>Made with ❤️ by Sanoober</p>", unsafe_allow_html=True)
