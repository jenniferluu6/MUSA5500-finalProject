# Flight Diversions: Understanding Air Traffic Disruptions

A comprehensive data science analysis of U.S. flight diversions from July 2021 through December 2024, using temporal clustering and geospatial visualization to uncover patterns in aviation system disruptions.

**Live Documentation**: [GitHub Pages Site](https://jenniferluu6.github.io/MUSA5500-finalProject/)

---

## 📊 Project Overview

This project analyzes **64,815 flight diversions** from a dataset of **25.4 million flights** to understand when, where, and how diversions occur across the U.S. aviation network. The analysis combines data-driven clustering with interactive maps to reveal:

- **3 major diversion clusters** (San Diego, Dallas/Fort Worth, Chicago O'Hare)
- **System-wide vs. regional disruption patterns**
- **Significant differences in airline operational resilience** (American Airlines diverts 29% more than Delta)
- **Consistent diversion hub airports** that absorb overflow capacity (DEN, IAD, LAX)

### Key Statistics

| Metric | Value |
|--------|-------|
| **Analysis Period** | July 2021 - December 2024 (45 months) |
| **Total Flights** | 25,386,632 |
| **Total Diversions** | 64,815 |
| **Diversion Rate** | 0.26% |
| **Airlines** | 10 major carriers |
| **Airports Affected** | 377 diversion airports |
| **Average Arrival Delay** | 278.8 minutes |
| **Top Diversion Hubs** | DEN (1,935), IAD (1,680), LAX (1,608) |

---

## 🔍 Key Findings

### Finding 1: American Airlines' Operational Challenge
American Airlines accounts for **27.7% of all diversions** despite operating only 18-22% of flights:
- AA: 18,004 diversions (27.7%)
- UA: 13,921 diversions (21.4%)
- DL: 10,886 diversions (16.8%)

**Implication**: Suggests operational inefficiencies in scheduling, recovery procedures, or network design compared to Delta.

### Finding 2: System-Wide vs. Regional Disruptions
Diversion clusters fall into two categories:

**System-Wide (SAN - December 2024)**
- Only 48.3% to primary airport
- 290 total diversions across 60 destinations
- Affected 73 origin airports
- Cascades across entire U.S. network

**Regional (DFW, ORD)**
- 57-59% to primary airport
- 150-200 total diversions
- Concentrated in geographic region (Texas, Midwest)
- Natural regional coordination

### Finding 3: Consistent Diversion Hub Pattern
Same airports repeatedly absorb diversions:
- **West Coast**: ONT, PHX, LAX, SFO
- **South-Central**: IAH, DFW, SAT, AUS
- **Midwest**: IND, STL, MKE

---

## 🛠️ Technologies & Methods

### Data Processing
- **Pandas** (2.3.1) - Data manipulation and aggregation
- **NumPy** (2.3.1) - Numerical analysis
- **GeoPandas** (1.0.1) - Geospatial analysis

### Analysis Methods
- **Temporal Clustering** - 12-hour threshold to identify disruption events
- **Geospatial Analysis** - Airport coordinates and flight path visualization
- **Statistical Analysis** - Airline comparison and delay impact assessment

### Visualization
- **Plotly** (6.5.0) - Interactive geospatial maps
- **Panel** (1.7.5) - Interactive dashboard
- **Matplotlib** - Static visualizations

### Documentation
- **Quarto** - Documentation site on GitHub Pages
- **Jupyter Notebook** - Analysis code and narrative

---

## 📁 Project Structure

```
MUSA5500-finalProject/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── app.py                             # Panel dashboard app
│
├── notebooks/
│   └── 5500_flightDiversion.ipynb    # Complete analysis code
│
├── data/
│   ├── diverted_flights.csv          # Cleaned diversion data
│   └── airports.csv                  # Airport coordinates
│
├── docs/                              # Quarto documentation site
│   ├── index.qmd                     # Homepage
│   ├── 01-collection.qmd             # Data collection & preparation
│   ├── 02-analysis.qmd               # Analysis methodology
│   ├── 03-visualization.qmd          # Visualizations with maps
│   ├── 04-results.qmd                # Results & conclusions
│   ├── 05-dashboard.qmd              # Dashboard documentation
│   └── _quarto.yml                   # Quarto configuration
│
└── visualizations/
    ├── cascade_cluster_1_SAN.html    # SAN individual cluster
    ├── system_wide_cluster_1_SAN.html # SAN system-wide
    ├── cascade_cluster_2_DFW.html    # DFW individual cluster
    ├── system_wide_cluster_2_DFW.html # DFW system-wide
    ├── cascade_cluster_3_ORD.html    # ORD individual cluster
    └── system_wide_cluster_3_ORD.html # ORD system-wide
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.13
- conda or pip
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/jenniferluu6/MUSA5500-finalProject.git
cd MUSA5500-finalProject
```

2. **Create environment**
```bash
conda create -n geospatial python=3.13
conda activate geospatial
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Analysis

**View the Jupyter Notebook:**
```bash
jupyter notebook notebooks/5500_flightDiversion.ipynb
```

**Run the Interactive Dashboard:**
```bash
conda activate geospatial
python app.py
```
Then visit: `http://localhost:5006`

**View Documentation Site (locally):**
```bash
cd docs
quarto preview
```

---

## 📊 Interactive Dashboard

The Panel dashboard allows you to explore the data with filters:

- **Airline Filter** - Select one or more airlines to compare
- **Date Range Slider** - Focus on specific time periods
- **Real-time Statistics** - Total diversions, diversion airports, avg delays
- **Top Diversion Airports Map** - Interactive geographic visualization
- **Airline Comparison Chart** - Side-by-side airline metrics

**Running locally:**
```bash
python app.py
```

Visit `http://localhost:5006` in your browser.

---

## 📚 Documentation

Full documentation available at: [GitHub Pages](https://jenniferluu6.github.io/MUSA5500-finalProject/)

### Documentation Sections:

1. **[Data Collection](docs/01-collection.qmd)**
   - BTS OTMC-OTP data source
   - Data cleaning pipeline
   - Quality assessment
   - 25.4M flight records → 64.8K diversions

2. **[Analysis Methodology](docs/02-analysis.qmd)**
   - Temporal clustering (12-hour threshold)
   - Geospatial analysis approach
   - Statistical analysis methods
   - Airline comparison methodology

3. **[Visualizations](docs/03-visualization.qmd)**
   - 6 interactive Plotly maps
   - Individual vs. system-wide cluster views
   - Bezier curve flight path visualization
   - Pattern interpretations

4. **[Results & Conclusions](docs/04-results.qmd)**
   - Key findings and surprises
   - Operational implications
   - Recommendations for airlines/airports/policy
   - Future research directions

5. **[Dashboard Documentation](docs/05-dashboard.qmd)**
   - How to use interactive dashboard
   - Filter explanations
   - Interpretation guide

---

## 🔬 Analysis Methodology

### Temporal Clustering

The core analysis uses a 12-hour temporal clustering approach:

```python
def dest_cluster(group, max_gap_hours=12):
    group = group.sort_values('FlightDate')
    group['time_since_last'] = group['FlightDate'].diff().dt.total_seconds() / 3600
    group['new_cluster'] = (group['time_since_last'] > max_gap_hours).fillna(True)
    group['cluster_id'] = group['new_cluster'].cumsum()
    return group
```

**Why 12 hours?**
- Aligns with airline operational recovery cycles
- Captures cascading effects from weather systems
- Prevents false clustering of unrelated events

### Geospatial Visualization

Flight paths visualized using quadratic Bezier curves:
- Curved paths separate overlapping routes
- Color-coded by airline for pattern recognition
- Interactive Plotly maps enable exploration

---

## 💡 Key Insights & Recommendations

### For Airlines:
1. **Pre-position Resources** - Station crews/aircraft at DEN, IAD, LAX during high-risk periods
2. **Tiered Protocols** - Develop different response strategies for regional vs. system-wide events
3. **Benchmark Operations** - Compare practices against DL/UA to reduce diversion rates
4. **Route Risk Assessment** - Monitor routes with historical high diversion frequency

### For Airports:
1. **Capacity Planning** - Expect consistent diversion traffic at hub airports
2. **Regional Coordination** - Establish agreements within geographic clusters (Texas, Midwest)
3. **Ground Services** - Position crews for surge capacity during disruptions

### For Policy Makers:
1. **Infrastructure Investment** - Support secondary hubs that absorb diversions (DEN, IAD, LAX)
2. **ATC Coordination** - Establish protocols between regional airport clusters
3. **System Monitoring** - Track whether network is near saturation during peak periods

---

## 📈 Data Sources

- **BTS OTMC-OTP Database**: https://www.transtats.bts.gov/
- **FAA Airport Data**: https://www.faa.gov/
- **OpenFlights Database**: https://openflights.org/

---

## 🔄 Reproducibility

All analysis is fully reproducible:

1. **Data Access** - Download BTS data from public portal
2. **Code Available** - Complete analysis in Jupyter notebook
3. **Environment Specified** - Python 3.13 with documented dependencies
4. **Documentation** - Step-by-step data pipeline documented

**To reproduce:**
```bash
# 1. Download BTS data (45 months: 2021-07 to 2024-12)
# 2. Place in /data directory
# 3. Run notebook or execute data cleaning script
# 4. Analysis outputs to diverted_flights.csv
```

---

## 📋 Requirements

See `requirements.txt`:

```
streamlit==1.28.0
plotly==5.18.0
pandas==2.3.1
numpy==2.3.1
geopandas==1.0.1
scipy
jupyter
quarto
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🎓 About This Project

**Course**: MUSA 5500: Data Science for Planning and Policy  
**University**: University of Pennsylvania  
**Semester**: Fall 2024  
**Author**: Jun  
**Completed**: December 2024

This project demonstrates:
- Multi-source data integration and validation
- Complex geospatial and temporal analysis
- Interactive visualization for exploration
- Clear communication to technical and non-technical audiences
- Actionable insights for industry stakeholders

---

## 📞 Questions or Feedback?

This project is open for discussion. For questions about:
- **Methodology** - See [Analysis](docs/02-analysis.qmd) documentation
- **Data** - See [Data Collection](docs/01-collection.qmd) documentation
- **Visualizations** - See [Visualizations](docs/03-visualization.qmd) documentation
- **Results** - See [Results & Conclusions](docs/04-results.qmd) documentation

---

## 📄 License

This project is available for educational and research purposes.

---

## 🔗 Related Links

- **GitHub Repository**: https://github.com/jenniferluu6/MUSA5500-finalProject
- **Documentation Site**: https://jenniferluu6.github.io/MUSA5500-finalProject/
- **BTS Data Portal**: https://www.transtats.bts.gov/
- **FAA Data**: https://www.faa.gov/

---

**Last Updated**: December 12, 2025  
**Data Current Through**: December 31, 2024
