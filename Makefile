setup:
	mc alias set minio http://localhost:9000 minio minio123
iris:
	mc mb minio/spark && mc cp iris.csv minio/spark
minio-server:
	docker-compose up
