# Databricks notebook source
# DBTITLE 1,install latest pkg from github
# MAGIC %sh 
# MAGIC #pip install mlflow-export-import
# MAGIC pip install git+https:///github.com/mlflow/mlflow-export-import/#egg=mlflow-export-import

# COMMAND ----------

# DBTITLE 1,we can see the s3 mount from %sh :)
# MAGIC %sh ls /dbfs/mnt/ccidsdatascidatalake/

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
os.environ["DATABRICKS_HOST"] = "https://adb-374784251182712.12.azuredatabricks.net/"
os.environ["DATABRICKS_TOKEN"] = "dapidb973ceb6dac26397c3d9c0b3d4158e5"

# COMMAND ----------

# DBTITLE 1,verify env vars
# MAGIC %sh
# MAGIC echo $MLFLOW_EXPORT_IMPORT_LOG_OUTPUT_FILE
# MAGIC echo $MLFLOW_EXPORT_IMPORT_LOG_FORMAT
# MAGIC echo $MLFLOW_TRACKING_URI

# COMMAND ----------

# DBTITLE 0,`export-models` options
# MAGIC %sh 
# MAGIC export-experiments --help

# COMMAND ----------

# DBTITLE 1,cli execution
# MAGIC %sh 
# MAGIC export-experiments \
# MAGIC   --output-dir /dbfs/mnt/ccidsdatascidatalake/mlflow-migration-01/experiments \
# MAGIC   --experiments all \
# MAGIC   --run-start-time 2022-11-01 \
# MAGIC   --export-permissions True \
# MAGIC   --notebook-formats SOURCE \
# MAGIC   --use-threads True

# COMMAND ----------


