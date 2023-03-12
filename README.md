# Section 1 Assignment
## Problem statement
Provision one database of your choosing (SQL, NoSQL, Graph).  Write a python ETL that ingests the provided data, transforms it in some way, and loads it into the database. This should be reproducible code with documentation. (Terraform / Cloudformation / Ansible, docker-compose etc). 
## Solution
In order to solve the given problem, the excel file containing the source data was uploaded in /data folder of the repo. The excel file was ingested to a in memory pandas dataframe and the data was transformed and then uploaded to a AWS provisioned postgres database. Below are the steps mentioned in details - 

1. Excel file from /data folder was uploaded to a pandas dataframe.
2. In the pandas dataframe an unique , not null idex column (different than id column in data) was added.
3. Added file_name column which has the source file name.
4. Added updated_timestamp column which has the ingestion timestamp.
5. Converted the data in columns first_name,last_nam and gender column to lower case.
6. Uplaoded the transformed dataframe to AWS provisioned postgresql.

### Code Features

The ETL is done from src/etl.py file. Below mentioned are some of the best practices and features of the code.

* The whole python file is broken into multiple functions in order to maintain the single responsibilty principle.
* Each function has its own docstrings describing the parmenters and returns.
* The file name and connection string is NOT hardcoded in the function body and passed as part of the function call args.
* The file name is dynamically read from data folder to a list. This allows the reusability of the code for multiple file ingestion. 
* Currently the processis set to TRUNCATE-LOAD and can easily be changed to APPEND by changing the to_sql argument in line 67.

## Steps to run the code

The developemnt is done is github codespaces and has been end to end dockerized with docker-compose.yml. In order to run the code we just have to execute 
>  docker-compose up


If the code is executed successfully, we should get the below messages -

```delloiteassignments_1  | Data from  excel file has been loaded to pandas dataframe.....
delloiteassignments_1  | Data is pandas dataframe has been transformed.....
delloiteassignments_1  | Data ingested in postgres successfully.....```
