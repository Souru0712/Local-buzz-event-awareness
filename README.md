# Automated Traffic Data ETL for Timely Urban Insights

**The goal is to build an automatic, low-latency pipeline that transforms high volume traffic data from around NYC to gain insight on traffic congestion and rush hour patterns, 
and the effect of weather, lane closures, incidents, and events**

The major tools being used:
- Amazon S3 for storing API data
- Spark for distributed transformation
- PostgreSQL for storing curated data
- Superset for visualization
- Airflow for scheduling tasks
- Docker for maintaining Airflow services

![project flowchart](Project_Flowchart.jpeg)
## Data Flow Description
The data comes from New York City's Department of Transportation public API, which is then collected and stored inside five S3 buckets, each representing a borough. Pyspark is used to <> <> <> which is then loaded into PostgreSQL for querying

# Setup and Execution
