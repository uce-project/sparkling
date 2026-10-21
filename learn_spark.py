from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("My-app").getOrCreate()
print("spark started")
data = [
    ("Joseph",20),
    ("Sebastian",17)
]
df = spark.createDataFrame(data,["name","age"])
print(df)
spark.stop()