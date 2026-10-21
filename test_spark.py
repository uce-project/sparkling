from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("KaliPySparkTest")
    .master("local[*]")
    .getOrCreate()
)

print("Spark version:", spark.version)

data = [(1, "Python"), (2, "Spark"), (3, "Kali Linux")]
df = spark.createDataFrame(data, ["id", "technology"])

df.show()

spark.stop()
