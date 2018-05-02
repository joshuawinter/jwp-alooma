# jwp-alooma tech eval



This solution was designed for the following requirements:

1. Pull Data from Hubspot.  Using their API and Python, build out logic to extract Engagement data from their endpoint.
Organize this data and store it into a file structure that makes sense.
Auth: https://developers.hubspot.com/docs/overview (see demo key)
Engagments API: https://developers.hubspot.com/docs/methods/engagements/engagements-overview

2. Spin Up a relational db Instance, you can choose either:
    Postgres 9.4+
    MySQL 5.6+
    Oracle 11g+
    SQL server(but please provide the docker image tag for it)

3. Create a table and Load the Data In (this can be done during reads as well)

4. Write a SQL Query that pulls the Engagements per Day broken down by type.
You should expose both the counts per day and a rolling 2 week avg for each day.

Methodology:

1. hubspot-api-eng.py is a python v3.6 program with a dependency on requests==1.18.4 which it uses to interact with the hubspot api for engagements
(https://api.hubapi.com/engagements/v1/engagements/paged?hapikey=demo).  The program pulls down hubspot engagement results as json, parses the json and
grabs relevant fields in order to meet the reporting requirements above.

2. The program outputs the formatted results into a csv file called engagements.csv.  This file is then loaded into a mysql(google cloud sql instance) database using the scripts found
in /sql/sqlstuff.sql

3. Once the data is loaded into the table 'engagements' a view is created 'vw_engagements' for querying.  Unix timestamps have been converted to dates in the view.

4. Queries for the daily engagement counts by type as well as the rolling 2 week avg are also found in sqlstuff.sql.

TODO:

1. change outputs to gcp cloud storage bucket and run on app engine.  GCP requirements.txt and app.yaml are staged in gcp folder.




