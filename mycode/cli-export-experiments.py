# Databricks notebook source
# MAGIC %md ## Libs

# COMMAND ----------

# DBTITLE 1,install latest pkg from github
# MAGIC %sh 
# MAGIC #pip install mlflow-export-import
# MAGIC pip install git+https:///github.com/mlflow/mlflow-export-import/#egg=mlflow-export-import

# COMMAND ----------

# DBTITLE 1,we can see the s3 mount from %sh :)
# MAGIC %sh ls /dbfs/mnt/aws-ds-non-prod

# COMMAND ----------

# MAGIC %run ./credentials

# COMMAND ----------

# MAGIC %md ## Setup

# COMMAND ----------

# DBTITLE 1,variables
dbutils.widgets.dropdown("platform","",["", "azure", "aws"])
platform = dbutils.widgets.get("platform")

credentials_path = get_credentials_path(platform)

# COMMAND ----------

# DBTITLE 1,set env vars
import os 
from datetime import datetime
import pytz

cst = pytz.timezone('US/Central')
now = datetime.now(tz=cst)
date = now.strftime("%Y%m%d_%H%M")
 
logfile = f"export_experiments_{date}.log"
os.environ["MLFLOW_EXPORT_IMPORT_LOG_OUTPUT_FILE"] = logfile 

os.environ["MLFLOW_EXPORT_IMPORT_LOG_FORMAT"]="%(threadName)s-%(levelname)s-%(message)s"

os.environ["MLFLOW_TRACKING_URI"]="databricks"

with open(credentials_path) as f:
  os.environ["DATABRICKS_HOST"]  = f.readline().strip("\n")
  os.environ["DATABRICKS_TOKEN"] = f.readline().strip("\n")

# COMMAND ----------

# DBTITLE 1,verify env vars
# MAGIC %sh
# MAGIC echo $MLFLOW_EXPORT_IMPORT_LOG_OUTPUT_FILE
# MAGIC echo $MLFLOW_EXPORT_IMPORT_LOG_FORMAT
# MAGIC echo $MLFLOW_TRACKING_URI
# MAGIC # echo $DATABRICKS_HOST
# MAGIC # echo $DATABRICKS_TOKEN

# COMMAND ----------

# MAGIC %md ## Execute

# COMMAND ----------

# DBTITLE 1,cli execution | all
# MAGIC %sh 
# MAGIC export-experiments \
# MAGIC   --output-dir /dbfs/mnt/aws-ds-non-prod/mlflow-migration-experiments/experiments \
# MAGIC   --experiments all \
# MAGIC   --run-start-time 2024-11-09 \
# MAGIC   --export-permissions True \
# MAGIC   --notebook-formats SOURCE \
# MAGIC   --use-threads True
