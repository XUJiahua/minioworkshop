from __future__ import print_function

from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("MinIO")\
        .getOrCreate()

    df = spark.read.load("s3a://spark/iris.csv", format="csv", sep=",", inferSchema="true", header="true")
    df.write.mode("overwrite").save("s3a://spark/iris-count", format="json")

    spark.stop()
