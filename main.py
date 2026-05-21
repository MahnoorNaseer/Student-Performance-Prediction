from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").getOrCreate()

print("Spark Version:", spark.version)

df = spark.createDataFrame([("Ali", 20), ("Sara", 22)], ["Name", "Age"])
df.show()