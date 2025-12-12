import panel as pn
import plotly.graph_objects as go
import pandas as pd
import numpy as np

pn.extension('plotly')

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

# Filters
airline_select = pn.widgets.MultiSelect(
    name='Airlines',
    options=sorted(diverted_flights['Marketing_Airline_Network'].unique().tolist()),
    value=sorted(diverted_flights['Marketing_Airline_Network'].unique().tolist())[:3],
    width=300
)

date_range = pn.widgets.DateRangeSlider(
    name='Date Range',
    start=diverted_flights['FlightDate'].min(),
    end=diverted_flights['FlightDate'].max(),
    value=(diverted_flights['FlightDate'].min(), diverted_flights['FlightDate'].max()),
    width=400
)

# Update functions
@pn.depends(airline_select.param.value, date_range.param.value)
def diversion_map(airlines, dates):
    filtered = diverted_flights[
        (diverted_flights['Marketing_Airline_Network'].isin(airlines)) &
        (diverted_flights['FlightDate'] >= dates[0]) &
        (diverted_flights['FlightDate'] <= dates[1])
    ]
    
    fig = go.Figure()
    
    # Add diversion points - MUCH SMALLER
    div_airports = filtered['Div1Airport'].value_counts().head(15)
    div_lats = [get_coords(code, airports_clean)[0] for code in div_airports.index]
    div_lons = [get_coords(code, airports_clean)[1] for code in div_airports.index]
    
    fig.add_trace(go.Scattergeo(
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
    
    fig.update_layout(
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
    
    return fig

@pn.depends(airline_select.param.value, date_range.param.value)
def airline_stats(airlines, dates):
    filtered = diverted_flights[
        (diverted_flights['Marketing_Airline_Network'].isin(airlines)) &
        (diverted_flights['FlightDate'] >= dates[0]) &
        (diverted_flights['FlightDate'] <= dates[1])
    ]
    
    print(f"DEBUG: Selected airlines: {airlines}")
    print(f"DEBUG: Filtered records: {len(filtered)}")
    
    if len(filtered) == 0:
        return pn.pane.HTML("<p>No data for selected filters</p>")
    
    fig = go.Figure()
    
    airline_counts = filtered['Marketing_Airline_Network'].value_counts()
    
    fig.add_trace(go.Bar(
        x=airline_counts.index,
        y=airline_counts.values,
        marker=dict(color='steelblue'),
        hovertemplate='<b>%{x}</b><br>Diversions: %{y}<extra></extra>'
    ))
    
    fig.update_layout(
        title=f'Diversions by Airline ({len(filtered)} total)',
        xaxis_title='Airline',
        yaxis_title='Number of Diversions',
        height=400,
        showlegend=False
    )
    
    return fig

@pn.depends(airline_select.param.value, date_range.param.value)
def summary_stats(airlines, dates):
    filtered = diverted_flights[
        (diverted_flights['Marketing_Airline_Network'].isin(airlines)) &
        (diverted_flights['FlightDate'] >= dates[0]) &
        (diverted_flights['FlightDate'] <= dates[1])
    ]
    
    return f"""
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">
        <div style="background: #E3F2FD; padding: 20px; border-radius: 8px; text-align: center;">
            <h3 style="margin: 0; color: #1976D2;">{len(filtered):,}</h3>
            <p style="margin: 0; color: #666;">Total Diversions</p>
        </div>
        <div style="background: #F3E5F5; padding: 20px; border-radius: 8px; text-align: center;">
            <h3 style="margin: 0; color: #7B1FA2;">{filtered['Div1Airport'].nunique()}</h3>
            <p style="margin: 0; color: #666;">Diversion Airports</p>
        </div>
        <div style="background: #E8F5E9; padding: 20px; border-radius: 8px; text-align: center;">
            <h3 style="margin: 0; color: #388E3C;">{filtered['DepDelay'].mean():.1f}</h3>
            <p style="margin: 0; color: #666;">Avg Departure Delay (min)</p>
        </div>
    </div>
    """

# Layout
dashboard = pn.Column(
    "# Flight Diversions Dashboard",
    pn.Row(
        pn.Column(airline_select, width=300),
        pn.Column(date_range, width=500)
    ),
    pn.Column(summary_stats, height=120),
    pn.Row(
        pn.Column(diversion_map, width=700),
        pn.Column(airline_stats, width=500)
    ),
    scroll=True
)

dashboard.servable()