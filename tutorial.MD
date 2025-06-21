## AUTOMATE ETL USING GOOGLE CLOUD

Step 1: Set up a Google Cloud account and enable the necessary APIs. For this particular use, we need to enable Bigquery, Cloud Storage, and Cloud DataFusion.

Step 2: Know where your source data is and what format it is in. For this example, we will assume it is in a CSV file on our local machine.

Step 3: Know where your destination table is and how you want to push the data to that table. For this example, we will assume it is in a Bigquery table.

Step 4: Create a Cloud Storage bucket to store the CSV file. You can do this by going to the Cloud Storage page in the Google Cloud Console and clicking on "Create bucket". Give the bucket a name and select the location. Then, upload your CSV file to the bucket. The csv file data upload can be our extract. Also, know that this data should be pushed automatedly so you need to set up google cloud cli or SDK on the host machine to automate the process.

Step 5: To automatically use the cli to push the data to the destination table, you can use the following command:
 - install the cli, initialize it and enable a auto login.
 - gcloud auth application-default login
 - install google cloud storage library in the virtual environment or host machine.
 - install google cloud bigquery library in the virtual environment or host machine.
 - push the data to cloud storage.

Step 6: Create a Cloud Data Fusion pipeline to load the data from Cloud Storage into Bigquery. You can do this by going to the Cloud Data Fusion page in the Google Cloud Console and creating an instance. Then, create a pipeline and add a source, a transformation, and a sink. The source will be the Cloud Storage bucket, the transformation will be a simple load into Bigquery, and the sink will be the Bigquery table.

Deploy the data fusion integration pipeline. This will create a scheduled task that will run at the specified interval and load the data from Cloud Storage. if there are any issues check the logs.

Step 7: Check the Bigquery table to see if the data has been loaded correctly. You can do this by going to the Bigquery page in the Google Cloud Console and selecting the table. Then, click on " Preview" to see the data.


### for this particular use case, we will use python to load data from our local machine to cload storage and then use cloud data fusion to load the data from cloud storage to bigquery.

- the python file to be used to load the data into cloud storage is the extract.py file.
- the python file to be used to create the csv data is the create_csv.py file.
- if you want to do some visualization, you can connect looker/powerbi to bigquery and create a dashboard.


Step 8: Automate the Pipeline with AirFlow.
- create a composer instance and create a dag that will run the extract.py and then the datafusion pipeline.
- create a scripts folder in the dags folder and then place the create_csv.py and the extract.py files in there.
- in your dags.py file, import the Operators you will need to run the processes. Bash operator for bash processes and the Data Fusion Operator for the data fusion integration.
- remeber to install all necessary modeules in the composer instance.
- the dag will run every 5 minutes and will load the data from the csv file into big
- trigger your dag and check the logs to see if there are any issues.

