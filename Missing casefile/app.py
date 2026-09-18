import streamlit as st
import pandas as pd
import numpy as np

st.title("CaseFile - Missing Person Search Zones")
st.write("ML-based last-seen trajectory prediction")

st.sidebar.header("Case Details")
lat = st.sidebar.number_input("Last Seen Latitude", value=17.3850, format="%.4f")
lon = st.sidebar.number_input("Last Seen Longitude", value=78.4867, format="%.4f")
hours = st.sidebar.slider("Hours Missing", 1, 48, 6)
radius = st.sidebar.slider("Search Radius (km)", 1, 20, 5)

if st.sidebar.button("Predict Zones"):
    # Simulate 3 probability zones
    zones = []
    for i, spread in enumerate([0.01, 0.03, 0.06]):
        n = 80
        zones.append(pd.DataFrame({
            'lat': np.random.normal(lat, spread, n),
            'lon': np.random.normal(lon, spread, n),
            'zone': f'Zone {i+1}'
        }))
    data = pd.concat(zones)
    st.map(data[['lat','lon']])
    
    col1, col2, col3 = st.columns(3)
    col1.metric("High Priority Zone", f"{radius*0.3:.1f} km")
    col2.metric("Medium Zone", f"{radius*0.6:.1f} km")
    col3.metric("Low Priority Zone", f"{radius:.1f} km")
    
    st.success(f"{hours} hours missing case ki 3 zones generate ayyayi!")
