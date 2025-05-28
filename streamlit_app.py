import streamlit as st
import pandas as pd
import plotly.express as px

st.write('Azis')

st.set_page_config(page_title="RUPTL Comparison Dashboard", layout="wide")
st.markdown("""
<h1 style="
    font-size: 3em;
    font-weight: 900;
    background: linear-gradient(to right, #8e44ad, #2980b9, #e84393);
    -webkit-background-clip: text;
    color: transparent;
    text-align: left;
    margin-top: -20px;
">
RUPTL Comparison Dashboard
</h1>
""", unsafe_allow_html=True)
st.markdown("""
Welcome to the **RUPTL Comparative Dashboard**. This interactive app helps you explore and analyze the evolution of Indonesia's electricity roadmap between **RUPTL 2021–2030** and **RUPTL 2025–2034**. Use the dropdowns and charts below to understand how capacity targets, energy mix, investment, and strategy have shifted over time toward a greener and more resilient future.
""", unsafe_allow_html=True)
# ---- Tabular Sections ----

st.markdown("""
<h1 style="
    font-size: 2em;
    font-weight: 700;
    background: linear-gradient(to right, #8e44ad, #2980b9, #e84393);
    -webkit-background-clip: text;
    color: transparent;
    text-align: left;
    margin-top: -20px;
">
Explore Sections by Category
</h1>
""", unsafe_allow_html=True)


def show_capacity_table():
    data = {
        "Metric": [
            "Total Planned Capacity (GW)",
            "Renewables (EBT) (GW)",
            "Fossil Fuel (GW)",
            "Storage Capacity (GW)",
            "Nuclear (GW)"
        ],
        "RUPTL 2021–2030": [40.6, 20.9, 19.7, 0, 0],
        "RUPTL 2025–2034": [69.5, 42.6, 16.6, 10.3, 0.5],
        "Remarks": [
            "+71% increase",
            "EBT nearly doubled",
            "Fossil portion reduced",
            "New category introduced",
            "First time inclusion"
        ]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

def show_regional_table():
    data = {
        "Region": [
            "Sumatera", "Jawa–Madura–Bali", "Kalimantan", "Sulawesi", "Maluku–Papua–NT"
        ],
        "RUPTL 2021–2030 (GW)": [5.2, 9.6, 1.7, 2.3, 2.0],
        "RUPTL 2025–2034 (GW)": [9.5, 19.6, 3.5, 7.7, 2.3],
        "Dominant Tech": [
            "Hydro, Geothermal",
            "Solar (10.9 GW)",
            "Solar, Nuclear (pilot)",
            "Hydro, Wind",
            "Solar"
        ]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

def show_demand_table():
    data = {
        "Metric": [
            "Electricity Sales Target (TWh)",
            "Avg. Growth per Year (%)"
        ],
        "RUPTL 2021–2030": [445, 4.9],
        "RUPTL 2025–2034": [511, 5.5],
        "Remarks": [
            "~15% higher target",
            "Higher post-COVID optimism"
        ]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

def show_infra_table():
    data = {
        "Metric": [
            "Transmission (kms)",
            "Substations (MVA)",
            "Investment Needs (Trillion IDR)",
            "Green Jobs Created (Million)"
        ],
        "RUPTL 2021–2030": [47.7, 76.7, 1793, 0],
        "RUPTL 2025–2034": [47.8, 107.9, 2967, 1.7],
        "Remarks": [
            "Flat, but improved quality",
            "+40% increase",
            "+65% increase",
            "91% are green jobs"
        ]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

def show_strategy_table():
    data = {
        "Policy Direction": [
            "Nuclear Power",
            "Energy Storage (Battery + Pumped Hydro)",
            "Alignment with RUKN 2025",
            "Village Electrification (Lisdes, BPBL)",
            "Support for 8% GDP Growth (2029)"
        ],
        "RUPTL 2021–2030": [
            "Not included", "Not emphasized", "No", "Basic level", "No direct target"
        ],
        "RUPTL 2025–2034": [
            "0.5 GW included", "10.3 GW planned", "Yes", "Aggressive national coverage", "Explicit alignment"
        ]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

def show_takeaways():
    st.markdown("""
    ### 📌 Key Takeaways
    1. **RUPTL 2025–2034 is more ambitious and greener**, nearly doubling RE plans.
    2. **Execution readiness** is clear – the plan isn't theoretical anymore.
    3. **Region-based energy planning** ensures optimized local development.
    4. **PLN shifts to an enabler**, increasing private sector (IPP) role.
    5. **Massive green investment and job creation** will drive inclusive economic growth.
    """)

# Dropdown
options = st.selectbox(
    "Select a section to view:", 
    (
        "1️⃣ Capacity Expansion & Bauran Energi",
        "2️⃣ Regional Renewable Energy Plan",
        "3️⃣ Electricity Demand & Sales",
        "4️⃣ Infrastructure & Investment",
        "5️⃣ Strategy & Policy Direction",
        "📌 Key Takeaways"
    )
)

# Show relevant section
if options.startswith("1"):
    show_capacity_table()
elif options.startswith("2"):
    show_regional_table()
elif options.startswith("3"):
    show_demand_table()
elif options.startswith("4"):
    show_infra_table()
elif options.startswith("5"):
    show_strategy_table()
else:
    show_takeaways()

# --- Bar Chart Comparison (unchanged) ---
st.subheader("Visual Comparison")

metrics_data = {
    "Total Planned Capacity (GW)": [40.6, 69.5],
    "Renewables (EBT) Capacity (GW)": [20.9, 42.6],
    "Fossil Fuel Capacity (GW)": [19.7, 16.6],
    "Storage Capacity (GW)": [0, 10.3],
    "Substation Capacity (MVA)": [76.7, 107.9],
    "Transmission Length (kms)": [47.7, 47.8],
    "Investment (Trillion IDR)": [1793, 2967],
    "Target Electricity Sales (TWh)": [445, 511],
    "Green Jobs (Million)": [0, 1.7]
}

df = pd.DataFrame(metrics_data, index=["RUPTL 2021–2030", "RUPTL 2025–2034"]).T
selected_metrics = st.multiselect("Select metrics to compare:", df.index.tolist(), default=["Total Planned Capacity (GW)","Renewables (EBT) Capacity (GW)"])

if selected_metrics:
    fig = px.bar(
        df.loc[selected_metrics],
        barmode="group",
        title="Selected RUPTL Metric Comparisons",
        labels={"value": "Value", "index": "Metric"},
        color_discrete_sequence=["#6c5ce7", "#2980b9"]  # <--- Custom colors!
    )
    st.plotly_chart(fig, use_container_width=True)
