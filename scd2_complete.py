# =============================================================================
# SCD TYPE 2 - COMPLETE IMPLEMENTATION (DATABRICKS / PYSPARK NOTEBOOK)
# =============================================================================
# Run each cell one by one in your notebook.
# You can update the source data in CELL 4 to test different scenarios.
# =============================================================================


# -----------------------------------------------------------------------------
# CELL 1 — IMPORTS
# -----------------------------------------------------------------------------

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, lit, current_date, monotonically_increasing_id,
    row_number, to_date
)
from pyspark.sql.window import Window
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType
from delta.tables import DeltaTable

# If running on Databricks, SparkSession is already available as `spark`
# If running locally, uncomment the lines below:
# spark = SparkSession.builder \
#     .appName("SCD2_Demo") \
#     .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
#     .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
#     .getOrCreate()

print("✅ Imports done.")


