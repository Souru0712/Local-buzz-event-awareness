# Automated Traffic Data ETL for Timely Urban Insights

The goal is to build an automatic, low-latency pipeline that transforms high volume traffic data from around NYC to gain insight on traffic congestion and rush hour patterns, 
and the effect of weather, lane closures, incidents, and events

The major tools being used:
- Amazon S3 for storing API data
- Spark for distributed transformation
- PostgreSQL for storing curated data
- Superset for visualization

![project flowchart](ProjectFlowchart.jpeg)
