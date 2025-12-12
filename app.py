import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Load your data
diverted_flights = pd.read_csv('diverted_flights.csv')
diverted_flights['FlightDate'] = pd.to_datetime(diverted_flights['FlightDate'])

# Load airport coordinates
airports_clean = pd.read_csv('airports.csv')
airports_clean = airports_clean.set_index('AIRPORT')[['LATITUDE', 'LONGITUDE']]

# Define get_coords function
def get_coords(airport_code, airport_df):
    if airport_code in airport_df.index:
        coords = airport_df.loc[airport_code]
        return (coords['LATITUDE'], coords['LONGITUDE'])
    return (None, None)

# Page config
st.set_page_config(page_title="Flight Diversions Dashboard", layout="wide")
st.title("Flight Diversions Dashboard")

# Filters in sidebar
st.sidebar.header("Filters")

airlines = st.sidebar.multiselect(
    'Select Airlines',
    options=sorted(diverted_flights['Marketing_Airline_Network'].unique().tolist()),
    default=sorted(diverted_flights['Marketing_Airline_Network'].unique().tolist())[:3]
)

date_range = st.sidebar.date_input(
    'Select Date Range',
    value=(diverted_flights['FlightDate'].min().date(), diverted_flights['FlightDate'].max().date()),
    min_value=diverted_flights['FlightDate'].min().date(),
    max_value=diverted_flights['FlightDate'].max().date()
)

# Filter data
filtered = diverted_flights[
    (diverted_flights['Marketing_Airline_Network'].isin(airlines)) &
    (diverted_flights['FlightDate'].dt.date >= date_range[0]) &
    (diverted_flights['FlightDate'].dt.date <= date_range[1])
]

# Summary statistics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Diversions", f"{len(filtered):,}")

with col2:
    st.metric("Diversion Airports", filtered['Div1Airport'].nunique())

with col3:
    st.metric("Avg Departure Delay (min)", f"{filtered['DepDelay'].mean():.1f}")

# Diversion map
st.subheader("Top Diversion Airports")

div_airports = filtered['Div1Airport'].value_counts().head(15)
div_lats = [get_coords(code, airports_clean)[0] for code in div_airports.index]
div_lons = [get_coords(code, airports_clean)[1] for code in div_airports.index]

fig_map = go.Figure()

fig_map.add_trace(go.Scattergeo(
    lon=div_lons,
    lat=div_lats,
    mode='markers+text',
    marker=dict(size=div_airports.values/10, color='red', opacity=0.7),
    text=div_airports.index,
    textposition='top center',
    hovertemplate='<b>%{text}</b><br>Diversions: %{customdata}<extra></extra>',
    customdata=div_airports.values,
    name='Diversion Airports'
))

fig_map.update_layout(
    title=f'Top Diversion Airports ({len(filtered)} diversions)',
    geo=dict(
        projection_type='mercator',
        showland=True,
        landcolor='rgb(243, 243, 243)',
        center=dict(lat=40, lon=-95),
        lataxis_range=[25, 50],
        lonaxis_range=[-125, -70]
    ),
    height=500
)

st.plotly_chart(fig_map, use_container_width=True)

# Airline stats
st.subheader("Diversions by Airline")

airline_counts = filtered['Marketing_Airline_Network'].value_counts()

fig_bar = go.Figure()

fig_bar.add_trace(go.Bar(
    x=airline_counts.index,
    y=airline_counts.values,
    marker=dict(color='steelblue'),
    hovertemplate='<b>%{x}</b><br>Diversions: %{y}<extra></extra>'
))

fig_bar.update_layout(
    title=f'Diversions by Airline ({len(filtered)} total)',
    xaxis_title='Airline',
    yaxis_title='Number of Diversions',
    height=400,
    showlegend=False
)

st.plotly_chart(fig_bar, use_container_width=True)