import streamlit as st
import math
import matplotlib.pyplot as plt

# App Layout Configuration
st.set_page_config(page_title="Four-Stroke Engine Calculator", layout="centered")

st.title(" Four-Stroke Engine Calculator")
st.markdown("Determine critical internal internal engine metrics instantly by adjusting variables below.")

# Sidebar Configuration for Inputs
st.sidebar.header(" Engine Input Dimensions")

calculation_mode = st.sidebar.radio(
    "Choose Mode:",
    ["Full Engine Analysis", "Single Parameter Calculation"]
)

# Shared Core Inputs
bore = st.sidebar.slider("Cylinder Bore (Diameter) in cm", min_value=1.0, max_value=20.0, value=8.5, step=0.1)
stroke = st.sidebar.slider("Stroke Length in cm", min_value=1.0, max_value=20.0, value=8.8, step=0.1)
cylinders = st.sidebar.number_input("Number of Cylinders", min_value=1, max_value=16, value=4, step=1)

if calculation_mode == "Full Engine Analysis":
    compression_ratio = st.sidebar.slider("Target Compression Ratio (:1)", min_value=2.0, max_value=25.0, value=10.5, step=0.1)

    # Computations
    swept_vol = (math.pi / 4) * (bore ** 2) * stroke * cylinders
    clearance_vol = swept_vol / (compression_ratio - 1)
    total_vol = swept_vol + clearance_vol

    # Metrics Display Columns
    st.subheader(" Complete Engine Diagnostics")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Swept Volume (Vs)", value=f"{swept_vol:.2f} cc / cm³")
        st.metric(label="Clearance Volume (Vc)", value=f"{clearance_vol:.2f} cc / cm³")
    with col2:
        st.metric(label="Total Cylinder Volume (Vt)", value=f"{total_vol:.2f} cc / cm³")
        st.metric(label="Compression Ratio (rc)", value=f"{compression_ratio:.1f} : 1")

    # Simple Visual Proportions Graph
    st.markdown("---")
    st.subheader(" Visualizing Volume Breakdown")
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.barh(["Engine Volume Structure"], [clearance_vol], label="Clearance Volume (Vc)", color="#FF4B4B")
    ax.barh(["Engine Volume Structure"], [swept_vol], left=[clearance_vol], label="Swept Volume (Vs)", color="#0068C9")
    ax.set_xlabel("Volume (cc)")
    ax.legend(loc='lower right')
    st.pyplot(fig)

else:
    st.subheader("Single Objective Explorer")
    metric_choice = st.selectbox(
        "Which isolated metric are you solving for?",
        ["Swept Volume", "Clearance Volume", "Compression Ratio", "Total Cylinder Volume"]
    )
    
    if metric_choice == "Swept Volume":
        swept_vol = (math.pi / 4) * (bore ** 2) * stroke * cylinders
        st.success(f"Calculated Swept Volume (**Vs**): **{swept_vol:.2f} cm³ (cc)**")
        
    elif metric_choice == "Clearance Volume":
        v_s = st.number_input("Known Swept Volume (cc)", min_value=10.0, value=1998.0)
        c_r = st.number_input("Compression Ratio (e.g. 10.5)", min_value=1.1, value=10.5)
        clearance_vol = v_s / (c_r - 1)
        st.success(f"Calculated Clearance Volume (**Vc**): **{clearance_vol:.2f} cm³ (cc)**")
        
    elif metric_choice == "Compression Ratio":
        v_s = st.number_input("Known Swept Volume (cc)", min_value=10.0, value=1998.0)
        v_c = st.number_input("Known Clearance Volume (cc)", min_value=1.0, value=210.0)
        compression_ratio = (v_s + v_c) / v_c
        st.success(f"Calculated Compression Ratio (**rc**): **{compression_ratio:.2f} : 1**")
        
    elif metric_choice == "Total Cylinder Volume":
        v_s = st.number_input("Known Swept Volume (cc)", min_value=10.0, value=1998.0)
        v_c = st.number_input("Known Clearance Volume (cc)", min_value=1.0, value=210.0)
        total_vol = v_s + v_c
        st.success(f"Calculated Total Cylinder Volume (**Vt**): **{total_vol:.2f} cm³ (cc)**")
