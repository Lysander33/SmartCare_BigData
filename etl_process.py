from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# 初始化 Spark Session 并关联 Hive
spark = SparkSession.builder \
    .appName("SmartElderlyCare_ETL") \
    .config("spark.sql.warehouse.dir", "hdfs://hadoop01:9000/user/hive/warehouse") \
    .enableHiveSupport() \
    .getOrCreate()

def clean_data():
    # 1. 从 Hive 读取原始数据
    raw_df = spark.sql("SELECT * FROM medical_db.raw_elderly_data")

    # 2. 数据清洗逻辑
    # 过滤年龄小于 60 的异常数据，处理缺失的健康等级
    cleaned_df = raw_df.filter(col("age") >= 60) \
        .fillna({"health_level": "Unknown"}) \
        .withColumn("service_duration", col("service_duration").cast("float"))

    # 3. 将清洗后的数据保存到 Hive 的新表
    cleaned_df.write.mode("overwrite").saveAsTable("medical_db.cleaned_elderly_data")
    print("ETL Process Completed Successfully.")

if __name__ == "__main__":
    clean_data()
