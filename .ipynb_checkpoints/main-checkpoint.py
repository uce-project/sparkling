
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("My-app").getOrCreate()

print("Spark started")

df = spark.read.csv("Reviews.csv", header=True, inferSchema=True)


df.printSchema()
result = spark.sql("""
    SELECT *
    FROM reviews
    WHERE Score >= 4
    LIMIT 20
""")

result.show()
spark.stop()
