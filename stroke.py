import streamlit as st
import math

st.set_page_config(
    page_title="Four Stroke Engine Calculator",
    page_icon="⚙️"
)

st.title("⚙️ Four Stroke Engine Calculator")

D = st.number_input("Enter Bore Diameter (mm)", min_value=0.1, value=100.0)
L = st.number_input("Enter Stroke Length (mm)", min_value=0.1, value=120.0)
r = st.number_input("Enter Compression Ratio", min_value=1.01, value=8.0)

if st.button("Calculate"):

    # Convert mm to metre
    D = D / 1000
    L = L / 1000

    # Swept Volume
    Vs = (math.pi / 4) * D**2 * L

    # Clearance Volume
    Vc = Vs / (r - 1)

    # Total Cylinder Volume
    Vt = Vs + Vc

    st.subheader("Results")

    st.write(f"Swept Volume = {Vs:.6f} m³")
    st.write(f"Clearance Volume = {Vc:.6f} m³")
    st.write(f"Total Cylinder Volume = {Vt:.6f} m³")
    st.write(f"Compression Ratio = {r:.2f}:1")

    st.subheader("Formulas")

    st.latex(r"V_s = \frac{\pi}{4}D^2L")
    st.latex(r"V_c = \frac{V_s}{r-1}")
    st.latex(r"V_t = V_s + V_c")
