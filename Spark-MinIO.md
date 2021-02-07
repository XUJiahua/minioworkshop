
### Setup Minio

```
make minio-server
```

http://localhost:9000
minio/minio123

### Setup Spark

download spark-3.0.1-bin-hadoop3.2 from https://spark.apache.org/downloads.html

copy spark-defaults.conf to spark-3.0.1-bin-hadoop3.2/conf/

spark-defaults.conf contains:

```
spark.hadoop.fs.s3a.access.key minio
spark.hadoop.fs.s3a.secret.key minio123
spark.hadoop.fs.s3a.endpoint http://localhost:9000
spark.hadoop.fs.s3a.impl org.apache.hadoop.fs.s3a.S3AFileSystem
spark.hadoop.fs.s3a.path.style.access true
```

### Spark-MinIO read/write

```
cd spark-3.0.1-bin-hadoop3.2

./bin/spark-submit \
  --master=local \
  --packages=org.apache.hadoop:hadoop-aws:3.2.0 \
  ../spark-minio-rw.py
```

